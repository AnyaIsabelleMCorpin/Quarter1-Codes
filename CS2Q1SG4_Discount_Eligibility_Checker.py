#Get inputs

student = input("Are you a student? Type Y or N: ")
age = int(input("Enter your age: "))
membership_card = input("Do you have a membership card? Yes or No: ")

#Calculate is eligible for discount

if (student == "Y" or age >= 65) and membership_card == "Yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")