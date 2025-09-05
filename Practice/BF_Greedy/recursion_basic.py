path = []

def kfc(x):
    if x == 2:
        print(path)
        return

    for i in range(3):
        path.append(i)
        kfc(x+1)
        path.pop()

kfc(0)

print('끝')
