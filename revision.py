# d = {'a':1,'b':2,'c':3,'d':4}

# for k, v in list(d.items()):
#     if v % 2 != 0:
#         d.pop(k)   

# print(d)

# class person:
#     def __init__(self,name):
#         self.name = name
#     def method(self):
#         print("Hello my name is " + self.name)

# class parent(person):
#     def method(self):
#         print("Hello my name is " + self.name + " and I am a parent")

# class child(person):
#     def method(self):
#         print("Hello my name is " + self.name + " and I am a child ")

# person1 = person("John")
# parent1 = parent("Mike")
# child1 = child("Sara")

# person1.method()
# parent1.method()
# child1.method()

import re

text = "My age is 25"
result = re.findall(r"\d+", text)

print(result)

import re

text = "apple,banana;orange"
result = re.split(r"[,;]", text)

print(result)

import math

print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5))

a=[]
a.extend("hello world")
print(a)