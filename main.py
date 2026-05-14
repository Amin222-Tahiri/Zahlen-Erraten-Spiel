import random

geheime_zahl = random.randint(1, 100)
versuche = 0

while True:
    
    tipp = int(input("Rate eine Zahl zwischen 1 und 100: "))
    versuche = versuche + 1
    
    
    if tipp < geheime_zahl:
            print("Zu niedrig! Versuche es noch einmal.")
            
    elif tipp > geheime_zahl:
        print("Zu hoch! Versuche es noch einmal.")
        
    else:
        print(f"Glückwunsch! Du hast die Zahl in {versuche} Versuchen erraten!")
    break
