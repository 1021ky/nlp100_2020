# popular-names.txtは，アメリカで生まれた赤ちゃんの「名前」「性別」「人数」「年」をタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，popular-names.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

result = 0
with open('popular-names.txt') as f:
    result = len(f.readlines())
print(result)
