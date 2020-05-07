# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


prog = re.compile(r"\[\[Category:(\w+)\]\]")


def search_category_name(data: str):
    return prog.finditer(data)


england_texts = []
with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            england_texts.append(line)
for matched in search_category_name("".join(england_texts)):
    for m in matched.groups(""):
        print(m)
