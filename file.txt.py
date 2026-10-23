# import os
# with open("text.txt","w") as f:
#     f.write("hello")
# with open("text.txt","r") as f:
#     print(f.read())  
# os.remove("text.txt")

# try:
#     x=10/0
#     b=10/2
# except  ZeroDivisionError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

# try:
#     x=("10" + 10)
# except TypeError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

# try:
#     print(a)
# except NameError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

# try:
#     x = {"name": "amal", "age": 20}
#     print(x["place"])
# except KeyError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

# try:
#     file = open("text.txt", "r")
# except FileNotFoundError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")
    print("Age is valid")
      
    check_age(19)
