# Write your solution here
farenheit : float = float(input("Please type in a temperature (F): "))
celsius : float = (farenheit - 32) * 5 / 9
print(f"{farenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if(celsius < 0):
    print("Brr! It's cold in here!")