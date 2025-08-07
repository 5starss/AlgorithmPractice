import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    ans = 0  # 디폴트 0
    for i in range(1, 1 << N):  # 부분 집합은 2**n
        temp = []  # 임시 리스트
        for j in range(N):  # 부분 집합 찾기
            if i & (1 << j):  # 부분 집합 인덱스 확인
                temp.append(arr[j])  # 부분 집합 값 넣기

        if sum(temp) == 0:  # 부분집합 내 값의 합이 0인 경우 1, 아닌경우 그대로 0
            ans = 1

    print(f"#{tc} {ans}")

