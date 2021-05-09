import MeCab
import glob
import collections
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# filesに指定の階層のファイルを全て取得
files = glob.glob('**/*.pdf.txt', recursive=True)

for file in files:

    #問題の取り込み
    f = open(file)
    text = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()

    print(mpl.rcParams['font.family'])

    #MeCabで分割
    m = MeCab.Tagger ('-Ochasen')
    
    node = m.parseToNode(text)
    words=[]
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in ["動詞"]:
            origin = node.feature.split(",")[6]
            words.append(origin)
        node = node.next

    #単語の数カウント
    c = collections.Counter(words)
    print(c.most_common(20))

    #グラフ化
    sns.set(context="talk")
    sns.set(font='Hiragino sans')
    fig = plt.subplots(figsize=(8, 8))
    
    sns.countplot(y=words,order=[i[0] for i in c.most_common(20)])

    line_plot = sns.lineplot()
    figure = line_plot.get_figure()
    figure.savefig(file + '.png')

    print(words)
    plt.show()

