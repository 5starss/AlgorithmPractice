N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
ans = []
num = 1
while arr:
    if not stack:
        stack.append(num)
        ans.append('+')
        num+=1
    else:
        if stack[-1] == arr[0]:
            stack.pop()
            arr.pop(0)
            ans.append('-')
        elif stack[-1] < arr[0]:
            stack.append(num)
            ans.append('+')
            num+=1
        else:
            print('NO')
            break
else:
    for i in ans:
        print(i)

"""
// 더 빠른 버전
import sys
input=sys.stdin.readline

n=int(input())
cmd=[]
stack=[]
curr=1  // 스택에 넣는 값
possible=True  // 가능 불가능
for _ in range(n):  // 바로바로 값 확인
    num=int(input())  
    while curr<=num:  // 일단 해당 수가 스택에 넣은 수보다 크면 그 수까지 push
        stack.append(curr)
        cmd.append('+')
        curr+=1
    if stack[-1]!=num:  // 만약 pop으로 수열을 만들 수 없으면 No
        possible=False
        break
    stack.pop()  // pop으로 수열을 만들 수 있다는 의미
    cmd.append('-')
if possible:
    print('\n'.join(cmd))
else:
    print('NO')
"""