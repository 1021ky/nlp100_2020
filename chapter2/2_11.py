# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
with open('popular-names.txt') as f:
    data = f.read()
    result = data.replace('\t', ' ')

    print(result)
