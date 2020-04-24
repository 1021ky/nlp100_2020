# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

rows = ''
with open('col1.txt') as f1, open('col2.txt') as f2:
    for col1, col2 in zip(f1.readlines(), f2.readlines()):
        rows += (col1.replace('\n', '') + '\t' + col2)

with open('joined.txt', mode='w') as f:
    f.write(rows)
