# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import re


def is_england_item(data: str):
    if "イギリス" in data:
        return True
    return False


prog = re.compile(
    r"(?P<section_level_start>==+) (?P<section_name>\w+) (?P<section_level_end>==+)")


def search_section(data: str):
    return prog.finditer(data)


england_texts = []
with open("jawiki-country.json") as f:
    for line in f.readlines():
        if is_england_item(line):
            england_texts.append(line)

for matched in search_section("".join(england_texts)):
    sls = matched.group("section_level_start")
    level = sls.count("=") - 1
    name = matched.group("section_name")
    print(f"{name} {level}")
