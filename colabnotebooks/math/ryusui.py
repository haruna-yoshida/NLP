from sympy import solve, Symbol

a = float(30)#船の速さ[km/h]
A1 = float(8)#進んだ距離[km]
m = float(12)#かかった時間[分]
k = float(1/60)#時間変数(分→時間)

def main():
  sympy_function(a, A1, m, k)

def sympy_function(a, A1, m, k):
  x = Symbol('x')#川の流れの速さ[km/h]
  equation1 = A1 - (a+x)*m*k
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()
