from sympy import solve, Symbol

a = float(1)#人数1の時の大人の人数
b = float(2)#人数1の時の子供の人数
c = float(2)#人数2の時の大人の人数
d = float(10)#人数2の時の子供の人数
A1 = float(1850)#人数1の時の料金
A2 = float(8500)#人数2の時の料金

def main():
    sympy_function(a,b,c,d,A1,A2)

def sympy_function(a,b,c,d,A1,A2):
  x = Symbol('x')#大人の入場料
  y = Symbol('y')#子供の入場料
  equation1 = (x*a+y*b)-A1
  equation2 = (x*c+y*d)-A2
  X = solve([equation1, equation2])
  print(X)

if __name__ == "__main__":
    main()