# Write your solution here

number_of_numbers = 0;
sum_of_numbers = 0;
pos_numbers = 0;
neg_numbers = 0;

while(True):
    print("Please type in integer numbers. Type in 0 to finish.")
    user_input = int(input("Number: "))

    if(user_input == 0):
        break

    if(user_input > 0):
        pos_numbers += 1

    if(user_input < 0):
        neg_numbers += 1


    sum_of_numbers += user_input
    number_of_numbers += 1

print(f"Numbers typed in {number_of_numbers}")
print(f"The sum of the numbers is {sum_of_numbers}")
print(f"The mean of the numbers is {sum_of_numbers/number_of_numbers}")
print(f"Positive numbers {pos_numbers}")
print(f"Negative numbers {neg_numbers}")