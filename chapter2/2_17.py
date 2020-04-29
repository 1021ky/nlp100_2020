# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
# cat popular-names.txt | cut -d DELIM -f 1 | sort | uniq
cel1_list = []
with open('popular-names.txt') as f:
    for line in f.readlines():
        cells = line.split('\t')
        cel1_list.append(cells[0])

set_list = list(set(cel1_list))
set_list.sort()

for c in set_list:
    print(c)

