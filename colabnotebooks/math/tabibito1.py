#TODO xは時間なので、速さ＊時間を答えとして出したい

from sympy import solve, Symbol

a = float(5)#太郎の速さ1（km/h）
b = float(10)#太郎の速さ2(km/h)
c = float(1)#速さ1の変数
d = float(1)#速さ2の変数
A1 = float(3.5)#太郎が進んだ合計距離(km)
B1 = float(30)#太郎が進んだ時間(分)

def main():
    sympy_function(a, b, c, d, A1, B1)

def sympy_function(a, b, c, d, A1, B1):
  x = Symbol('x')#速さ1で進んだ時間
  y = Symbol('y')#速さ2で進んだ時間
  determinant = a * d - b * c
  if determinant != 0:
    equation1 = a * x + b * y - A1
    equation2 = c * x + d * y - B1 / 60
    X = solve([equation1, equation2])
    Y = X[x] * a #速さ1で進んだ距離を出したい
    print(Y)

if __name__ == "__main__":
    main()