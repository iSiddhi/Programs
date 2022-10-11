#write ny program and calculate the area of triangle 


a=float(input('enter the first side'))
b=float(input('enter the first side'))
c=float(input('enter the second side'))

#calculating
s= (a+b+c)/2

Area = (s*(s-a)*(s-b)*(s-b))**0.5

print(Area)