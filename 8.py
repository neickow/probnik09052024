import itertools
ans=0
alf=itertools.product('ЖИРАФ', repeat=4)
for x in alf:
    s=''.join(x)
    if s.count('Р')==1:
        ans+=1
print(ans)
