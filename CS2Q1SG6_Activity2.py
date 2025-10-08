#Get inputs

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

#Calculate the distance between two points

import math
d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
rounded_d = round(d, 2)

#Show output

print("The distance between the two points is:", rounded_d)