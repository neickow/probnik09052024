s=9**12 + 3**8 - 3
ans=0
while s>0:
    if (s%3)==2:
        ans+=1
    s=s//3
print(ans)