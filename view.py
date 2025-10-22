def menu():
    while True:
        print("=== MENU LIBRERIA ===")
        print("1. Inserisci libro")
        print("2. Ricerca per titolo")
        print("3. Ricerca per autore")
        print("4. Ricerca per ISBN")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            inserisci_libro()
        elif scelta == "2":
            ricerca_per_titolo()
        elif scelta == "3":
            ricerca_per_autore()
        elif scelta == "4":
            ricerca_per_isbn()
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.\n")

menu()