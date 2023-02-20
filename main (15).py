def F(n, d):
    if d == 1:
        return 1
    elif n % d == 0:
        return 0
    return F(n, d - 1)
        

n = int(input())
n = abs(n)
d = int(n ** 0.5)
if F(n, d):
    print('YES')
else:
    print('NO')