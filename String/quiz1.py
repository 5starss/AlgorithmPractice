# s1의 각 글자가 s2에 모두 존자하는가?

s1 = 'XYPV'
s2 = 'EOGGXYPVSY'

# 2중 for문
ans = False
for i in s1:
    for j in s2:
        if i == j:
           ans = True  # 존재할 경우 다음 글자
           break
    else:
        ans = False  # 순회를 다 돈 경우 => 없을 경우 전체 순회 종료
        break
print(ans)

# if - in 사용
ans = False
for i in s1:
    if i in s2:  # 존재할 경우
        ans = True
    else:  # 없는 경우
        ans = False
        break  # 더 찾아볼 필요 없음
print(ans)
