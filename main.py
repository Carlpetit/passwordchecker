import os
from check import PasswordCheck #Importera classen PasswordCheck från check filen

os.system("CLS") 

password = input("Skriv in ett lösernord ") #Användaren matar in ett lösernord.


if(len(password) < 8): #Kolla om lösernordet är kortare än 8
    print("Ditt lösernord är för kort.") #Låter användaren veta genom att skriva ut
    exit() #Stoppar hela programmet, vi vill inte att den ska förtsätta om lösenordet är för kort

if(not PasswordCheck.checkLetters(password)): #Kallar på funktionen checkLetter ifrån PasswordCheck classen, kollar om bokstäverna fin-
#ns i det engelska alfabetet.

    print("Innehåller en eller flera bokstäver som inte finns i det engelska alfabetet.") #Låter användaren veta genom att skriva ut texten.
    exit() #Stoppar hela programmet, vi vill inte att den ska förtsätta om lösenordet ej innehåller bokstäver från det engelska alfabetet.

        
if(not PasswordCheck.checkUppercase(password)): #Kallar på checkUppercace funktionen och kollar om lösernordet har stora bokstäver.
    print("Ditt lösenord måste minst innehålla en stor bokstav.") #Skriver ut till användaren.
    exit() #Stoppar hela programmet, vi vill inte att den ska förtsätta om lösenordet inte har stora bokstäver.
    
if(not PasswordCheck.checkNumber(password)): #Kallar på checkNUmber funktionen, kollar om lösernordet har siffror i sig.
    print("Ditt lösenord måste minst innehålla en siffra.") #Låter användaren veta.
    exit() #Stoppar hela programmet, vi vill inte att den ska förtsätta om lösenordet inte har siffror
    
if(not PasswordCheck.charCheck(password)): #Kallar på charCheck funktionen, kollar om lösernordet har speciella tecken i sig.
    print("Ditt lösenord innehåller inte speciella tecken, Till exempel _, @, $, !, ?") #Låter användaren veta 
    #Vi behöver ingen exit  funktion här då det är den sista if-vilkoret och inget mer kommer att köras.

print(f"\n{password} är ett säkert lösernord. 👍") #Lösernordet har allt som krävs och låter användaren att veta. 