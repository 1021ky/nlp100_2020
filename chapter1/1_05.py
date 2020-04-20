"""与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def get_bigram(iterable):
    return [iterable[i:i+2] for i in range(len(iterable)-1)]


s = "I am an NLPer"

print(f'単語bi-gram:{get_bigram(s.split())}')
print(f'文字bi-gram:{get_bigram("".join(s.split()))}')
