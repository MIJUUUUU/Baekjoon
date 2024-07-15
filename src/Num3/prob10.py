space = ' ' #공백 변수 space 지정
star = '*'
n = int(input())
for i in range(n, 0, -1): #n에서 1까지 역순으로 숫자 생성(마지막 숫자보다 +1임을 기억)
    print(space * (i - 1) + star * (n - (i - 1))) #공백과 for문 곱하고 + 별과 input값에서 for문-1을 뺀걸 곱함 
n = int(input())
for i in range(1, n+1): #1~n까지 범위
    print(" "*(n-i)+"*"*i) #5넣었을 때, 4공백+1별