import math
sides = int(input(""))
length = float(input(""))
apothem=length/2*math.tanh(180/sides)
area=sides*length*apothem/2
print(area)
