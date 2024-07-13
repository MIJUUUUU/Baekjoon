h, m= input().split()
c= input()

h= int (h)
m= int (m)
c= int (c)

m = (m+c)

while m>=60 or h>=24:
    if m+c>=60:
        h = h+1
        m = m-60
    if h>=24:
            h= h%24

print(h,m)