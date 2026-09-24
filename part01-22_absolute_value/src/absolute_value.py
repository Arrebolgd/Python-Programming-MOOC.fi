# Write your solution here
# Please type in a number: -7
# The absolute value of this number is 7
number : int = int(input("Please type in a number: "))
if(number > 0):
    print(f"The absolute value of this number is {number}")
else:
    print(f"The absolute value of this number is {(-number)}")