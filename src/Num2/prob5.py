h, m = input().split()

h = int(h)
m = int(m)

if m < 45:
    h = h - 1
    if h < 0:
        h = 23
    m = m + 15

h * 100 + m
print(h,m)

# 틀린 이유 모르겠음