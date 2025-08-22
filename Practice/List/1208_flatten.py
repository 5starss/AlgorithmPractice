def flatten(arr):  # 평탄화
    max_index, max_value = 0, arr[0]  # 최고점 높이와 위치
    min_index, min_value = 0, arr[0]  # 최저점 높이와 위치

    # for idx in range(100):  -> 인덱스로 접근 후 높이와 위치 갱신 가능.
    for i, v in enumerate(arr):
        if max_value < v:  # 최고점 높이와 위치 갱신
            max_index = i
            max_value = v

        elif min_value > v:  # 최저점 높이와 위치 갱신
            min_index = i
            min_value = v

    # 평탄화
    arr[min_index] += 1
    arr[max_index] -= 1


def max_min(arr):  # 최고점과 최저점의 높이 차
    min_ = arr[0]
    max_ = arr[0]
    for i in range(1, 100):
        if max_ < arr[i]:
            max_ = arr[i]  # 최고점 찾기
        if min_ > arr[i]:
            min_ = arr[i]  # 최저점 찾기
    return max_ - min_  # 높이 차


if __name__ == "__main__":
    import sys

    sys.stdin = open('input.txt')

    for i in range(1, 11):
        N = int(input())  # 덤프 횟수
        arr = list(map(int, input().split()))  # 각 상자의 높이 값

        for _ in range(N):
            flatten(arr)  # 평탄화

        ans = max_min(arr)  # 최고점과 최저점의 높이 차
        print(f"#{i} {ans}")
