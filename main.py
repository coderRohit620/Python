# first program
# print("hello")

# variable
name = "Rohit"
age = 20
salary = 10000

# print("Name :",name, "Age :",age , "Salary :",salary )

# Taking Input
# name = input("Enter your name :")
# age = int(input("Enter your age :"))
# print(name, age)
# print(f"My name is {name} and I am {age} years old.")

# Type Conversion

a = "125"
a = int(a)
# print(type(a))

# Arithmetic Operator

# print(10 + 5)   # 15
# print(10 - 5)   # 5
# print(10 * 5)   # 50
# print(10 / 5)   # 2.0
# print(10 // 3)  # 3
# print(10 % 3)   # 1
# print(2 ** 3)   # 8

# Comparison Operators
# print(10 > 5)
# print(10 < 5)
# print(10 == 10)
# print(10 != 5)
# print(10 >= 5)
# print(10 <= 5)

# slicing
greeting = "Good Morning"
name = "Rohit"
# print(type(name))
# print(greeting + " " + name)
# print(name[0])
# print(name[0:5])
# print(name[0:5:2])

# print(len(name))


# list and tuples

# LIST
l1 = [2,8,4,75,6,47,1,541]
# print(l1)
# l1.sort() #sort the list 
# l1.reverse()# reverse the list
# l1.append(45)# add 45 at the end of the list
# l1.insert(3, 533) #inserts 533 at index 2
# l1.pop(2) #remove element at index 2
# l1.remove(75) #remove 75 from the list 
# print(l1)

# Practice set
# f1 =input("Enter Fruit Number 1 :")
# f2 =input("Enter Fruit Number 2 :")
# f3 =input("Enter Fruit Number 3 :")
# f4 =input("Enter Fruit Number 4 :")
# f5 =input("Enter Fruit Number 5 :")
# myFruitList = [f1,f2,f3,f4,f5]

# print(myFruitList)

# write a programe to sum all the given nuber in the list
a = [2,4,56,7]
sum = 0
for i in a:
    sum += i
    
# print("Sum :",sum)
# TUPLES

t = (1,2,3,4,5,6) 
# print(t[0])
# cannot update the tuple values

# t1 = () #Empty Tuple 
# t1 = (1,) #tuple with only element needs a comma
# t = (1,2,3) #Tuple withe more thean one value
# print(t)

# TUPLES METHODS
t = (1,2,3,3,4,5,5,5,5,5,6,6,6) 
# print(t.count(5))
# print(t.index(3))
a= (7,0,8,0,0,9)
# print(a.count(0))

# Dictionary & Sets:
myDict = {
    "fast":"In a quick Manner",
    "rohit":"A coder",
    "marks":[1,55,88],
    "anotherdict":{'ravi':'coder'},
}


# print(myDict["Fast"])
# print(myDict["Rohit"])
# myDict["Marks"] = [45,88,99] # we can update the dict
# print(myDict["Marks"])
# print(myDict["anotherdict"]["ravi"])


# # Dictionary Methods

# collection key value pair
print(myDict.keys()) 
print(list(myDict.keys())) 

print(myDict.values())
print(list(myDict.values()))


