from sympy import solve, Symbol

s = float(5)#たかしがかかる時間
t = float(7)#きよしがかかる時間
c = float(1)#たかし時間の変数
d = float(1)#2人時間の変数
e = float(4)#今回かかった時間

def main():
    sympy_function(s, t, c, d, e)

def sympy_function(s, t, c, d, e):
  k = Symbol('k')
  x = Symbol('x')#たかしが1人で仕事をした時間
  y = Symbol('y')#2人で仕事をした時間
  a = Symbol('a')#たかしの1日の仕事量(/日)
  b = Symbol('b')#きよしの1日の仕事量(/日)
  A1 = Symbol('A1')#全体の仕事量
  x=t*k
  
  equation1 = s*a - A1
  equation2 = t*b - A1
  equation3 = x*a + y*(a+b) - A1  
  equation4 = x*c + y*d - e
  X = solve([equation1, equation2, equation3, equation4], [x, y])
  print(X)

if __name__ == "__main__":
    main()


"""高校生が解くとしたら（小学生は違う解き方）
a=たかしが1日にする仕事量　b=きよしが1日にする仕事量　とする
5a=7b=全体の仕事量 
従ってb=5a/7
    ①a*x+(a+b)*y=全体の仕事量
    ②x+y=4
であるから、
①よりax+(a+5a/7)y=5a
②より、y=4-x
よって、
ax+(12a/7)(4-x)=5a
ax-(12a/7)x+(13a/7)=5a
(1/5)x-(12/35)x+(13/35)=1
x=