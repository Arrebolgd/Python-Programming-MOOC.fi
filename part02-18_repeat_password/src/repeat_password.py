# Write your solution here
pswMatch = False;
userPswOne = input("Password: ")
while(not pswMatch):
    
    userPswTwo = input("Repeat password: ")
    if(userPswOne == userPswTwo):
        pswMatch = True
    else:
        print("They do not match!")

print("User account created!")