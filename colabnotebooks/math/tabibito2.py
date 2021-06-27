#TODO 分数で表すようにする

from sympy import solve, Symbol

a = float(80)#春子の速さ1（m/m）
b = float(95)#義雄の速さ2(m/m)
c = float(1)#速さ1の変数
d = float(1)#速さ2の変数
A1 = float(12)#池の周りの距離(km)
s = float(1000)#距離変数（km→m）

def main():
    sympy_function(a, b, c, d, A1, s)

def sympy_function(a, b, c, d, A1, s):
  x = Symbol('x')#時間
  equation1 = (a+b) * x - A1*s
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()