classes = int(input("number of classes in a semester: "))
attendent = int(input("number of complulsary classes: "))
percentage=((attendent)/(classes)*100)
if percentage>=75:
    print("allow to sit in exam")
else:
    print("not allow to sit in exam")    