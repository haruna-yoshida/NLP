from sympy import solve, Symbol

a1 = float(8)#配る枚数1
a2 = float(-18)#配る枚数1の時の余った枚数
b1 = float(5)#配る枚数2
b2 = float(45)#配る枚数2の時の余った枚数

def main():
    sympy_function(a1,a2,b1,b2)

def sympy_function(a1,a2,b1,b2):
  x = Symbol('x')#クラスの人数
  y = Symbol('y')#メダルの枚数
  equation1 = y - a1*x - a2
  equation2 = y- b1*x - b2
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()