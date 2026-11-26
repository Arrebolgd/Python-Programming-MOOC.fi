# Write your solution here

toBeTaxed = int(input("Value of gift: "))

if(toBeTaxed < 5_000):
    print("No tax!")
elif(toBeTaxed >= 5_000 and toBeTaxed < 25_000):
    print("Amount of tax: " + str(100 + (toBeTaxed - 5000) * 0.08))
elif(toBeTaxed >= 25_000 and toBeTaxed < 55_000):
    print("Amount of tax: " + str(1_700 + (toBeTaxed - 25_000) * 0.10))
elif(toBeTaxed >= 55_000 and toBeTaxed < 200_000):
    print("Amount of tax: " + str(4_700 + (toBeTaxed - 55_000) * 0.12))
elif(toBeTaxed >= 200_000 and toBeTaxed < 1_000_000):
    print("Amount of tax: " + str(22_100 + (toBeTaxed - 200_000) * 0.15))
elif(toBeTaxed >= 1_000_000):
    print("Amount of tax: " + str(142_100 + (toBeTaxed - 1_000_000) * 0.17))