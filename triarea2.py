import math
a=int(input("enetr the first side:"))
b=int(input("enetr the enter the second side:"))
c=int(input("enetr the enter the third side:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)

