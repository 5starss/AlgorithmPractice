import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())), reverse=True)
dict_ = dict()

for i in arr:
    dict_[i] = dict_.setdefault(i, 0) + 1

sum_ = 0
keys = list(dict_.keys())
for i in range(1, len(keys)):
    pass


