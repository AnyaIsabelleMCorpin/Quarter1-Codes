#Input the radius
radius = float(input("Enter the radius of the circle: "))

#Calculate the area of the circle
area = 3.14159*(radius**2)
rounded_area = round(area, 2)

#Give the output
print("The area of the circle is: ", rounded_area, "square units.")