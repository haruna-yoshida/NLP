from sympy import solve, Symbol
 
a = float(250)#りんごの値段
b = float(120)#みかんの値段
c = float(1)#りんご一つ
d = float(1)#みかん一つ
A1 = float(2970)#合計金額
A2 = float(15)#合計個数

def main():
    sympy_function(a, b, c, d, A1, A2)

def sympy_function(a, b, c, d, A1, A2):
  x = Symbol('x')#りんごの個数
  y = Symbol('y')#みかんの個数
  determinant = a * d - b * c
  if determinant != 0:
    equation1 = a * x + b * y - A1
    equation2 = c * x + d * y - A2
    X = solve([equation1, equation2])
    print(X)
  else:
     if c/a == A1 / A2:
      print('解が複数存在します')

     else:
      print('解が存在しません')

if __name__ == "__main__":
    main()