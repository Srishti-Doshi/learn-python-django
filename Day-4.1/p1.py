# Dictionary
mydict = {"name":"Raj", "age":20, "city":"Indore"}

#Accessing and Retrieving data
print(mydict.get("name"))

#Returns a view object
print(mydict.keys())
print(mydict.values())
print(mydict.items()) #key-value pair as tuple

mydict.update({"post":"developer"})
print(mydict)


#Modifying
# copy() ->reference copy-> shallow copy
# clear()


# pop()
# popitem()


# setdefault()

#Creating
new_dict = dict.fromkeys(["a", "b", "c", "d"],0)
print(new_dict)

#popping
data = mydict.pop("age")
print(data)