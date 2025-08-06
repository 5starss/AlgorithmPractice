T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 수열의 길이
    str_ = input()  # 수열

    cnt = 0  # 연속한 1의 개수
    max_cnt = 0  # 연속한 1의 개수의 최대값

    for char in str_:
        if int(char) == 0:  # 0인 경우 연속값 리셋
            cnt = 0
        else:  # 1인 경우 1추가
            cnt += 1

        if max_cnt < cnt:  # 최대값 갱신
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")
