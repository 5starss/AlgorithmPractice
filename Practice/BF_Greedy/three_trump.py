# A, K, Q, J가 넉넉히
# 카드 5장을 뽑았을 때, 같은 종류의 카드가 3장 연속으로 나오은 경우의 수

card = ['A', 'K', 'Q', 'J']
path = []
result = 0

# 같은 카드가 3개인가?
def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True

    return False

def recur(cnt):
    global result
    if cnt == 5:
        if count_three():
            result += 1
        return

    for idx in range(len(card)):
        path.append(card[idx])
        recur(cnt+1)
        path.pop()


recur(0)

print(result)
