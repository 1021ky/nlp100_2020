""""Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

for remove_chr in (',', '.'):
    s = s.replace(remove_chr, '')
words = s.split()

result = [len(word) for word in words]
print(result)
