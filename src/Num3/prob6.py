T = int(input())

answer = []
for _ in range(T):
    a, b = (map(int, input().split()))
    answer.append(a+b)

for i in answer:
    print(i)

#input때문에 길이 에러 뜸