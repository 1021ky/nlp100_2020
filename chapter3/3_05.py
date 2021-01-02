# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ

import re
import json

re_basic_info = re.compile(
    r"^\{\{基礎情報(?P<info>.*?)^\}\}$",
    flags=re.MULTILINE | re.DOTALL | re.UNICODE,
)

re_element = re.compile(
    r"|(?P<key>\w*)\s*\=\s*(?P<value>\w*?)$",
    flags=re.MULTILINE | re.DOTALL | re.UNICODE,
)


if __name__ == "__main__":
    texts = []
    with open("jawiki-country.json", encoding="utf-8") as f:
        for line in f.readlines():
            j = json.loads(line)
            texts.append(j.get("text", ""))
    for text in texts:
        for matched in re_basic_info.finditer(text):
            basic_info = matched.group("info")
            for m in re_element.finditer(basic_info):
                key = m.group("key")
                value = m.group("value")
                if not (key == None and value == None):
