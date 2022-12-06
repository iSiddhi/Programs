first=int(input("enter the first number"))
operator=(input("enter the operator"))

second=int(input("enter the second number"))


if operator=="+":
    print(first+second)
elif operator=="*":
    print(first*second) 
elif operator=="/":
    print(first/second)
elif operator=="-":
    print(first-second)
else:
    print("invalid number")
