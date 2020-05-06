# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import codecs
import json


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            print(line, end="")
# data.append(json.loads(line, object_hook=dict))


# england_texts = []
# for d in data:
#     if is_england_item(d.get("text", "")):
#         england_texts.append(d.get("text"))
# print(codecs.decode(json.dumps(england_texts), encoding='unicode-escape'))
