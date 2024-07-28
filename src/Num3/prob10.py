n = int(input())
star = '*'
space = ' '

for i in range(n,0,-1):#4,3,2,1,0
    print(space * (i-1) + star * ( n-(i-1)))
