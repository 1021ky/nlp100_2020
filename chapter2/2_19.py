# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

# 確認コマンド cat popular-names.txt | cut -f 1 | sort | uniq -c | sort -k 1 -r

cell1s = []
with open('popular-names.txt') as f:
    for line in f.readlines():
        cell1s.append(line.split('\t')[0])

word_occurency = {}
for c in set(cell1s):
    count = cell1s.count(c)
    word_occurency[c] = count

sorted_word_occurency = sorted(
    word_occurency.items(), key=lambda x: x[1], reverse=True)

for k, v in sorted_word_occurency:
    print(k, v)
