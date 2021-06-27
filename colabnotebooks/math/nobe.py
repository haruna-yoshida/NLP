from sympy import solve, Symbol

a = float(2)#作業員の人数1
b = float(8)#作業員の人数2
s = float(3)#人数1で働いた日数1
t = float(15)#人数2で働いた日数2
A1 = float(96000)#人数1*日数1の給料

def main():
  sympy_function(a,b,s,t,A1)

def sympy_function(a,b,s,t,A1):
  x = Symbol('x')#人数2*日数2の給料
  equation1 = b*t/a*s - x/A1
  X = solve([equation1])
  print(X)

if __name__ == "__main__":
    main()