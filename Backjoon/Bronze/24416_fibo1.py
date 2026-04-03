""" 재귀형 순서 세는 법
def fibo_recur(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return fibo_recur(n-1) + fibo_recur(n-2)
"""

def fibo_dp(n):
    global cnt2
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-2] + f[i-1]
    return f[n]

# 피보나치 재귀형의 실행 횟수도 DP처럼 규칙성이 있음
def fibo_recur_cnt(n):
    f2[1], f2[2] = 1, 2
    for i in range(3, n + 1):  # 1, 2, 3, 5, 8, 13, ...
        f2[i] = f2[i - 2] + f2[i - 1]
    return

n = int(input())
cnt1, cnt2 = 0, 0
f = [0] * (n+1)
f2 = [0] * (n+1)
# fibo_recur(n)
fibo_dp(n)
fibo_recur_cnt(n)
cnt3 = f2[n-1]
print(cnt1, cnt2, cnt3)