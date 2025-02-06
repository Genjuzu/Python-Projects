import random  # 🔹 Wichtig: random-Modul muss importiert werden

again = "Yes"

while again in ["yes", "Yes"]:
    ergebnis = random.randint(1, 10)        # Generiert eine Zahl zwischen 1 und 10
    versuche = 3                                 # Zähler für Falscheingaben initialisieren auf 0

    # Nutzer Grüßen & Raten
    print("Willkommen! Bitte errate die Zahl zwischen 1-10. Du hast 3 versuche: ")

    # Solange der Nutzer Versuche hat
    while versuche > 0:
        eingabe = int(input())

        while eingabe not in ["1","2","3","4","5","6","7","8","9"]:
            eingabe = int(input("Ungültige Eingabe! Versuche es erneut!"))


        # Wenn das Ergebnis stimmt
        if eingabe == ergebnis:
            print("Hurra! Das war richtig!")
            break

        else :
            if eingabe > ergebnis:
                print("Leider falsch! Die Zahl ist kleiner!")

            else:
                print("Leider falsch! Die Zahl ist größer!")

            versuche -= 1  # Zählt um 1 runter
            print("Versuche übrig:", versuche)

        if versuche == 1:
            if ergebnis < eingabe:
                differenz = eingabe - ergebnis
                print("\nLetzter Versuch! Kleiner Tipp: Die Differenz ist ", differenz)
            else:
                differenz = ergebnis - eingabe
                print("\nLetzter Versuch! Kleiner Tipp: Die Differenz ist ", differenz)

    again = input("\nDu hast leider verloren! \nErneut spielen? (Yes/No)")

    while again not in ["No", "no", "Yes", "yes"]:
        again = input("Ungültige Eingabe! Versuche es erneut =)\nErneut spielen? (Yes/No)")

    if again not in ["yes", "Yes"]:  # ✅ Wenn die Antwort nicht "yes" ist, verlasse die Schleife
        break

print("\nDas war ein Spaß! Vielen Dank und bis zum nächsten Mal!")



