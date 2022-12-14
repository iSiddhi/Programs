num1=[1,2,3,4,5]
num2=[1,2,3,4,5]
result=[]


for i in range(len(num1)):
    result.append(num1[i]+num2[i])

print(result)    



lst1=[True,False,True,False,True]
lst2=[]

result=[]
and_result=[]
or_result=[]



for i in range(len(lst1)):
    and_result.append(lst1[i] and lst2[i])
    or_result.append(lst1[i] or lst2[i])
print(and_result)
print(or_result)