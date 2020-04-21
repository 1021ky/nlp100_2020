#!/bin/bash
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
echo 'exe sed'
sed -e 's/\t/ /g' popular-names.txt
echo 'exe tr'
cat popular-names.txt | tr '\t' ' '
echo 'exe expand'
expand -t 1 popular-names.txt