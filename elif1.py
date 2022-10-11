from re import A


a=1
b=2
if a>b:
    print("a")
else:
    print("b")

    print("a")if a>b else print("b")

#---------------------------------------------------------------------------------------------------------------------------
#marks   #grades
#100-90     #a
#90-80      #b
#80-70      #c

marks=int(input("enter your marks:"))

if marks>90 and marks<=100:
    print("Your Grade is A")
if marks>80 and marks<=90:
    print("Your grade is B")    
if marks>70 and marks<80:
    print("Your grade is C")    
else:
    print("not a valid number")
    
