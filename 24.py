s=open('24.txt').readline()
s=s.replace('X','X ').replace('Y','Y ').split(' ')
s.sort(key=lambda x: len(x))
s=s[::-1]
print(s[0])
print(len(s[0]))