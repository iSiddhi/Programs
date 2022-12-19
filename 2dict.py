#def isEven(i):
  #  return i%2==0

# from copyreg import _Reduce
from functools import reduce


# list1=[3,2,4,5,6,7,8,9,16,18] 
#output=filter[isEven,list]   
#print(output)


list1=[3,2,4,5,6,7,8,9,16,18] 
#output=list1(_Reduce(lambda i:i+=1,list1))
# print(output) 

output3=reduce(lambda a,b:a+b,list1)
print(output3)
#=_Reduce#performing the opertaion on each nd everyone 



