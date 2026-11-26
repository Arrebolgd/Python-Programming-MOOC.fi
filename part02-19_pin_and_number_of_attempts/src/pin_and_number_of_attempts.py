# Write your solution here
PIN = 4321
tries = 0
while(True):

    userInput = int(input("PIN: "))
    tries += 1
    
    if(userInput == PIN):
        break

    print("Wrong")
    

if(tries == 1):
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {tries} attempts")
