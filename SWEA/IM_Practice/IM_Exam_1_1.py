import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K_max, K_min = map(int, input().split())
    scores = sorted(list(map(int, input().split())))

    # 최대 인원, 최소 인원 반 차이의 최소
    min_ = N

    # T1, T2 뽑을 점수 리스트
    # set는 무작위므로 sorted(list())를 통해 정렬
    # ex) [1, 2, 3, 5]
    score_lst = sorted(list(set(scores)))

    for i in range(len(score_lst) - 1):
        for j in range(i + 1, len(score_lst)):
            # C, B, A 순
            # t2는 C|B 칸막이, t1은 B|A 칸막이
            t2 = score_lst[i]
            t1 = score_lst[j]

            # 해당 T1, T2 사용해서 반 나누기
            # 각 반의 인원수
            A, B, C = 0, 0, 0

            # A >= T1,
            # T1 > B >= T2
            # T2 > C 로 반을 나눌 수 있다.
            for k in range(N):
                if scores[k] == t2:
                    # 만약 인덱스가 3이라면 앞에 3명이 C반
                    C = k
                    break

            for k in range(N):
                if scores[k] == t1:
                    # 만약 인덱스가 5라면 C반 3명을 뺀 2명이 B반
                    B = k - C
                    break

            # 나머지 A반
            A = N - B - C

            # 각 반이 최대 최소 인원 안에 있는지 확인
            if K_min <= A <= K_max and K_min <= B <= K_max and K_min <= C <= K_max:
                # 최대 최소반 인원 차이가 최소인지 확인
                min_ = min(min_, (max([A, B, C]) - min([A, B, C])))

    # 최소값 갱신이 없었다면 -1
    if min_ == N:
        result = -1

    print(f'#{tc} {min_}')
