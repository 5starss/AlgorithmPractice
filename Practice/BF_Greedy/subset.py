arr = ["O", "X"]
path = []
name = ["MIN", "CO", "TIM"]

# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     for i in range(len(arr)):
#         path.append(arr[i])
#         recur(cnt+1)
#         path.pop()

def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return

    # 부분 집합에 포함 시키는 경우
    recur(cnt+1, subset + [name[cnt]])
    # 포함시키지 않는 경우
    recur(cnt+1, subset)


recur(0, [])
