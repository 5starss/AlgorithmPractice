import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())
    # 다른 행성의 숫자 리스트
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in range(int(N)):
        arr[i] = num_list.index(arr[i])  # index 검색

    arr.sort()  # 정렬

    for i in range(int(N)):
        arr[i] = num_list[arr[i]]  # 외계 숫자 가져오기

    print(tc)
    print(' '.join(arr))
    #print(*arr) # 언패킹으로도 출력 가능

