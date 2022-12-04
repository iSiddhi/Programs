myDictionary={
    "Name" : "Gaurav",
    "Age" : 21
}
print(myDictionary)
age=myDictionary.get("Age")
print(age)
keys=myDictionary.keys()
print(keys)
value=myDictionary.values()
print(value)
items=myDictionary.items()
print(items)
myDictionary["Roll no"]=10
print(myDictionary)
myDictionary.update({"Name":"Virat"})
print(myDictionary)
myDictionary.pop("Name")
print(myDictionary)
myDictionary.popitem()
print(myDictionary)