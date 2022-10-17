#if the lenghth of that input is greater than 3 characters then add ing as prefix else print the same input without ading input

x=str(input("enter the word"))
y=len(x)
if y>3:
    print(x+"ing")
else:
    print(x)    