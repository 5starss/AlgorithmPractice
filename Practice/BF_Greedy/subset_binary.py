arr = [1, 2, 3, 4]

# for i in range(1 << len(arr)):  # 부분 집합은 2**n  i번째 부분집합  0000, 0001, 0010, 0011, ...
#     for idx in range(len(arr)):  # 부분 집합 찾기
#         if i & (1 << idx):  # 부분 집합 인덱스 확인
#             print(arr[idx], end=' ')
#     print()


def subset(tar):
    for i in range(len(arr)):  # 부분 집합 찾기
        if tar & 0x1:  # 0x1 -> 비트 연산임을 강조
            print(arr[i], end=' ')
        tar >>= 1
    print()


for i in range(1 << len(arr)):
    subset(i)

