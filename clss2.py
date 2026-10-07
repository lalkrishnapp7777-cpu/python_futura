
# x = 2
# y = 3
# a=lambda x,y:0.5*x*y
# a=a(x,y)
# print(a)

# x=[1,2,3,4,5,6,7]
# y=lambda x: x[0]
# print(y(x))

# a = 4
# b = 5
# x= lambda a,b:a+b
# print(x(a,b))

a = [1,2,3,4,5,6,7,8]
cube=list(map(lambda x: x**3,a))
print (list(cube))

a = [1,2,3,4,5,6,7,8]
even=list(filter(lambda x: x%2==0,a))
print (list(even))