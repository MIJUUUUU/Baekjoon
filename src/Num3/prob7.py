T = int(input())
answer = []
for _ in range(T):
    a, b = map(int, input().split())
    answer.append(a+b)

i=1
while i<=T:
    print("Case #",i,sep='',end="")
    print(":",answer[i-1])
    i+=1