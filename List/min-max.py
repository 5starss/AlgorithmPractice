import sys

sys.stdin = open('input.txt')

if __name__ == "__main__":
    for i in range(1, 11):
        N = int(input())
        arr = list(map(int, input().split()))

        sum_count = 0
        result_l = 0
        result_r = 0
        for idx in range(2, N-2):
            if arr[idx - 1] >= arr[idx - 2] and arr[idx] > arr[idx - 1]:
                result_l = arr[idx] - arr[idx - 1]
            elif arr[idx - 1] < arr[idx - 2] and arr[idx] > arr[idx - 2]:
                result_l =  arr[idx] - arr[idx - 2]

            if arr[idx + 1] >= arr[idx + 2] and arr[idx] > arr[idx + 1]:
                result_r = arr[idx] - arr[idx + 1]
            elif arr[idx + 1] < arr[idx + 2] and arr[idx] > arr[idx + 2]:
                result_r = arr[idx] - arr[idx + 2]

            if result_l > result_r:
                sum_count += result_r
            else:
                sum_count += result_l

        print(f"#{i} {sum_count}")

