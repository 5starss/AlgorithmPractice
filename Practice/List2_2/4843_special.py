def sort():  # idx가 짝수, 홀수 분기를 먼저하고 최대값 최소값 찾기
    for i in range(N-1):
        if i % 2 == 0:  # 짝수인 경우
            max_idx = i  # 자기자신으로 설정
            for j in range(i+1, N):  # 뒷부분 탐색
                if arr[max_idx] < arr[j]:  # 최대값 찾기
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]  # 최대값을 앞으로
        else:  # 홀수인 경우
            min_idx = i  # 자기 자신으로 설정
            for j in range(i + 1, N):  # 뒷부분 탐색
                if arr[min_idx] > arr[j]:  # 최소값 찾기
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최소값을 앞으로

def sort2():  # 일단 큰 수, 작은 수 찾고 idx가 짝수인지 홀수인지 확인
    for i in range(N-1):
        min_idx = i  # 자기 자신으로 설정
        max_idx = i
        for j in range(i+1, N):  # 최대, 최소 찾기
            if arr[max_idx] < arr[j]:
                max_idx = j
            elif arr[min_idx] > arr[j]:
                min_idx = j
        if i % 2 == 0:  # idx가 짝수인 경우
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:  # 홀수인 경우
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sort()

    sort2()

    print(f"#{tc} {' '.join(map(str, arr[:10]))}")  # 10개까지 출력
