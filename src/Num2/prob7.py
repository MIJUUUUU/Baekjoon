a, b, c = map(int, input().split())

if a == b and b == c:
    answer = 10000 + a * 1000
elif a == b or a == c or b == c:
    if a == b or a == c:
        answer = 1000 + a * 100
    else:
        answer = 1000 + c * 100
if a != b and a != c and b != c:
    if a > b and a > c:
        answer = a * 100
    elif b > a and b > c:
        answer = b * 100
    elif c > a and c > b:
        answer = c * 100
print(answer)
