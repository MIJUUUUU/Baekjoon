total = int(input())
n = int(input())
answer = []

for _ in range(n):
    a, b = map(int, input().split())
    answer.append(a * b)

if total == sum(answer):
    print("Yes")
else:
    print("No")


