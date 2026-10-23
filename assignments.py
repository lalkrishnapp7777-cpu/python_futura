# # Create a lambda that returns the absolute difference between two numbers
# a = 2
# b = 1
# x = lambda a,b: a-b
# x = x(a,b)
# print(x)

# # Use lambda inside map() to convert a list of integers into strings.
# a = [1, 2, 3, 4, 5]
# s = list(map(lambda x: str(x), a))
# print(s)

# # Write a lambda to calculate the area of a triangle (0.5 * b * h).
# b = 4
# h = 7
# a=lambda b,h: 0.5*b*h
# a=a(b,h)
# print(a)

# # Filter numbers that end with digit 5 using lambda
# a = [15, 23, 35, 42, 55, 67, 75, 89, 95]
# f = list(filter(lambda x: x % 10 == 5, a))
# print(list(f))

# # Sort a list of tuples by the second element using lambda.
# # t = [(1, 3), (2, 1), (4, 2), (3, 4)]
# # s = sorted(t, key=lambda x: x[1])
# # print(s)

# # Create a lambda to check if a string contains the letter 'a'.
# s = "futuralabs"
# c = lambda x: 'a' in x
# print(c(s))

# # Create a lambda to multiply three numbers
# a = 2
# b = 3
# c = 4
# m = lambda a, b, c: a*b*c
# m = m(a, b, c)
# print(m)   

# # Use lambda + filter() to extract palindromes from a list.
# a = [121, 123, 323, 434, 454, 565, 676, 787, 898, 909]
# p = list(filter(lambda x: str(x)==str(x)[::-1], a))
# print(list(p))

# # Use lambda + map() to add 10 to each number in a list
# a = [1, 2, 3, 4, 5]
# b = list(map(lambda x: x + 10, a))
# print(b)

# # Create a lambda that returns True if a number is between 10 and 50.
# a = int(input("enter a number: "))
# b = lambda x: 10 < x < 50
# b=b(a)
# print(b)

# a = [1, 2, 3, 4, 5]
# s = list(map(lambda x: x ** 2,a))
# print(s)

# numbers = [-3, -1, 0, 2, 5]
# x = {x: "positive" if x > 0 else "negative" if x < 0 else "zero" for x in numbers}
# print(x)

def pattern(n):
    for i in range(1, n):
        for j in range(2 * i - 1):
            print("*", end= " ")
        print()
pattern(5)

    