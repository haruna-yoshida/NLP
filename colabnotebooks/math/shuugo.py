from sympy import solve, Symbol

a = float(42)#クラスの人数
b = float(28)#算数に合格した人数
c = float(25)#国語に合格した人数
d = float(17)#両方合格した人数

def main():
    sympy_function(a,b,c,d)

def sympy_function(a,b,c,d):
  x = Symbol('x')#両方不合格の人数
  equation1 = a-(b+c-d)-x
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()