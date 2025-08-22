def magnet():
    for i in range(100):  # 좌표 전체 화인
        for j in range(100):
            if arr[i][j] == 1:  # 1인경우 N극. S극이 있는 밑으로 이동
                if i + 1 < 100 and arr[i+1][j] == 0:  # 아래가 행렬 밖이 아니고 값이 없을 경우
                    arr[i+1][j], arr[i][j] = arr[i][j], 0  # 아래로 이동
            elif arr[i][j] == 2:  # 2인경우 S극. N극이 있는 위로 이동
                if i - 1 >= 0 and arr[i-1][j] == 0:  # 위에가 행렬 밖이 아니고 값이 없을 경우
                    arr[i-1][j], arr[i][j] = arr[i][j], 0  # 위로 이동

def agglutination():  # 교착 확인
    cnt = 0
    for i in range(100):  # 좌표 전체 확인
        for j in range(100):
            if i+1 < 100 and arr[i][j] == 1:  # N극을 발견하면
                if arr[i][j] != arr[i+1][j]:  # 바로 아래 확인. 전부 붙어있을테니 아래만 확인하면 됨. 만약 다를경우
                    cnt += 1  # 교착상태. 개수 추가
                    arr[i][j], arr[i+1][j] = 0, 0  # 추가 검색 방지
                else:  # N극 밑에 N극이 있는 경우
                    for k in range(2, 50):  # 계속해서 밑을 확인
                        if i+k < 100 and arr[i+k][j] == 2:  # 쌓여있는 곳 맨 밑에가 S극인 경우
                            cnt += 1  # 쌓여있어도 1개로 취급
                            for l in range(k):  # 교착되어 있는 것 전부 지우기
                                arr[i+l][j] = 0
                            break  # 밑에 확인하는 로직 끝내기
    return cnt


import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(100):  # 한틱당 한칸씩 이동
        magnet()

    print(f"#{tc} {agglutination()}")