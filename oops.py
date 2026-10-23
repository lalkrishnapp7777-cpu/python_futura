# class Evenorodd:
#     def __init__(self, number):
#         self.number = number
#     def even(self):
#         if self.number % 2 == 0:
#             print("even")
#         else:
#             print("odd")
# r = Evenorodd(6)
# r.even()

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"{self.name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def display(self):
#         super().display()
#         print(f"{self.name}---{self.age}")

# obj=  Child("sneha", 45)
# obj.display()

# a = [[1,2],[3,4],[5,6]]
# b = []

# for i in a:
#     for n in i:
#         b.append(n)
# print(b)

# a=[1, 2, 3, 4, 5, 6, 7, 8,]
# a.append([9, 10])
# a.extend([9, 10])
# print(a)

a = [2, 4, 6, 8, 10]
a.append(12)
a.extend([14, 16])

print(a)

