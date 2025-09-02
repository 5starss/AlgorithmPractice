import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    original = list(map(int, input().split()))
    M = int(input())
    command = list(input().split())

    i = 0
    while i < len(command):
        if command[i] == "I":
            i += 1
            x = int(command[i])
            i += 1
            y = int(command[i])
            i += 1
            tmp = i + y
            while i < tmp:
                original.insert(x, int(command[i]))
                x += 1
                i += 1
        elif command[i] == "D":
            i += 1
            x = int(command[i])
            i += 1
            y = int(command[i])
            i += 1
            for _ in range(y):
                original.pop(x)

        elif command[i] == "A":
            i += 1
            y = int(command[i])
            i += 1
            tmp = i + y
            while i < tmp:
                original.append(int(command[i]))
                i += 1

    print(f"#{tc}", *original[:10])
