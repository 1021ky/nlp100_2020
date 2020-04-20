"""
09. TypoglycemiaPermalink
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
"""

from random import shuffle


def prog(param: str):
    # 単語をスペース区切りで取り出す
    words = param.split()
    # 長さ5以上の単語を対象にする
    result = []
    for word in words:
        pass
        if len(word) <= 4:
            result.append(word)
            continue
        # 先頭と末尾の文字を残し、それ以外はランダムに並び替える
        rdm = list(word[1:-1])
        shuffle(rdm)
        changed = word[0] + ''.join(rdm) + word[-1]
        result.append(changed)
    return result


s = 'I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind .'
for remove in [':', '.']:
    s = s.replace(remove, '')
result = prog(s)
print(result)
