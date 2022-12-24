


#f = open("img.png","rb")
f=open("portfoliophoto.jpg","rb")
f1=open("portfoliophoto.jpg","wb")
for i in f:
    f1.write(i)



f2=open("portfoliophoto.jpg","rb")
print(f2.read())