# TODO 24行目()の中身をnounAndVerbにする

import MeCab
import csv
import pprint
import sys
import wikipedia

# 言語を日本語に設定
wikipedia.set_lang("jp")
# テキストファイルを開く
f = open('wikipedia.txt', 'a')

args = sys.argv
word = args[1]
# 検索ワードを用いて検索
words = wikipedia.search(word)

if not words:
    print("一致なし")
else:
    #検索ワードがヒットすれば要約を取得
    line = str(wikipedia.summary(words[0]))
    f.write(word)
    f.write(line.rstrip())
    print("success!")

f.write("\n" + "EOS" + "\n")
f.close()

mecab = MeCab.Tagger ()
text = line.rstrip()
result = mecab.parse(text)
lines = result.split('\n')
nounAndVerb = []#「名詞」と「動詞」を格納するリスト
for line in lines:
    print (line)
    if ('記号') in line:
        continue
    feature = line.split('\t')
    if len(feature) == 2: #'EOS'と''を省く
        info = feature[1].split(',')
        hinshi = info[1]
        if hinshi in ('一般') and info[6] != "*":
            nounAndVerb.append(info[6])
print(nounAndVerb)

with open('data/temp/sample_writer_row.csv', 'x') as f:
    writer = csv.writer(f)
    #()の中身をnounAndVerbにする↓
    writer.writerow([0, 1, 2])
    writer.writerow(['a', 'b', 'c'])