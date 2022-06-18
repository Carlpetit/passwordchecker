import os
from check import PasswordCheck 

os.system("CLS") 

password = input("Enter a password ")


if(len(password) < 8):
    print("Your password is too short.")
    exit() 

if(not PasswordCheck.checkLetters(password)): 

    print("Contains one or more letters that are not in the English alphabet.") 
    exit() 

        
if(not PasswordCheck.checkUppercase(password)):
    print("Your password must contain at least one uppercase letter.")
    exit()
    
if(not PasswordCheck.checkNumber(password)): 
    print("Your password must contain at least one digit.") 
    exit() 
    
if(not PasswordCheck.charCheck(password)):
    print("Your password does not contain any special characters") 
 

print(f"\n{password} is a safe password. 👍") 
