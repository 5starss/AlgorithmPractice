# 앞에서부터 시작(BFS)
# a, b = map(int, input().split())
# queue = [(a,1)]
#
# while queue:
#     current, cnt = queue.pop(0)
#     cnt += 1
#     if current > b:
#         continue
#
#     if current * 2 == b or current * 10 + 1 == b:
#         print(cnt)
#         break
#     else:
#         queue.append((current * 2, cnt))
#         queue.append((current * 10 + 1, cnt))
# else:
#     print(-1)

# 뒤에서부터 시작
a, b = map(int, input().split())
cnt = 1
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print(-1)
        break

    cnt += 1

    if b == a:
        print(cnt)
        break

else:
    print(-1)