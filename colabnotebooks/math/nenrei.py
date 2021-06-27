from sympy import solve, Symbol

a = float(65)#Aさんの年齢
b = float(29)#Bさんの年齢
c = float(4)#倍数1
d = float(1)#変数1

def main():
    sympy_function(a, b, c, d)

def sympy_function(a, b, c, d):
  x = Symbol('x')#◯年前
  equation1 = (a-x)-c*(b-x)
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()