"""
07. テンプレートによる文生成Permalink
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""


def get_formatted(x: int, y: str, z: float):
    return f'{x}時の{y}は{z}'


print(get_formatted(12, '気温', 22.4))
