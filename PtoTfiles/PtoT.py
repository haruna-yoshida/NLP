# こっちが大切！
import glob
import os
import sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# 現在の階層を確認
print('getcwd:', os.getcwd())

# filesに指定の階層のファイルを全て取得
files = glob.glob('**/*.pdf', recursive=True)

#filesの1つ1つに関して処理を行う．
for file in files:
  with open(file,mode='r') as f: #fileを開く
    print(file)
    
    # PDFPage.get_pages()にファイルオブジェクトを指定して、PDFPageオブジェクトを順に取得する。
    # 時間がかかるファイルは、キーワード引数pagenosで処理するページ番号（0始まり）のリストを指定するとよい。
    for page in PDFPage.get_pages(f):
        print_and_write('\n====== ページ区切り ======\n')
        interpreter.process_page(page)  # ページを処理する。
        layout = device.get_result()  # LTPageオブジェクトを取得。

        # ページ内のテキストボックスのリストを取得する。
        boxes = find_textboxes_recursively(layout)

        # テキストボックスの左上の座標の順でテキストボックスをソートする。
        # y1（Y座標の値）は上に行くほど大きくなるので、正負を反転させている。
        boxes.sort(key=lambda b: (-b.y1, b.x0))

        for box in boxes:
            print_and_write('-' * 10)  # 読みやすいよう区切り線を表示する。
            print_and_write(box.get_text().strip())  # テキストボックス内のテキストを表示する。
    # 行う処理 今回はシンプルに内容の表示
    print(f.read())