# Write your solution here
hourlyWage : float = float(input("Hourly wage: "))
hoursWorked : int = int(input("Hours worked: "))
dayWeek : str = str(input("Day of the week: "))

wage = hourlyWage * hoursWorked;

if(dayWeek != "Sunday"):
    print(f"Daily wages: {wage} euros")
else:
    print(f"Daily wages: {wage*2} euros")