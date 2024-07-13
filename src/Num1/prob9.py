A, B, C = map(int, input().split())
result1= (A+B)%C
print(result1)

result2 = ((A%C) + (B%C))%C
print(result2)

result3 = (A*B)%C
print(result3)

result4 = ((A%C) * (B%C))%C
print(result4)