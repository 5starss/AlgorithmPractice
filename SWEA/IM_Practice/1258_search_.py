def mini_mat(arr, x ,y):
    len_x, len_y = 0, 0
    while x+len_x < N:
        if arr[x+len_x][y] == 0:
            break
        len_x += 1

    while y+len_y < N:
        if arr[x][y+len_y] == 0:
            break
        len_y += 1

    return len_x, len_y



# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    list_ = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                len_x, len_y = mini_mat(arr, i, j)

                list_.append((len_x, len_y))
                print(len_x, len_y)
                for k in range(len_x):
                    for l in range(len_y):
                        arr[i+k][j+l] = 0

    list_.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f"#{tc} {len(list_)}", end=' ')
    for i in range(len(list_)):
        print(list_[i][0], list_[i][1], end=' ')
    print()