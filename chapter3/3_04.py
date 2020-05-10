# 記事から参照されているメディアファイルをすべて抜き出せ

import re


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


prog = re.compile(
    r"[^\w,()](?P<mediafile_name>[\w\ \-,()\']*?\.(jpg|JPG|jpeg|JPEG|svg|png|PNG))\W")


def search_mediafile_ref(data: str):
    return prog.finditer(data)


england_texts = []
with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            england_texts.append(line)

for matched in search_mediafile_ref("".join(england_texts)):
    print(matched.group("mediafile_name"))
