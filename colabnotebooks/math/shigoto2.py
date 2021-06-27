from sympy import solve, Symbol

s = float(5)#たかしがひとりでかかる日数
t = float(7)#きよしがひとりでかかる日数
c = float(1)#変数1
d = float(1)#変数2

def main():
  sympy_function(s, t, c, d)

def sympy_function(s, t, c, d):
  x = Symbol('x')#ふたりでかかる日数
  k = Symbol('k')#仕事定数
  A1 = Symbol('A1')#全部の仕事量
  equation1 = t*k*s - A1
  equation2 = s*k*t - A1
  equation3 = (t+s)*k*x - A1  
  X = solve([equation1, equation2, equation3])
  print(X[-1][x])#最後の項のxの値

if __name__ == "__main__":
    main()
