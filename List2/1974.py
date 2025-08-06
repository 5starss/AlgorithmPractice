def sudoku1(arr):
    sorted_arr = [i for i in range(1, 10)]

    # 행 검사
    for r in arr:
        if sorted(r) != sorted_arr:  # 정렬되었을 때 1 ~ 9가 다 있지 않은 경우
            return 0

    # 열 검사
    for c in zip(*arr):  # zip은 같은index(열)끼리 묶은 tuple을 return
        if sorted(c) != sorted_arr:
            return 0

    # 3 x 3 검사
    for r in range(0, 9, 3):  # 0, 3, 6
        for c in range(0, 9, 3):
            count = [0] * 10
            for i in range(3):  # 3 x 3 순회
                for j in range(3):
                    count[puzzle[r + i][c + j]] += 1
            if 2 in count:
                return 0
    return 1

def sudoku(arr):
    # 행 검사
    for r in range(9):
        count = [0] * 10  # 1 ~ 9를 인덱스로 검사하기 때문에 10개 생성
        for c in range(9):
            count[puzzle[r][c]] += 1  # 숫자 카운트
        if 2 in count:  # 같은 숫자가 두번 들어간 경우
            return 0

    # 열 검사
    for c in range(9):
        count = [0] * 10
        for r in range(9):
            count[puzzle[r][c]] += 1
        if 2 in count:
            return 0

    # 3 x 3 검사
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            count = [0] * 10
            for i in range(3):
                for j in range(3):
                    count[puzzle[r+i][c+j]] += 1
            if 2 in count:
                return 0
    return 1


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt', 'r')

    T = int(input())
    for tc in range(1, T + 1):
        puzzle = [list(map(int, input().split())) for _ in range(9)]

        print(f"#{tc} {sudoku1(puzzle)}")


