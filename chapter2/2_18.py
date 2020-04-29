# 各行を3コラム目の数値の逆順で整列せよ
# （注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）

# 確認コマンド
# * sort -r -k 3 popular-names.txt
# * diff <(sort -r -k 3 popular-names.txt) <(python 2_18.py) ※ bashで
columns_tuple_list = []

with open('popular-names.txt') as f:
    for line in f.readlines():
        columns = line.split('\t')
        columns_tuple_list.append((columns[2], line))
sorted_columns = sorted(
    columns_tuple_list, key=lambda x: x[0], reverse=True)

for _, c in sorted_columns:
    print(c, end='')
