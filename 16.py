import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
@lru_cache(None)
def f(n):
    if n==0:
        return 0
    if n>0 and n%3==2:
        return f(n-1)+1
    if n>0 and n%3<2:
        return f((n-(n%3))/3)
for i in range(1, 2000):
    f(i)
for n in range(1, 2000):
    if f(n)==5:
        print(n)
        break