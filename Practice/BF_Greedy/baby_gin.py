'''
- 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
  3장의 카드가 동일한 번호를 갖는 경우를 triplet이라 한다.
- 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
- 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하라.


[입력 예]
- 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
- 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin이다.(456, 000)
- 101123은 한 개의 triplet이 존재하나, 023이 run이 아니므로 baby-gin이 아니다.
  (123을 run으로 사용하더라도  011이 run이나 triplet이 아님)
'''
def baby_gin(arr):
    arr.sort()
    if len(set(arr)) == 1:
        return True

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        return True

    return False

def recur(cnt, permutations):
    global ans
    if cnt == 6:
        if baby_gin(permutations[:3]) and baby_gin(permutations[3:]):
            ans = "true"
        return

    for i in range(6):
        if used[i] == 0:
            used[i] = 1
            permutations.append(arr[i])
            recur(cnt+1, permutations)
            permutations.pop()
            used[i] = 0


card = list(range(10))

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))
    used = [0] * 6

    ans = "False"
    recur(0, [])

    print(f"#{tc} {ans}")

