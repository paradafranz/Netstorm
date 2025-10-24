def libro_inserito():
    print("Libro inserito con successo!\n")

def mostra_risultati(risultati):
    if risultati:
        print("\n--- RISULTATI ---")
        for libro in risultati:
            print(f"Titolo: {libro['titolo']}, Autore: {libro['autore']}, ISBN: {libro['isbn']}")
    else:
        print("Nessun libro trovato.")
    print()
