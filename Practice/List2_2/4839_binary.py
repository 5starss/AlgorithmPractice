def binary_search1(l, r, key, step=1):  # 재귀 함수 사용
    if l > r:  # 찾지 못한 경우
        return step
    else:
        middle = (l + r) // 2  # 중앙값 설정
        if key == middle:  # 원하는 값이 중앙값에 있을 경우
            return step  # 찾은 횟수 리턴
        elif key < middle:  # 원하는 값이 중앙값보다 작을 경우
            return binary_search1(l, middle, key, step + 1)  # 중앙값 밑으로 다시 탐색
        elif key > middle:  # 원하는 값이 중앙값보다 클 경우
            return binary_search1(middle, r, key, step + 1)  # 중앙값 위로 다시 탐색

def binary_search2(l, r, key, step=1):  # 재귀 함수 미사용
    while l <= r:  # 찾지 못한 경우
        middle = (l + r) // 2  # 중앙값 설정
        if key == middle:  # 원하는 값이 중앙값인 경우
            return step
        elif key < middle:  # 원하는 값이 중앙값보다 작은 경우
            r = middle  # 중앙값 이상 탐색
            step += 1
        elif key > middle:
            l = middle  # 중앙값 이하 탐색
            step += 1

    return step  # 찾은 횟수 리턴


if __name__ == "__main__":
    import sys

    sys.stdin = open('input.txt', 'r')

    T = int(input())
    for tc in range(1, T + 1):
        P, A, B = map(int, input().split())
        l, r = 1, P
        cnt_A = binary_search1(l, r, A)
        cnt_B = binary_search1(l, r, B)

        # cnt_A = binary_search2(l, r, A)
        # cnt_B = binary_search2(l, r, B)

        winner = ''
        if cnt_A < cnt_B:  # A가 더 빨리 찾은 경우
            winner = 'A'
        elif cnt_A > cnt_B:  # B가 더 빨리 찾은 경우
            winner = 'B'
        else:  # 비긴 경우
            winner = 0

        print(f"#{tc} {winner}")
