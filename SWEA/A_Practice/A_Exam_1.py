'''
좌우 모두에 풍선이 남아 있는 경우
터트린 풍선의 왼쪽 풍선 값 × 오른쪽 풍선 값을 점수로 얻는다.

좌 혹은 우에만 풍선이 남아 있는 경우
남아 있는 이웃 풍선의 값을 점수로 얻는다.

풍선이 단 하나만 남아 있는 경우
그 풍선에 적힌 값을 점수로 얻는다.

풍선은 원하는 순서대로 터트릴 수 있다.
모든 풍선을 터트려서 얻을 수 있는 최대 점수를 구하라.
1
4
1 2 3 4
=> 20
     / 8 4 4 4

3 10 1 2 5
=> 100

   / 20 50 10 10 10

12 34 56 78 90
=> 10804
34 5040 3060 90 90
12 34 56 78 90
'''

def pang(sum_, arr, i):
    arr2 = arr[:]
    if len(arr2) == 1:  # arr가 하나만 남았을 경우 -> 자기 자신을 더함
        sum_ += arr2.pop(i)
    elif i == 0:  # arr가 2개 이상인데 맨 앞인경우 -> 이웃한 뒷쪽을 더함
        sum_ += arr2[1]
        arr2.pop(i)
    elif i == len(arr2)-1:  # arr가 2개 이상인데 맨 뒤인경우 -> 이웃한 앞쪽을 더함
        sum_ += arr2[len(arr2)-2]
        arr2.pop(i)
    else:  # arr가 맨 앞, 맨 뒤가 아닌경우 -> 이웃한 두 값의 곱을 더함
        sum_ += arr2[i-1] * arr2[i+1]
        arr2.pop(i)

    return sum_, arr2

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    ans = 0

    queue = [(ans, arr)]

    while queue:
        sum_, current_arr = queue.pop(0)

        ans = max(ans, sum_)

        for i in range(len(current_arr)):
            sum_2, arr_1 = pang(sum_, current_arr, i)
            queue.append((sum_2, arr_1))

    print(f"#{tc} {ans}")



