T = int(input())

answer=[]
for _ in range(T):
    A, B = map(int, input().split())
    answer.append(A+B)

for x in answer:
    print(x)
