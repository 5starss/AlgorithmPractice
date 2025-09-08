'''
아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분집합을 모두 출력
-1, 3, -9, 6, 7, -6, 1, 5, 4, -2
'''

def subset(start, path):
    if start == N:
        if sum(path) == 0:
            print(path)
        return

    subset(start + 1, path)
    subset(start + 1, path + [arr[start]])


arr = list(map(int, input().split(',')))
N = len(arr)

subset(0, [])
