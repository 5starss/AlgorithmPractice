import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    str_ = input()
    str_list = list(str_)

    # 버블정렬하듯이 -> list로 변환 필요
    for i in range(len(str_list)//2):
        str_list[i] , str_list[-(i+1)] = str_list[-(i+1)],  str_list[i]
    str_1 = ''.join(str_)

    # 새로운 문자열 생성 후 계속 갱신
    str_2 = ''
    for i in str_:
        str_2 = i + str_2

    # 슬라이싱
    str_3 = str_[::-1]

    # str 메서드 사용
    str_4 = ''.join(list(reversed(str_)))

    print(f"#{tc} {str_4}")
