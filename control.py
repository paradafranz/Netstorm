# menu che gestisce ricerca libro (per autore, titolo e isbn) post ricerca stampa libri, 
# inserimento libri



libri = []  

def inserisci_libro():
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    isbn = input("Inserisci l'ISBN: ")
    libro = {"titolo": titolo, "autore": autore, "isbn": isbn}
    libri.append(libro)
    print("Libro inserito con successo!\n")

def ricerca_per_titolo():
    titolo = input("Inserisci il titolo da cercare: ")
    risultati = [l for l in libri if l["titolo"].lower() == titolo.lower()]
    stampa_risultati(risultati)

def ricerca_per_autore():
    autore = input("Inserisci l'autore da cercare: ")
    risultati = [l for l in libri if l["autore"].lower() == autore.lower()]
    stampa_risultati(risultati)

def ricerca_per_isbn():
    isbn = input("Inserisci l'ISBN da cercare: ")
    risultati = [l for l in libri if l["isbn"] == isbn]
    stampa_risultati(risultati)

def stampa_risultati(risultati):
    if risultati:
        print("\n--- RISULTATI ---")
        for libro in risultati:
            print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, ISBN: {libro['isbn']}")
    else:
        print("Nessun libro trovato.")
    print()

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
