"""
5
AAA
ABBA
ABABA
ABCA
PALINDROME
"""

def recursion(s, l, r, cnt=1):
    if l >= r: return 1, cnt  # 대칭 확인
    elif s[l] != s[r]: return 0, cnt  # 다른 경우 대칭 아님
    else: return recursion(s, l+1, r-1,cnt+1) # 맨 앞을 한 칸 뒤로, 맨 뒤를 한 칸 앞으로

def isPalindrome(s):
    return recursion(s, 0, len(s)-1) # 맨 앞과 맨 뒤를 비교

n = int(input())
for _ in range(n):
    s = input()
    print(*(isPalindrome(s)))