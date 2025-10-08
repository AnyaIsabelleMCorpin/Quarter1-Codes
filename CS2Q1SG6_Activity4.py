#Ask user to inpur full name

full_name = input("Enter your full name (First, Middle, Last): ")

#Perform operations
first, middle, last = full_name.split(",")

#Remove spaces and capitalize
first = first.strip().capitalize()
middle = middle.strip().capitalize()
last = last.strip().title()

#Make middle name to initial
middle_initial = middle[0] + "."

#Rearrange name
final_name = f"{last}, {first} {middle_initial}"

#Show results
print(f"Formatted name: {final_name}")