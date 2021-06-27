from sympy import solve, Symbol

a = float(85)#電車の速さ[km/h]
a1 = float(10/36)#速さ変数1(km/h→m/s)
s = float(100)#電車の長さ[m]
m = float(52)#かかった時間(秒)
p = float(1)#距離変数1(電車が完全に入るor一部が出てくる問題の時)
q = float(2)#距離変数2(電車が入ってから完全に出てくる問題の時)

def main():
  sympy_function(a, a1, s, m)

def sympy_function(a, a1, s, m):
  x = Symbol('x')#トンネルの長さ
  equation1 = (a*a1)*m - q*s - x
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()
