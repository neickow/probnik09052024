from fnmatch import fnmatch
# 12345?7?8
for i in range(123450729, 10**9, 23):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i//23)
