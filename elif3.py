#take input of age from 3 people and determine the youngest and oldest

Siddhi=int(input("age of a first person"))
Shruti=int(input("age of second person"))
Dheeraj=int(input("age of third person"))

if Siddhi<Shruti:
    print("Siddhi is youngest")

if Siddhi<Dheeraj:
    print("Siddhi is youngest")

if Shruti>Dheeraj:
    print("Shruti is oldest")

elif Shruti>Siddhi and Dheeraj<Shruti:
    print
