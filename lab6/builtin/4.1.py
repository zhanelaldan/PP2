import math
def specific_milliseconds(x):
    return(math.sqrt(x))

num1 = int(input())
num2 = int(input())
num3 = specific_milliseconds(num1)

print(f"Square root of {num1} after {num2} miliseconds is {num3}")