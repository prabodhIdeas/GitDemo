print("Whatsuppp!!YO")

a = "prabodh"

b = "kumar"

print(a,b)
#every dog has a day
a, b, c = 5.4, 7, "pepper"

print(b,c)
#print("value is" , a) - can also use the below function
print("{} {}".format("value is", a))

# List

values = [1, 7.5, "demos", 123]

print(values[2])
print(values[-1])
print(values[1:-1])

values.insert(2, "class") #to add value within the list
print(values)

values.append("enough") #append is to add any value at the end
print(values)

values[2] = "END game" #to replace 2nd variable in the list
print(values)

del values[0] #delete the value
print(values)

#Tuple

val1 = (4, 7.5, "hey")

print(val1)

#Dictionary

val2 = {"x": 4, "y": 5.5, "dude": "woman"}
print(val2["dude"])

#add values in dictionary

Dict = {}

Dict["firstname"] = "prabodh"
Dict["lastname"] = "kumar"
print(Dict)