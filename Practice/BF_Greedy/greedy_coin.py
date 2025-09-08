coin_list = [100, 500, 10, 100]
target = 1730
cnt = 0

coin_list.sort(reverse=True)

for coin in coin_list:
    possible_cnt = target // coin
    cnt += possible_cnt
    target -= coin * possible_cnt

print(cnt)