# Write your solution here
wordOne = input("Please type in the 1st word: ")
wordTwo = input("Please type in the 2nd word: ")

if(wordOne.lower() > wordTwo.lower()):
    print(f"{wordOne} comes alphabetically last.")
elif(wordOne.lower() == wordTwo.lower()):
    print("You gave the same word twice.")
else:
    print(f"{wordTwo} comes alphabetically last.")