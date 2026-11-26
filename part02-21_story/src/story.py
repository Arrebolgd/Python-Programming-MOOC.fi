# Write your solution here
userInput = ""
lastWord = ""
while(True):
    word = input("Please type in a word: ")
    
    if(word == "end" or word == lastWord):
        break;
    lastWord = word
    userInput += word + " "


print(userInput)