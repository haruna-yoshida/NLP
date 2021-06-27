from sympy import solve, Symbol

A1 = float(284)#合計
s = float(21)#人物B-人物A
t = float(5)#人物C-人物A
a = float(1)#変数1
b = float(1)#変数2
c = float(1)#変数3

def main():
  sympy_function(A1, a, b, c, s, t)

def sympy_function(A1,a, b, c, s, t):
  x = Symbol('x')#人物1のもらった数
  y = Symbol('y')#人物2のもらった数
  z = Symbol('z')#人物3のもらった数
  equation1 = a * x + b * y + c * z - A1
  equation2 = y - x - s
  equation3 = z - x - t
  X = solve([equation1, equation2, equation3])
  print(X)

if __name__ == "__main__":
    main()
