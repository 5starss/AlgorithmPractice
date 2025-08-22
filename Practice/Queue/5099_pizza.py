import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))  # 녹지 않은 치즈의 양

    # # 원형큐를 통해 인덱스 제어
    # q = []  # 화덕
    #
    # for i in range(N):  # 화덕 채우기
    #     q.append([i+1, arr[i]])  # [피자번호, 치즈 양]
    #
    # arr_pointer = N  # 다음 피자를 가리킴
    #
    # pointer = 0  # 화덕의 내부를 가리키는 포인터
    # ans = 0  # 마지막에 0이 되는 피자의 번호
    # pizza_cnt = 0  # 완성된 피자의 개수
    #
    # while pizza_cnt < M:  # 다 완성되기 전까지 반복
    #     if q[pointer][1] != 0:  # 치즈가 다 안녹은 경우
    #         q[pointer][1] //= 2  # 안녹은 치즈 반으로 줄이기
    #
    #         if q[pointer][1] == 0:  # 만약 해당 피자의 치즈가 0이라면
    #             pizza_cnt += 1  # 완성된 피자 증가
    #             ans = q[pointer][0]  # 완성된 피자 번호
    #
    #             if arr_pointer < M:  # 남은 피자가 있다면
    #                 q[pointer] = [arr_pointer + 1, arr[arr_pointer]]  # 화덕에 넣어줌
    #                 arr_pointer += 1  # 다음 피자를 가리키도록 함
    #
    #     pointer = (pointer + 1) % N  # 화덕 내부 가리키는 포인터 증가, 원형 큐
    #
    # print(f"#{tc} {ans}")

    # 원형큐를 통해 인덱스 제어, 화덕은 인덱스만 제어
    q = list(range(N))  # 화덕

    arr_pointer = N  # 다음 피자를 가리킴

    pointer = 0  # 화덕의 내부를 가리키는 포인터
    ans = 0  # 마지막에 0이 되는 피자의 번호
    pizza_cnt = 0  # 완성된 피자의 개수

    while pizza_cnt < M-1:  # 다 완성되기 전까지 반복
        if arr[q[pointer]] != 0:  # 치즈가 다 안녹은 경우
            arr[q[pointer]] //= 2  # 안녹은 치즈 반으로 줄이기

            if arr[q[pointer]] == 0:  # 만약 해당 피자의 치즈가 0이라면
                pizza_cnt += 1  # 완성된 피자 증가
                # ans = q[pointer]  # 완성된 피자 번호

                if arr_pointer < M:  # 남은 피자가 있다면
                    q[pointer] = arr_pointer  # 화덕에 넣어줌
                    arr_pointer += 1  # 다음 피자를 가리키도록 함

        pointer = (pointer + 1) % N  # 화덕 내부 가리키는 포인터 증가, 원형 큐

    print(f"#{tc} {ans+1}")

    # # deque 사용(치즈의 양을 큐에서 컨트롤)
    # q = deque()  # 화덕
    #
    # for i in range(N):  # 화덕 채우기
    #     q.append([i+1, arr[i]])  # [피자번호, 치즈 양]
    #
    # next_pizza = N  # 다음 피자 번호
    #
    # while len(q) > 1:  # 화덕에 피자가 하나 남을 때 까지
    #     num, cheese = q.popleft()  # 화덕에서 피자 꺼내서 확인
    #
    #     cheese //= 2  # 치즈 반으로 줄이기
    #
    #     if cheese != 0:  # 치즈가 0이 아니라면 다시 화덕으로
    #         q.append([num, cheese])
    #     elif next_pizza < M:  # 치즈가 0이고 남은 피자가 있다면 화덕에 넣어줌
    #         q.append([next_pizza + 1, arr[next_pizza]])
    #         next_pizza += 1
    #
    # ans = q[0][0]  # 마지막에 남은 피자의 번호
    #
    # print(f"#{tc} {ans}")
    #
    # # deque 사용(치즈의 양이 적힌 배열 그 자체에서 컨트롤)
    # q = deque(range(N))  # 큐에 치즈 양이 적힌 리스트의 idx를 넣음
    #
    # next_pizza = N  # 다음 피자 번호
    #
    # while len(q) > 1:  # 화덕에 피자가 하나 남을 때 까지
    #     num = q.popleft()  # 화덕에서 피자 꺼내서 확인
    #
    #     arr[num] //= 2  # 치즈 반으로 줄이기. 배열 자체에서 컨트롤
    #
    #     if arr[num] != 0:  # 치즈가 0이 아니라면 다시 화덕으로
    #         q.append(num)
    #     elif next_pizza < M:  # 치즈가 0이고 남은 피자가 있다면 화덕에 넣어줌
    #         q.append(next_pizza + 1)
    #         next_pizza += 1
    #
    # ans = q[0] + 1  # 마지막에 남은 피자의 번호 = idx+1
    #
    # print(f"#{tc} {ans}")
