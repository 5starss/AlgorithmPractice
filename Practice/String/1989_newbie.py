import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = str1[::-1]  # 거꾸로
    if str1 == str2:  # 같다면 회문
        ans = 1
    else:
        ans = 0

    print(f"#{tc} {ans}")
