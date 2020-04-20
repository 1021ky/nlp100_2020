"""
08. 暗号文Permalink
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(param: str):
    result = ''
    for s in param:
        if s.isalpha() and not s.isupper():
            result += chr(219 - ord(s))
        else:
            result += s
    return result


encrypt = cipher('Permalink')
print(encrypt)
decrypt = cipher(encrypt)
print(decrypt)
