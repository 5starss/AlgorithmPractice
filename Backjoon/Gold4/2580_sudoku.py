def square(x, y):
    return (x // 3) * 3 + (y // 3)

def sudoku(z):
    if z == 81: # 끝까지 확인
        for i in range(9):
            print(*mat[i])
        return True  # 완성되면 끝

    x = z // 9
    y = z % 9

    if mat[x][y] != 0:
        return sudoku(z+1)
    else:
        for i in range(1, 10):
            if not line_x[x][i] and not line_y[y][i] and not square_[square(x, y)][i]:
                line_x[x][i], line_y[y][i], square_[square(x, y)][i] = 1, 1, 1
                mat[x][y] = i
                if sudoku(z+1):  # 한번 완성 되면 종료
                    return True
                line_x[x][i], line_y[y][i], square_[square(x, y)][i] = 0, 0, 0
                mat[x][y] = 0

    return False


mat = [list(map(int, input().split())) for _ in range(9)]
line_x = [[0] * 10 for _ in range(10)]
line_y = [[0] * 10 for _ in range(10)]
square_ = [[0] * 10 for _ in range(10)]

for i in range(9):
    for j in range(9):
        if mat[i][j] != 0:
            line_x[i][mat[i][j]] = 1
            line_y[j][mat[i][j]] = 1
            square_[square(i, j)][mat[i][j]] = 1

sudoku(0)




