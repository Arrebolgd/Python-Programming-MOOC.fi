# Write your solution here
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2
students : int = int(input("How many students on the course? "))
groupSize : int = int(input("Desired group size? "))
result : float = students / groupSize;

if(result % 2):
    print(f"Number of groups formed: {int(result +1)}")
else:
    print(f"Number of groups formed: {int(result)}")
    