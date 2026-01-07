"""
7 4
apple
ant
sand
apple
append
sand
sand
"""
"""
sand
apple
append
"""
import sys
input = sys.stdin.readline  # 시간 초과 해결

n, m = map(int, input().strip().split())
words = []
for _ in range(n):
    word = input().strip()  # 개행문자 제거
    words.append(word)

word_count = {}  # 딕셔너리로 저장
for word in words:
    # 단어 - 나온 횟수
    word_count[word] = word_count.get(word, 0) + 1  # get = 기존 값이 없으면 디폴트로 0

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))  # 정렬 기준: 나온 횟수, 단어 길이, 알파벳 순서
for word, count in sorted_words:
    if len(word) >= m:  # 단어 길이가 m 이상인 경우만 출력
        print(word)