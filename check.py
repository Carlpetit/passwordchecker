





alfabetet = "ABCDEFGHIJKLMNOPQRSTUWVXYZ" 
class PasswordCheck(): 
    
    
    def checkLetters(password: str) -> bool: 
        englishLetter = True 
        
        for char in password: 
            if not char.isdigit() and char.isalpha(): 
                if char.upper() in alfabetet: 
                    continue 
                else:
                    englishLetter = False 
                    break 
            
        return englishLetter 
    

   
    def checkUppercase(password: str) -> bool: 
        count = 0 
        for char in password: 
            if char.isupper(): 
              count += 1  

        
        if count == 0:
            return False
        else: 
            return True

    
    def checkNumber(password: str): 
        count = 0 
        
        for x in password: 
            if x.isnumeric(): 
              count += 1  

        
        if count == 0:
            return False
        
        return True 


   
    def charCheck(password: str) -> bool: 
        specialChars = "_@$!?+&%*.,\"^~¨;:-<>|§½/()={[]}'" 
        count = 0 
        
        for char in password:
            if char in specialChars:
                count += 1 
            
        if count == 0: 
            return False 
            
        return True 
