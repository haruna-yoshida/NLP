from sympy import solve, Symbol

a = float(142)#1辺の墓石の数

def main():
  sympy_function(a)

def sympy_function(a):
  x = Symbol('x')#すべての墓石の数
  y = Symbol('y')#まわりの墓石の数
  equation1 = x - a**2
  equation2 = (a-1)*4 -y
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()
