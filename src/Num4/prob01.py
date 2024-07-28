n = int(input())
line = list(map(int, input().split()))
num = int(input())
answer = 0

for i in range(line):
    if line[i] == num:
        answer += 1
print(answer)