from sympy import solve, Symbol

a = float(8)#一分で新しく並ぶ人数
s = float(2)#入場口の数1
t = float(3)#入場口の数2
m = float(30)#入場口二つの時かかった時間
A1 = float(240)#元から並んでいた人数

def main():
    sympy_function(a, s, t, m, A1)

def sympy_function(a, s, t, m, A1):
  x = Symbol('x')#入場口一つで一分で入る人数
  n = Symbol('n')#入場口三つでかかる時間
  equation1 = (A1+a*m)-s*x*m
  equation2 = (A1+a*n)-t*x*n
  X = solve([equation1, equation2])
  print(X[0][n])

if __name__ == "__main__":
    main()