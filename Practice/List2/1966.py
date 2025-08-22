def bubble_sort1(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort2(arr, N):
    for i in range(N-1):
        for j in range(i, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def counting_sort(arr, N):
    count = [0] * (max(arr) + 1)  # 정렬 해야 될 리스트 속 최대값까지 저장하기 위함.
    temp = [0] * N

    for i in range(N):  # 카운팅
        count[arr[i]] += 1

    for i in range(1, len(count)):  # 누적 합
        count[i] += count[i - 1]

    for i in range(N - 1, -1, -1):
        count[arr[i]] -= 1
        temp[count[arr[i]]] = arr[i]

    return temp


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt', 'r')

    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())

        arr = list(map(int, input().split()))

        # 버블 정렬 두가지
        arr = bubble_sort1(arr, N)
        arr = bubble_sort2(arr, N)

        # 리스트 메서드 sort() 사용
        arr.sort()

        # 내장함수 sorted() 사용
        arr = sorted(arr)

        # 카운팅 정렬 사용
        arr = counting_sort(arr, N)

        print(f"#{tc} {' '.join(map(str, arr))}")  # str로 변환 후 한 칸씩 띄어쓰기
