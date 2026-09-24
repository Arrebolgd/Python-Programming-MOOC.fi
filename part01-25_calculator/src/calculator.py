# Write your solution here

numberOne : int = int(input("Number 1: "))
numberTwo : int = int(input("Number 2: "))
operation : str = input("Operation: ")

if(operation == "add"):
    print(f"{numberOne} + {numberTwo} = {numberOne + numberTwo}")
if(operation == "subtract"):
    print(f"{numberOne} - {numberTwo} = {numberOne - numberTwo}")
if(operation == "multiply"):
    print(f"{numberOne} * {numberTwo} = {numberOne * numberTwo}")