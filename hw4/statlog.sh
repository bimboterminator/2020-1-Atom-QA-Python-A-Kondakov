#!/usr/bin/env bash
if [ $# -eq 0 ]; then
  echo "No arguments: filename required"
  exit
fi
file=($1)
req_num=$(cat $file |grep ' - - '| wc -l)
echo -e "\nNumber of requests:$req_num\n" >> report

num_req_method=$(cat $file | cut -f6 -d" "| cut -c2-|grep -e "^[[:upper:]]"| sort |uniq  -c)
echo -e "Request methods:\n$num_req_method\n" >> report 

top_req_by_size=$(cat $file | sort  -k10r,10 -k7,7 -s|cut -f7,9 -d" "|awk '!visited[$0]++ {print $0}'| head)
echo -e "Top 10 by size:\n$top_req_by_size\n" >> report

top_req_40x=$(awk '($9 ~ /^4/)' $file | awk '{print $7,$9}' | sort | uniq -c | sort -r -k3 |tr -s " "| cut -f3,4 -d" "|head )
echo -e "Top 10 with client errors:\n$top_req_40x\n" >> report

top_req_50xSize=$( cat $file | awk -F' ' -e '$9 ~ /[5??]/ {print $0}'|sort -nt' ' -k 10 -r| cut -f1,7,9 -d" "|awk '!visited[$0]++{print $0}'|head)
echo -e "Top 10 with server errors:\n$top_req_50xSize\n" >> report
