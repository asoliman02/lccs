#Date: 15th April 2024
#Objective: to create and understand loops

#for loop:
for i in range(1,10):
    print(i)
    
    
#while loop/brute loop:
var1 = 'Again'
while var1 == 'Again':
    print('Running while in loop ')
    check= input('Do you want the loop to continue? ')
    if check == 'N':
        break