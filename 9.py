s=open('Задание 9.csv').readlines()
ans=0
for i in range(len(s)):
    s[i]=list(map(int, s[i].split(';')))
    s[i].sort()
    pvt=[int(x) for x in s[i] if s[i].count(x)>1]
    npvt = [int(x) for x in s[i] if s[i].count(x) == 1]
    if len(set(s[i]))==4:
        if (sum(npvt)/len(npvt))>sum(pvt):
            ans+=1
print(ans)

print(100/8)