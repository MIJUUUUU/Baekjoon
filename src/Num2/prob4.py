x = int(input())
y = int(input())
Quad1 = x>0 and y>0
Quad2 = x<0 and y>0
Quad3 = x<0 and y<0
Quad4 = x>0 and y<0

if Quad1:
    print("1")
elif Quad2:
    print("2")
elif Quad3:
    print("3")
elif Quad4:
    print("4")