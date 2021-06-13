from sympy import solve, Symbol, Function

a = float(300)#もとの食塩水の体積
b = float(200)#加えた食塩水の体積
c = float(13)#加えた食塩水の濃度
d = float(8.8)#できた食塩水の濃度

def main():
    sympy_function(a, b, c, d)

def sympy_function(a, b, c, d):
    x = Symbol('x')#もとの食塩水の濃度
    ans = solve(a*x + b*c - (a+b)*d, x)
    print(ans)

if __name__ == "__main__":
    main()