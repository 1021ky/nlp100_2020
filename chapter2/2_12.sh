#!/bin/bash
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt

echo 'result col1'
cat col1.txt
echo 'result col2'
cat col2.txt