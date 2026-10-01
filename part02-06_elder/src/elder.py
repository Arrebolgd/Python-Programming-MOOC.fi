# Write your solution here
print("Person 1: ")
nameOne = input("Name: ")
ageOne = int(input("Age: "))

print("Person 2: ")
nameTwo = input("Name: ")
ageTwo = int(input("Age: "))

if(ageOne > ageTwo):
    print(f"The elder is {nameOne}")
elif (ageOne == ageTwo):
    print(f"{nameOne} and {nameTwo} are the same age")
else:
    print(f"The elder is {nameTwo}")