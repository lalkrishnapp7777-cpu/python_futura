#a={"name":"kkk","age":20}
#a["grade"]="A"
#a.update({"place":"kerala","gender":"male"})

#print(a.keys()) 
#print(a.values()) 
#print(a.items()) 

#for key,value in a.items(): 
   # print(key,value)

#del a["age"] 
#a.pop("name")

#print(a)

# class A:
#    def hello(self):
#       print("A")
# class B(A):
#    def hai(self):
#       print("B")
# class C(B):
#    pass

# obj = C()
# obj.hello()
# obj.hai()

# class A:
#    def greet(self):
#       print("Hello from A")
# class B:
#    def greet(self):
#       print("Hello from B")
# class C(A, B):
#    pass

# obj = C()
# obj.greet()
# print(C.__mro__)

# class Bank:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self._dept=dept
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary=amount
# b=Bank("lalkrishna","CEO",100000000)
# print(b.name)    
# print(b._dept)    
# # print(b.__salary)
# print(b.get_salary())  #getter
# # print(b._Bank__salary) #name mangling
# b.set_salary(1550000000) #setter
# print(b.get_salary())

from abc import ABC, abstractmethod

class shape(ABC):
      @abstractmethod
      def area(self):
            pass
class circle(shape):
      def __init__(self, radius):
          self.radius = radius
      def area(self):
          return 3.14 * self.radius ** 2
class rectangle(shape):
      def __init__(self, length, breadth):
            self.length = length
            self.breadth = breadth
      def area(self):
           return self.length * self.breadth
      
c = circle(5)
r = rectangle(5,6)
print(c.area())
print(r.area())