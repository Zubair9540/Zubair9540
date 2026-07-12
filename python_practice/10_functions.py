def greet_user():
    print("Hello, User!")
# greet_user()

def falana(name):
    print(f"Assalamu alaikum, {name} Kese ho"
          )
# falana("Zubair")

def falana(name = "Haroon"):
    print(f"Assalamu alaikum {name} bhai! kese ho")
# falana()

# Return Values
def square(number):
    return number * number
# print(square(9))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(6))

# lambda function
# def x(a):
#     return a/2
# print(x(4))
# x = lambda a: a/2
# print(x(4))

def x(a,b):
    return a * b

x = lambda a,b: a*b
print(x(2,8))