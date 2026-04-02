def expression(n, result):
    if n == N:
        arr.append(result)
        return

    if operator[0]:
        operator[0] -= 1
        expression(n + 1, result + nums[n])
        operator[0] += 1
    if operator[1]:
        operator[1] -= 1
        expression(n + 1, result - nums[n])
        operator[1] += 1
    if operator[2]:
        operator[2] -= 1
        expression(n + 1, result * nums[n])
        operator[2] += 1
    if operator[3]:
        operator[3] -= 1
        expression(n + 1, int(result / nums[n]))
        operator[3] += 1

    return


N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
arr = []

expression(1, nums[0])
print(max(arr))
print(min(arr))

