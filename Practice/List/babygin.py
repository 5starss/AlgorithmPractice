def baby_gin(num):
    # 카드 개수 저장하는 리스트, 순회할 때 idx+2까지 확인할 것이므로 12까지
    arr = [0] * 12

    for _ in range(6):  # 카드 개수 세기
        arr[num % 10] += 1
        num //= 10

    count = 0  # triplet이나 run으로 구성된 횟수

    i = 0  # 카드 개수 리스트 순회할 idx
    while i < 10:  # 카드는 0~9
        if arr[i] == 3:  # triplet
            count += 1
        elif arr[i] == 6:  # triplet이 두번
            count += 2
            break
        elif arr[i] == 1 and arr[i + 1] == 1 and arr[i + 2] == 1:  # run
            count += 1
            i += 2  # 확인한 부분 뒤로
        elif arr[i] == 2 and arr[i + 1] == 2 and arr[i + 2] == 2:  # run이 두번
            count += 2
            break
        i += 1

    if count == 2:  # baby-gin
        return 1
    else:
        return 0


if __name__ == "__main__":
    # import sys
    #
    # sys.stdin = open('input.txt')

    T = int(input())
    for i in range(1, T + 1):
        cards = int(input())
        ans = baby_gin(cards)
        print(f"#{i} {ans}")
