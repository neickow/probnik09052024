print('19 задание')
def f(a, p):
    if a>=39 and p==3:
        return True
    if a>=39 and p==2:
        return False
    if a<39 and p==3:
        return False
    if p%2==1:
        return f(a+1, p+1) or f(a*3, p+1)
    if p%2==0:
        return f(a+1, p+1) or f(a*3, p+1)
for s in range(1, 39):
    if f(s, 1):
        print(s)
print('20 задание')
def f(a, p):
    if a>=39 and p==4:
        return True
    if a>=39 and p==3:
        return False
    if a<39 and p==4:
        return False
    if p%2==1:
        return f(a+1, p+1) or f(a*3, p+1)
    if p%2==0:
        return f(a+1, p+1) and f(a*3, p+1)
for s in range(1, 39):
    if f(s, 1):
        print(s)
print('21 задание')
def f(a, p):
    if a>=39 and p in (3, 5):
        return True
    if a>=39 and p in (2, 4):
        return False
    if a<39 and p==5:
        return False
    if p%2==0:
        return f(a+1, p+1) or f(a*3, p+1)
    if p%2==1:
        return f(a+1, p+1) and f(a*3, p+1)
for s in range(1, 39):
    if f(s, 1):
        print(s)