import datetime
now=datetime.datetime.now()
print("Current date and time:", now)
today=datetime.date.today()
print("Today's date:", today)

import math
print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))

try:
    a=int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
    print("Result:", result)
except:
    print("Error: You cannot divide by zero or enter invalid input.")
