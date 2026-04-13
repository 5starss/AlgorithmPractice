def binary_mod(n, cnt, div):
    if cnt == 1:
        return n % div

    tmp = binary_mod(n, cnt//2, div)

    if cnt % 2 == 0:
        return tmp * tmp % div
    else:
        return (tmp * binary_mod(n, cnt-cnt//2, div) % div) % div

A, B, C = map(int, input().split())

print(binary_mod(A, B, C))