# a=" siddhi patel"
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("s","v"))
# print(a.split(","))


#string concatenation
# a="siddhi"
# b="patel"
# c= a + b
# d= a+ " " +b
# print(c)
# print(d)



#string format

# age=36
# txt="my name is sidddhiii patel" +str(age)
# print(txt)

# age=18
# txt="my name is john, i m {}"
# print(txt.format(age))


# a=3468765432
# intro="my name is john, and my number is {}"
# print(intro.format(a))


# a=18
# b=56.78
# c=1233456789876543
# txt="my name is siddhi , i m {} and i have to buy  a gold neclace but the price of gold is {} and my no. is {}"
# print(txt.format(a,b,c))


#escape character
# txt = "We are the so-called \"Vikings\"from the north."


# a="girls are literally very intelligent and have very good brains"
# # print(a.capitalize())
# print(a.casefold())
# print(a.center())
# print(a.encode())
# print(a.count())
# print(a.find())
# print(a.title()
# x="Hello World"
# print(len())


import CurrencyRates
c= CurrencyRates()
amount=int(input("Enter the amount: "))
from_currency=input("From Currency: ").upper()
to_currency=input("To Currency:").upper()
print("From",from_currency,"To",to_currency,amount,"is")
result= c.convert(from_currency,to_currency,amount)
print(result)



