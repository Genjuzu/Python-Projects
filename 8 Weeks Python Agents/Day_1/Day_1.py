import os

# Bildschirm leeren für Windows oder Linux/macOS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Nutzer nach Name & Alter fragen
name = input("What's your name? ")
age = int(input("How old are you? "))
days_age = age * 365

# Bildschirm leeren & Begrüßung ausgeben
clear_screen()
print(f"\nHello {name}!\nYou are {days_age} days old.")

# Nutzer fragen, ob eine Berechnung gewünscht ist
answer = input("\nWould you like to calculate something? (yes/no)\n").strip().lower()

# Ungültige Eingaben erneut abfragen
while answer not in ["yes", "no"]:
    answer = input("Wrong input! Please enter 'yes' or 'no': ").strip().lower()

# Hauptschleife für Berechnungen
while answer == "yes":
    # Eingabe der Zahlen
    number_1 = int(input("Okay! Please enter the first number: "))
    number_2 = int(input("Thank you! Please enter a second number: "))

    # Nutzereingabe für die Operation
    operations = input("What operation do you choose?\n1) Addition\n2) Subtraction\n3) Division\n4) Multiplication\n\n[Choose by number]: ").strip()

    # Ungültige Eingaben erneut abfragen
    while operations not in ["1", "2", "3", "4"]:
        operations = input("Wrong input! Please try again. Choose 1, 2, 3, or 4: ").strip()

    # Berechnung durchführen
    if operations == "1":
        result = number_1 + number_2
    elif operations == "2":
        result = number_1 - number_2
    elif operations == "3":
        # Fehler abfangen, falls der Nutzer durch 0 teilt
        if number_2 == 0:
            result = "Error! Division by zero is not allowed."
        else:
            result = number_1 / number_2
    elif operations == "4":
        result = number_1 * number_2

    # Ergebnis ausgeben
    print(f"Das Ergebnis lautet: {result}")

    # Nutzer fragen, ob er weitermachen möchte
    answer = input("Try again? (yes/no): ").strip().lower()

    # Ungültige Eingaben erneut abfragen
    while answer not in ["yes", "no"]:
        answer = input("Wrong input! Please enter 'yes' or 'no': ").strip().lower()

# Abschlussmeldung
print("\nOkay! Enjoy your day! 😊")
