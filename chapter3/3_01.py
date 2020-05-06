# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            print(line, end="")
