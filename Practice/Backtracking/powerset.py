def powerset(subset, idx):
    if sum(subset) == 10:
        print(*subset)
        return
    elif sum(subset) > 10 or idx == 10:
        return

    powerset(subset+[arr[idx]], idx+1)
    powerset(subset, idx + 1)

"""
1 2 3 4 5 6 7 8 9 10
"""
arr = list(map(int, input().split()))

powerset([], 0)
