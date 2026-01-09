def cantor(n):
    if not n:
        return '-'
    ans = '-' * 3**n


    return ans

n = int(input())
ans = ''
if not n:
    pass
print(cantor(n))