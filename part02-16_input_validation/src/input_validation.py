from math import sqrt

# Write your solution here
userInput = -1;
while(userInput != 0):
    userInput = int(input("Please type in a number: "))
    if(userInput > 0):
        print(sqrt(userInput))
    elif(userInput != 0):
        print("Invalid number")

print("Exiting...")