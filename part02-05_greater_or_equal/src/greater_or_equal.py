# Write your solution here

numberOne = int(input("Please type in the first number: "))
numberTwo = int(input("Please type in another number: "))

if(numberOne > numberTwo):
    print(f"The greater number was: {numberOne}")
elif(numberOne == numberTwo):
    print("The numbers are equal!")
else:
    print(f"The greater number was: {numberTwo}")