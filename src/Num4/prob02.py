a, b = map(int, input().split())
line = []

for _ in range(a):
    n = list(map(int, input().split()))

    for i in n:
        if i < b:
            line.append(i)

for j in line:
    print(j,end=" ")