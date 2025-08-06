import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 버스 노선
    bus_stops = [0] * 5001  # 버스 정류장 번호. 지나는 버스 노선 counting

    for _ in range(N):
        A, B = map(int, input().split())  # 버스 시작점, 도착점
        for i in range(A, B + 1):
            bus_stops[i] += 1  # 지나는 정류장 번호 counting

    P = int(input())

    print(f"#{tc}", end='')
    for _ in range(P):
        C = int(input())
        print(f" {bus_stops[C]}", end='')  # 각 버스 정류장을 지나는 버스 노선의 개수

    print()  # 테스트 케이스가 여러 개일 경우 필요함
