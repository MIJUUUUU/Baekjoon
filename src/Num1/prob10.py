a,b,c = map(int, input())
d,e,f = map(int, input())

abc= 100*a + 10*b + c
def1= 100*d + 10*e + f
line3= f*abc
print(line3)

line4= e*abc
print(line4)

line5= d*abc
print(line5)

line6 = line3+ (10*line4) + (100*line5)
print(line6)