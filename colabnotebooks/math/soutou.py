from sympy import solve, Symbol

a = float(1)#分子1
b = float(7)#分母2
c = float(1)#分子2
d = float(3)#分母2
s = float(44)#ページ数1

def main():
  sympy_function(a, b, c, d, s)

def sympy_function(a, b, c, d, s):
  x = Symbol('x')#全ページ数
  equation1 =x*(a/b) + s + x*(c/d) -x
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()
