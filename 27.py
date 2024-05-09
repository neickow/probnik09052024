a = open('27-A.txt').readlines()
a = [int(x) for x in a]
N = a.pop(0)
sm = 0
b = [[0 for i in range(9)] for j in range(9)]
for i in range(N):
    for j in range(9):
        ind = (i - a[i] - j) % 9
        sm += b[j][ind]
    b[i % 9][a[i] % 9] += 1
print(sm % 10 ** 6)