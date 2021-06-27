from sympy import solve, Symbol

a = float(40)#りんごの原価
b = float(70)#りんごの定価
c = float(1)#りんごの値下げ割合(◯割引)
d = float(0.1)#割合変数1（1割→0.1）
e = float(0.01)#割合変数2（1厘→0.01）
s = float(100)#仕入れた個数
A1 = float(2545)#もうけ

def main():
  sympy_function(a, b, c, d, e, s, A1)

def sympy_function(a, b, c, d, e, s, A1):
  x = Symbol('x')#定価で売れた個数
  y = Symbol('y')#割引値で売れた個数
  equation1 = b*x + b*(1-c*d)*y - a*s - A1
  equation2 = x + y - s
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()
