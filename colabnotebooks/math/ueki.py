#TODO yの計算式が思いつかない

from sympy import solve, Symbol

a = float(200)#土地の縦
b = float(300)#土地の横
s = float(10)#木の間隔1[m]
n = float(3)#看板の幅[m]
q = float(40)#看板の数

def main():
  sympy_function(a, b, s, n, q)

def sympy_function(a, b, s, n, q):
  x = Symbol('x')#木の数
  y = Symbol('y')#看板の間隔
  equation1 = ((a/s)-1)*2 + ((b/s)-1)*2 -x
  equation2 = y #今適当
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()
