#!/usr/bin/env python
import re
import sys
import os
import json

def process_log(log_line):
    line_format = (
        r'(?P<ipaddress>.*?)\ \-\ \-\ \[(?P<dateandtime>.*?)\]\ \"(?P<request>.*?)\"\ (?P<statuscode>.*?)\ (?P<bytessent>.*?)\ \"(?P<referer>.*?)\"\ \"(?P<useragent>.*?)\"')
    request = re.match(line_format, log_line, re.IGNORECASE)
    if request:
        data = request.groupdict()
        dict = {
            'ip': data["ipaddress"],
            'time': data["dateandtime"],
            'url': data["request"].split(' ')[1],
            'bytes_sent': data["bytessent"],
            'referrer': data["referer"],
            'useragent': data["useragent"],
            'status': data["statuscode"],
            'method': data["request"].split(' ')[0]
        }
        return dict


def num_requests(logs):
    num = 0
    for line in logs:
        if line.find(' - - ') != -1:
            num += 1
    return num


def num_req_method(logs):
    methods = {'POST': 0, 'GET': 0, 'HEAD': 0, 'PUT': 0}
    for line in logs:
        d = process_log(line)
        if d:
            m = d['method']
            if m in methods.keys():
                methods[m] += 1
    return methods


def top_by_size(logs):
    requests = []
    for line in logs:
        req = process_log(line)
        if len(requests) == 0:
            requests.append(req)
            continue
        if req['bytes_sent'] == '-':
            continue
        small = min(requests, key=lambda x: int(x['bytes_sent']))

        if len(requests) == 10:
            prev = next((item for item in requests if item['url'] == req['url']), None)
            small = min(requests, key=lambda x: int(x['bytes_sent']))
            if prev and req['bytes_sent'] >= prev['bytes_sent'] and req['method'] != prev['method']:
                requests.remove(prev)
                requests.append(req)
            elif int(req['bytes_sent']) >= int(small['bytes_sent']):
                requests.remove(small)
                requests.append(req)
        elif len(requests) < 10:
            requests.append(req)

    requests.sort(key=lambda x: int(x['bytes_sent']))
    requests = requests[:10]
    requests.reverse()
    result = []
    for line in requests:
        new = {"url": line["url"],
               'code': line['status']
               }
        result.append(new)

    return result


def top_req_client_error(logs):
    requests = []

    for line in logs:
        req = process_log(line)
        status = req["status"]

        if status[0] == '4':
            if len(requests) == 0:
                requests.append([req, 1])
                continue
            flag = True
            for i in requests:
                if req['url'] == i[0]['url'] and status == i[0]["status"]:
                    i[1] += 1
                    flag = False
                    break

            if flag:
                requests.append([req, 1])

    requests.sort(key=lambda x: x[1], reverse=True)
    requests = requests[:10]
    result = []
    for line in requests:
        new = {"url": line[0]["url"],
               "ip": line[0]["ip"],
               "status": line[0]["status"],
               }
        result.append(new)

    return result


def top_req_server_error(logs):
    requests = []

    for line in logs:
        req = process_log(line)
        status = req["status"]

        if status[0] == '5':
            if len(requests) == 0:
                requests.append([req, 1])
                continue
            flag = True
            for i in requests:
                if req['url'] == i[0]['url'] and status == i[0]["status"] and req['bytes_sent'] >= i[0]['bytes_sent']:
                    i[1] += 1
                    flag = False
                    break

            if flag:
                requests.append([req, 1])

    requests.sort(key=lambda x: int(x[0]['bytes_sent']), reverse=True)
    requests = requests[:10]
    result = []
    for line in requests:
        new = {"url": line[0]["url"],
               "ip": line[0]["ip"],
               "status": line[0]["status"],
               }
        result.append(new)

    return result


def write_in_file(data, file):
    if isinstance(data, list):
        for line in data:
            print(line, file=file)
    else:
        print(data, file=file)


if __name__ == '__main__':

    if len(sys.argv) - 1 == 0:
        print('Filename or path required')
    else:
        filename = sys.argv[1]
        with open(filename, 'r') as log_file:
            logs = log_file.readlines()
            name = os.path.join(os.getcwd(), "pyreport")
            with open(f'{name}', 'w') as wfile:
                num = num_requests(logs)
                print('Number of requests:', file=wfile)
                write_in_file(num, wfile)
                print('#' * 10, file=wfile)

                num_req_method_lst = num_req_method(logs)
                print('Requests by method:', file=wfile)
                write_in_file(num_req_method_lst, wfile)
                print('#' * 10, file=wfile)

                top_by_size_lst = top_by_size(logs)
                print('Top by size:', file=wfile)
                write_in_file(top_by_size_lst, wfile)
                print('#' * 10, file=wfile)

                top_req_client_error_lst = top_req_client_error(logs)
                print('Top by client error:', file=wfile)
                write_in_file(top_req_client_error_lst, wfile)
                print('#' * 10, file=wfile)

                top_req_server_error_lst = top_req_server_error(logs)
                print('Top by server error:', file=wfile)
                write_in_file(top_req_server_error(logs), wfile)
                print('#' * 10, file=wfile)

            with open(f'{name}.json', 'w') as json_record:

                lst = [
                    {"count": num},
                    num_req_method_lst,
                    top_by_size_lst,
                    top_req_client_error_lst,
                    top_req_server_error_lst
                ]

                json.dump(lst, json_record, indent=3)

        log_file.close()
