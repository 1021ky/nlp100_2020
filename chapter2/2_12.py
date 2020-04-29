# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
col1 = ''
col2 = ''
with open('popular-names.txt') as f:
    for line in f.readlines():
        cells = line.split('\t')
        col1 += cells[0] + '\n'
        col2 += cells[1] + '\n'

with open('col1.txt', mode='w') as f:
    f.write(col1)

with open('col2.txt', mode='w') as f:
    f.write(col2)
