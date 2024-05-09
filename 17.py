s=open('17.txt').readlines()
s=[int(x) for x in s]
ans=0
mxs=0
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        if (s[i]+s[j])%10==0:
            ans+=1
            mxs=max(mxs, s[i]+s[j])
print(ans, mxs)
