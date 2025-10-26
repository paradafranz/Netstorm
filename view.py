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
  
# Ottenere Parametro di Ricerca
def get_input_ricerca(tipo_ricerca):
    """Ottiene il parametro di ricerca in base al tipo."""
    parametro = input(f"\n🔎 Inserisci il/l'{tipo_ricerca} da cercare: ")
    return parametro
  
# Mostra risultato di un ricerca
def mostra_risultato(risultati_coppie):
    print("\n--- LIBRERIA COMPLETA ---")
    if not risultati_coppie:
        print("Nessun libro trovato nella libreria.")
        return
    # Scompatta ogni tupla in (libro, autore)
    for i, (libro, autore) in enumerate(risultati_coppie, 1):
        print(f"\n--- Libro {i} ---")

        # Dati del Libro
        print(f"Titolo: {libro.titolo}")
        print(f"ISBN: {libro.isbn}")
        print(f"anno di pubblicazione: {libro.annoP}")
        print(f"descrizione: {libro.descrizione}")
        
        # Dati dell'Autore (recuperati dalla tupla)
        print("\n--- Autore ---")
        print(f"Nome: {autore.nome}")
        print(f"Cognome: {autore.cognome}")
      
# Ottenere ISBN per rimozione di un Libro
def get_input_isbn_rimuovi():
    return input("🔎 Inserisci l'ISBN del libro da eliminare: ")
  
# Messaggi Generici
def mostra_messaggio(messaggio):
    print(f"\n[INFO] {messaggio}")
