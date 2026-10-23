
# def fact(n):
#     if n<=1:
#         return n
#     return n*fact(n-1)
# print(fact(1))

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(5))


def rev(s):
    if len(s) == 0: 
        return s
    return rev(s[1:]) + s[0] 
print(rev("lalkrishnaa"))