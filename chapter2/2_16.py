# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
from argparse import ArgumentParser

parser = ArgumentParser(
    "split", f"{__file__} 2 -f hoge.txt", "指定されたファイルを行単位でN分割する")
parser.add_argument("N", help="分割数", type=int)
parser.add_argument("-f", "--filename",
                    default="popular-names.txt", help="対象ファイル", type=str)
args = parser.parse_args()
num = args.N

with open(args.filename) as f:
    lines = f.readlines()
    unit_count = int(len(lines) / num)
    start = 0
    end = unit_count
    for i in range(num):
        fn = str(i+1) + args.filename
        with open(fn, mode='w') as fw:
            fw.write(''.join(lines[start:end]))
        start = end
        end += unit_count + 1
