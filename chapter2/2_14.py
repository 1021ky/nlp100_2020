# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
from argparse import ArgumentParser

parser = ArgumentParser("head", f"{__file__} 2 -f hoge.txt",
                        "指定されたファイルを先頭から指定された行数標準出力します。")
parser.add_argument("N", help="先頭から出力する行数", type=int)
parser.add_argument("-f", "--filename",
                    default="popular-names.txt", help="対象ファイル", type=str)
args = parser.parse_args()
num = args.N

with open(args.filename) as f:
    for _ in range(num):
        line = f.readline()
        print(line, end='')
