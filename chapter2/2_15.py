# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
from argparse import ArgumentParser

parser = ArgumentParser("tail", f"{__file__} 2 -f hoge.txt",
                        "指定されたファイルを末尾から指定された行数標準出力します。")
parser.add_argument("N", help="末尾から出力する行数", type=int)
parser.add_argument("-f", "--filename",
                    default="popular-names.txt", help="対象ファイル", type=str)
args = parser.parse_args()
num = args.N

with open(args.filename) as f:
    lines = f.readlines()
    for l in lines[len(lines) - 2: len(lines)]:
        print(l, end="")
