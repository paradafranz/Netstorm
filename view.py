from model import *
def mostra_menu_e_ottieni_scelta():
    """Mostra il menu all'utente e restituisce l'opzione scelta (stringa)."""
    print("\n=== 📚 MENU LIBRERIA ===")
    print("1. Inserisci nuovo libro")
    print("2. Ricerca per titolo")
    print("3. Ricerca per autore")
    print("4. Ricerca per ISBN") 
    print("5. Rimuovi libro per ISBN")
    print("6. Visualizza la Libreria")
    print("X. Esci")
    
    scelta = input("👉 Scegli un'opzione: ")
    return scelta
# Ottenere Dati per Inserimento
def get_input_nuovo_libro():
    print("\n--- INSERIMENTO NUOVO LIBRO ---")
    try:
        isbn = int(input("Inserisci l'isbn del libro: "))
        titolo = input("Inserisci il titolo del libro: ")
        annoP = int(input("Inserisci l'anno di pubblicazione del libro: "))
        descrizione = input("Inserisci la descrizione del libro: ")
        nAutori = int(input("Quanti autori ha questo libro?"))
    except ValueError:
        print("[ERRORE] Input ISBN/Anno/Numero Autori non valido.")
        return None
        
    dati_autori = []
    for i in range(nAutori):
        print(f"--- Dati Autore {i+1} ---")
        nome = input("   Nome autore: ")
        cognome = input("   Cognome autore: ")
        dati_autori.append({"nome": nome, "cognome": cognome})
        
    if not titolo or not dati_autori:
        return None 
    # Crea l'oggetto Libro
    libronew = Libro(isbn, titolo, annoP, descrizione)
    # Restituisce l'oggetto e la lista di dati grezzi degli autori
    return libronew, dati_autori
