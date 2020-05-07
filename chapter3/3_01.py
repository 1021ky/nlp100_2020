# 記事中でカテゴリ名を宣言している行を抽出せよ．


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


england_texts = []
with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            england_texts.append(line)
for text in england_texts:
    if "Category" in text:
        print(text)
