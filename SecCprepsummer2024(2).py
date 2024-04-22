#Date: 11 April 2024
#Objective: To add and subtract variables that are inputted into the computer

num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))
choice = input("Would you like to add or subtract them? ")

if choice == 'a' or choice == 'A':
    print("The answer is",num1 + num2)
 
elif choice == 's' or choice == 'S':
    print ("The answer is", num1 - num2)

else:
    print("Invalid option")