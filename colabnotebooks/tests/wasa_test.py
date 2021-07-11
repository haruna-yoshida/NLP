import Mecab
import glob
from sympy import solve, Symbol

# filesに指定の階層のファイルを全て取得
files = glob.glob('**/*.pdf.txt', recursive=True)



a = float(1)#人物1の倍数
b = float(1)#人物2の倍数
c = float(1)#人物1の変数
d = float(1)#人物2の変数
A1 = float(2400)#和
A2 = float(400)#差

def main():
  sympy_function(a, b, c, d, A1, A2)

def sympy_function(a, b, c, d, A1, A2):
  x = Symbol('x')#人物1のお小遣い
  y = Symbol('y')#人物2のお小遣い
  equation1 = a * x + b * y - A1
  equation2 = c * x - d * y - A2
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()
