# ABCD 존재
N = int(input())

text = [input() for _ in range(N)]

pattern = ['AB', 'CD']  # 찾을 패턴 설정

ans = False  # 패턴 유무

# 전체 순회
for i in range(N-1):
    for j in range(N-1):
        cnt = 0  # 패턴 중 맞는 개수
        for x in range(2):
            for y in range(2):
               if text[i+x][j+y] == pattern[x][y]:
                   cnt += 1
        if cnt == 4:  # 4개 다 맞는 경우
            ans = True  # 패턴 찾기 완료 -> 순회 중지
            break

print(ans)