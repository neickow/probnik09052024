def f(a, b):
    if a==b:
        return True
    if a>b:
        return False
    if a<b:
        return f(a+1, b)+f(a*3, b)+f(a+2, b)
print(f(1, 10)*f(10, 12)*f(12, 15))