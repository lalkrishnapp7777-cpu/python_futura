# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)      
# s1 = Student("LalKrishna", 20, 85)
# s1.display_details()

# class Car:
#     def __init__(self, brand, model, mileage):
#         self.brand = brand
#         self.model = model
#         self.mileage = mileage
#     def display(self):
#         print(self.brand, self.model, self.mileage)
# car1 = Car("Toyota", "Innova", 15)
# car1.display()

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth
#     def perimeter(self):
#         return 2 * (self.length + self.breadth)
# r = Rectangle(10, 5)

# print("Area:", r.area())
# print("Perimeter:", r.perimeter())

class Employee:
    def __init__(self, name, salary, bonus, deductions):
        self.name = name
        self.salary = salary
        self.bonus = bonus
        self.deductions = deductions
    def calculate_salary(self):
        return self.salary + self.bonus - self.deductions

e = Employee("lalkrishna", 30000000, 5000, 2000)
print("Employee:", e.name)
print("Net Salary:", e.calculate_salary())

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