def is_palindrome(arr):  # 회문인지 확인
    str_ = ''.join(arr)
    if str_ == str_[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    import sys

    sys.stdin = open('input.txt', 'r')

    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        str_list = [list(input()) for _ in range(N)]

        ans = ''
        # 행 검색
        for i in range(N):
            for j in range(N-M+1):
                if is_palindrome(str_list[i][j:j+M]):  # 원하는 범위까지 확인
                    ans = ''.join(str_list[i][j:j+M])
        
        # 열 검색
        str_list2 = list(zip(*str_list))  # zip을 이용해 같은index(열)끼리 묶을 수 있다.
        for i in range(N):
            for j in range(N-M+1):
                if is_palindrome(str_list2[i][j:j+M]):  # 원하는 범위까지 확인
                    ans = ''.join(str_list2[i][j:j+M])

        print(f"#{tc} {ans}")


