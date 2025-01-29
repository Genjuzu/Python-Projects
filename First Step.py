import os


def clear_screen():
    """
    Löscht den Bildschirm, abhängig vom Betriebssystem.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Benutzereingaben sammeln
    name = input("Hallo! Wie ist dein Name? ")
    city = input("Vielen Dank! Und aus welcher Stadt kommst du? ")

    # Fehlerbehandlung für das Alter
    while True:
        try:
            age = int(input("Super! Und wie alt bist du? "))
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")

    jahr = 2025 - age  # Optional: Dynamisches Jahr verwenden

    # Bildschirm löschen nach Eingaben
    clear_screen()

    # Ausgabe mit Absätzen
    print("\n\nGuten Tag", name + "diggah", "\n\nDu kommst aus", city + "-City", "\n\nDu bist Jahrgang: ", jahr)


if __name__ == "__main__":
    main()
