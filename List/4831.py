def charge_num(arr):
    cnt = 0  # 충전 횟수
    pos = 0  # 전기 버스 위치. 출발지
    for i in range(len(arr) - 1):  # 충전기가 있는 위치까지 순회
        if pos + K > arr[i]:  # 충전기 너머로 갈 수 있는 경우
            if pos + K < arr[i + 1]:  # 하지만 그 다음 충전기까지는 못가는 경우. 그 다음 충전기까지 가는 경우는 continue
                cnt += 1
                pos = arr[i]
        elif pos + K == arr[i]:  # 충천기까지 갈 수 있는 경우
            cnt += 1
            pos = arr[i]
        else:  # 충전기까지 갈 수 없는 경우
            break
    else:
        if pos + K >= N:  # 마지막에 도착지까지 갈 수 있는 경우
            return cnt
        else:  # 도착지까지 갈 수 없는 경우
            return 0
    return 0  # 충전기까지 갈 수 없는 경우


if __name__ == "__main__":
    import sys

    sys.stdin = open('input.txt')

    T = int(input())
    for tc in range(1, T+1):
        K, N, M = map(int, input().split())  # K: 한 번 충전 후 이동 가능한 거리, N: 정류장 수, M: 충전기 설치 수
        arr = list(map(int, input().split()))  # 충전기가 설치된 정류장 리스트
        arr.append(N)  # 도착지 추가

        ans = charge_num(arr)
        print(f"#{tc} {ans}")