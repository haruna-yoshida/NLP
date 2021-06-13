from sympy import solve, Symbol, Function

a = float(500)#全体人数
b = float(125)#合格者人数
c = float(84)#合格者平均
d = float(69)#全体平均

def main():
  sympy_function(a, b, c, d)

def sympy_function(a, b, c, d):
    x = Symbol('x')#不合格者平均
    ans = solve(a*d-b*c-(a-b)*x, x)
    print(ans)

if __name__ == "__main__":
    main()