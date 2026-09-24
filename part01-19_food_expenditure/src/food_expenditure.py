# Write your solution here
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros
cafeteria : float = float(input("How many times a week do you eat at the student cafeteria? "))
lunchPrice : float = float(input("THe price of the typical student lunch? "))
groceries : float = float(input("How much money do you spend on groeries in a week? "))

weekly : float = (cafeteria*lunchPrice) + groceries;
daily : float = weekly / 7;

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")