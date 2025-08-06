import sys

sys.stdin = open('input.txt')

T = int(input())

factors = [2, 3, 5, 7, 11]  # 인수 리스트

for tc in range(1, T+1):
    exp = []  # 지수 리스트
    N = int(input())
    for factor in factors:
        cnt = 0  # 지수
        while not N % factor:  # 나머지가 없는 경우 // 나머지가 있는 경우 -> 나누지 못함 -> 다음 인수로
            N //= factor
            cnt += 1
        exp.append(cnt)

    print(f"#{tc} {exp[0]} {exp[1]} {exp[2]} {exp[3]} {exp[4]}")