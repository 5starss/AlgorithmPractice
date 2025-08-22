import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    print(f"#{tc}", end=' ')

    for j in range(15):  # 행 검색
        for i in range(5):  # 열 검색
            if j < len(arr[i]):  # 행 길이보다 넘지 않게 검색
                print(arr[i][j], end='')   # 띄어쓰기 없이 출력
    print()

    # 리스트 컴프리헨션으로 한줄로 가능
    # print(''.join([arr[i][j] for j in range(15) for i in range(5) if j < len(arr[i])]))
