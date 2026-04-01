"""
N개의 원판을 start에서 end를 보내는 방법은
N-1개의 원판을 start에서 end를 거쳐 sub로 보내고
N번째 원판을 end를 보내고
N-1개의 원판을 다시 sub에서 start를 거쳐 end로 보내는 것
"""

def hanoi(N, start, end, sub):
    if N == 0:
        return
    hanoi(N-1, start, sub, end)
    ans.append([start, end])
    hanoi(N-1, sub, end, start)

N = int(input())
ans = []
hanoi(N, 1, 3, 2)
print(len(ans))
for i in range(len(ans)):
    print(*(ans[i]))

"""
// 더 빠른 방법
import sys
def hanoi(n, start, end, sub):
    if n == 0:
        return
    hanoi(n - 1, start, sub, end)
    out.append(f"{start} {end}\n")
    hanoi(n - 1, sub, end, start)


N = int(sys.stdin.readline().strip())

# 이동 횟수는 미리 계산 가능
sys.stdout.write(f"{(1 << N) - 1}\n")

out = []
hanoi(N, 1, 3, 2)
sys.stdout.write("".join(out))
"""