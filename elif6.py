#company will give bonus on following criteria

#time spent in company                bonus
#greater than 10 years                    10%
# more than 6 and less than 10             8%
# less than 6                              5%
# ask the salary and time spent from the user
# print the net bonus amount accoringlytime
#--------------------------------------------------------------------------------------------
time=int(input("time spent in the company"))
salary=int(input("salary "))

if time>10: 
    print("(10/100)*salary")
elif time <10 and time>6:
    print("(8/100)*salary") 
else:
    print("(5/100)*salary")