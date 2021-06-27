from sympy import solve, Symbol

a = float(5)#比1の左辺
b = float(4)#比1の右辺
c = float(7)#比2の左辺
d = float(11)#比2の右辺
s = float(150)#渡した金額1

def main():
  sympy_function(a, b, c, d, s)

def sympy_function(a, b, c, d, s):
  x = Symbol('x')#人物1のもとの所持金
  y = Symbol('y')#人物2のもとの所持金
  p = Symbol('p')#人物1の今の所持金
  q = Symbol('q')#人物2の今の所持金
  equation1 = b*x - a*y
  equation2 = x-s-p
  equation3 = y+s-q 
  equation4 = d*p - c*q
  X = solve([equation1, equation2, equation3, equation4])
  print(X)

if __name__ == "__main__":
    main()
