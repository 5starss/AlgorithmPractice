arr = []
ans = []
for _ in range(9):
    arr.append(int(input()))

for i in range(1, 1 << 9):
    tmp = []
    for j in range(9):
        if i & (1 << j):
            tmp.append(arr[j])
    #print(tmp)
    if sum(tmp) == 100 and len(tmp) == 7:
        ans = tmp

for i in sorted(ans):
    print(i)