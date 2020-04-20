"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

set1 = 'paraparaparadise'
set2 = 'paragraph'


def get_bigram(seq: list):
    return [seq[i:i+2] for i in range(len(seq)-1)]


s1 = 'paraparaparadise'
s2 = 'paragraph'

X = set(get_bigram(list(s1)))
Y = set(get_bigram(list(s2)))

print(f'和集合:{X|Y}')
print(f'積集合:{X&Y}')
print(f'差集合:{X-Y}')
if 'se' in (X | Y):
    print('seというbi-gramがXおよびYに含まれる')
else:
    print('seというbi-gramがXおよびYに含まれない')
