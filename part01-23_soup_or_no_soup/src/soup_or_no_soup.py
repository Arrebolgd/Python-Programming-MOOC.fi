# Write your solution here
# Please tell me your name: Kramer
# How many portions of soup? 2
# The total cost is 11.8
# Next please!

name : str = input("Please tell me your name: ")
if(name != "Jerry"):
    portions : int = int(input("How many portions of soup? "))
    print(f"The total cost is {5.90 * portions}")

print("Next please!")