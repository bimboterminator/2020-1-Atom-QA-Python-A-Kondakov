### Анализ логов nginx
### statlog.sh
Вызывается ./statlog.sh либо bash statlog.sh.Параметром передается имя файла(если он в cwd) или полный путь до файла.
В процессе выполнения скрипта в текущей рабочей директории создается файл с отчетом report.
### Основные функции
1.req_num=$(cat $file |grep ' - - '| wc -l) 

Считатся общее количество запросов, полагаяю, что запрос начинается с ' - - '

2.num_req_by_method=$(cat $file | cut -f6 -d" "| cut -c2-|grep -e "^[[:upper:]]"| sort |uniq  -c)

Идет подсчет количества запросов кажодого метода. Сначала выделятся поле с методом вида "МЕТОД, сортируется и считается количество повторябщихся
методов 

3.top_req_by_size=$(cat $file | sort  -k10r,10 -k7,7 -s|cut -f7,9 -d" "|awk '!visited[$0]++ {print $0}'| head)

Выводит 10 зпросов с наибольшим размером тела. Строка сортируется по размеру запроса, форматируется, и сливает одинаковые запросы

4.top_req_40x=$(awk '($9 ~ /^4/)' $file | awk '{print $7,$9}' | sort | uniq -c | sort -r -k3 |tr -s " "| cut -f3,4 -d" "|head )

Этой командой ведется поиск запросов, завершившихся клиентской ошибкой, и их сортировка. На выходе самые посещаемые ресурсы с клиентской ошибкой


 5.top_req_50xSize=$( cat $file | awk -F' ' -e '$9 ~ /[5??]/ {print $0}'|sort -nt' ' -k 10 -r| cut -f1,7,9 -d" "|awk '!visited[$0]++{print $0}'|head)
 
 Этой командой ведется поиск запросов, завершившихся серверной ошибкой, и их сортировка по размеру тела.
 На выходе самые посещаемые ресурсы с серверной ошибкой
 
 ###report
Отчет по логам, разделитель пусткая строка:
1.Количество запросов
2.Количество запросв кажого типа
3.10 самых  больших запросов в  формате url статус ответа
4.10 наиболее частых запросов с клиентой ошибкой в формате url статус ответа
5. 10 наиболее частых запросв с серверной ошбкой в формате ip-адрес url статус ответв

### anlog.py
Python-скрипт, позиционным параметром передается полный пусть к файлу или имя файла(если он в cwd) 
В результате работы формируется файл pyreport с аналгичой статистикой, разделитель 10 символов #
Также создается отчет в json формате, содержит список со всеми данными.