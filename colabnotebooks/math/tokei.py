#TODO 分数の形で答えるようにする（帯分数）

from sympy import solve, Symbol

a = float(4)#短針1
b = float(15)#長針1
m = float(0.5)#短針が一分に進む角度
n = float(6)#長針が一分に進む角度
s = float(360)#角度1
t = float(90)#角度2

def main():
  sympy_function(a, b, m, n, s, t)

def sympy_function(a, b, m, n, s, t):
  x = Symbol('x')#重なる時間が◯分後
  y = Symbol('y')#90度になる時間が◯分後
  equation1 = s - (n-m)*x
  equation2 = (s + t) - (n-m)*y
  X = solve([equation1, equation2])
  print(X[x],X[y]-X[x])

if __name__ == "__main__":
    main()
