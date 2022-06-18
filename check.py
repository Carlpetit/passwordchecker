#Skapar en klass för att minska all kod i våran Main.py fil
#Om det skulle bli något fel så behöver jag inte gå igenom en stor mängd kod i en och samma fil.





alfabetet = "ABCDEFGHIJKLMNOPQRSTUWVXYZ" #Skapar en variabel och tilldelar hela engleska alfabetet.

class PasswordCheck(): #Definerar en class med namn PasswordCheck

    #Meningen med denna funktion är att den ska kolla om det finns bokstäver som inte finns i alfabetet i lösernordet.
    def checkLetters(password: str) -> bool: #Definerar en funktion som tar en parameter vilket är lösernordet och returnerar en bool (true/false)
        englishLetter = True #englishLetter till true

        for char in password: #iterera igenom parametern password vilket är lösernordet som du mäta in tidigare i programmet
            if not char.isdigit() and char.isalpha(): #Vi måste kolla om karaktären inte är en siffra och att den måste vara en bokstav
                if char.upper() in alfabetet: #Gör om karaktären till en stor bokstav och kollar om den finns i "alfabetet" variabeln
                    continue #Karaktären finns i det engelska alfabetet och då gör vi inget. Låter lopen börja om och gå vidare till nästa steg.
                else:
                    englishLetter = False #karaktären finns inte i det engelska och vi sätter englishLetter till false 
                    break #Stannar lop då lösernordet innehåller bokstav som ej finns i det engelska alfabetet
            
        return englishLetter #returnerar false
    

    #Meningen med denna funktion är att kolla efter stora bokstäver
    def checkUppercase(password: str) -> bool: #Funktionen tar in en parameter och returnerar en bool 
        count = 0 #tilldelar värdet 0 till counter, den ska räkna hur många stora bokstäver det finns i lösernordet.
        for char in password: #iterera igenom parametern password, char är bokstäven
            if char.isupper(): #Kollar om char är en stor bokstav.
              count += 1  #Addera counter med ett då villkoret är sant.

        
        if count == 0: #Om count är noll så returnerar vi false
            return False
        else: #Annars returnera true
            return True

    #Meningen med funktionen är att leta efter siffror 
    def checkNumber(password: str): #Returnerar en bool och tar in en parameter som ska vära en sträng
        count = 0 #Räknar hur många siffror det finns i lösernordet
        
        for x in password: #iterera igenom parametern password, char är bokstäven/siffran
            if x.isnumeric(): #Kolla om det är en siffra
              count += 1  #addera count med 1

        
        if count == 0: #Om count är noll returnera falsse 
            return False
        
        return True #returnerar true om count inte är noll


    #meningen med denna funktion är att kolla efter speciella tecken
    def charCheck(password: str) -> bool: #password som parameter och returnerar en bool
        specialChars = "_@$!?+&%*.,\"^~¨;:-<>|§½/()={[]}'" #EN sträng med olicka speciella tecken. 
        count = 0 #Räknar hur många speciella tecken det finns.
        
        for char in password: #iterera igenom parametern password, char är bokstäven/siffran
            if char in specialChars: #om char finns i specialChars
                count += 1 #addera count med 1
            
        if count == 0: # Om count är false 
            return False #Returnera false
            
        return True #Returnerar ture om count inte är noll. 