from view import *
from repository import *
from model import *
 
def inserisci_libro():
    risultato = get_input_nuovo_libro() 
    if risultato is None:
        mostra_messaggio("Inserimento annullato o dati non validi.")
        return
    libro_obj, dati_autori = risultato 
    
    try:
        # Inserimento Libro
        risultato_salvataggio = salva_libro(libro_obj) 
        
        if risultato_salvataggio == "EXISTS":
            mostra_messaggio(f"Libro con ISBN {libro_obj.get_isbn()} già presente.")
            return
        elif risultato_salvataggio == "ERROR_DB":
            mostra_messaggio("Errore DB durante il salvataggio del libro.")
            return

        # Inserimento Autori e Collegamento
        for autore in dati_autori:
            codice_autore = salva_autore(autore) 

            # Repository: collega il libro all'autore (senza commit)
            aggiungi_scritto(libro_obj.get_isbn(), codice_autore)
            
        conn.commit() 
        
        mostra_messaggio("Libro e autori inseriti correttamente!")

    except Exception as e:
        conn.rollback() 
        mostra_messaggio(f"Errore DB durante il salvataggio autori/scritto: {e}")

def ricerca_per_titolo():
    titolo = get_input_ricerca('titolo')

    codice_stato, risultati_coppie = cerca_libri_per_titolo(titolo)

    if codice_stato == "SUCCESSO":
        
        mostra_risultato(risultati_coppie)
    elif codice_stato == "NESSUN_LIBRO":
        mostra_messaggio(f"Nessun libro trovato con titolo simile a '{titolo}'.")
    elif codice_stato == "PARAMETRO_VUOTO":
        mostra_messaggio("Errore: Il titolo da cercare non può essere vuoto.")
    else: 
        mostra_messaggio(f"Errore di sistema durante la ricerca per titolo: {risultati_coppie}")

def ricerca_per_autore():
    nome=get_input_ricerca("nome dell'autore")
    cognome=get_input_ricerca("cognome dell'autore")

    autore = Autore(nome,cognome)
    
    codice_stato, libro = visualizza_libri_per_autore(autore)
    
    if codice_stato == "SUCCESSO":
        mostra_risultato(libro)
    elif codice_stato == "AUTORE_NON_TROVATO":
        mostra_messaggio(f"Autore '{nome} {cognome}' non trovato nel database.")
    elif codice_stato == "NESSUN_LIBRO":
        mostra_messaggio(f"Autore '{nome} {cognome}' trovato, ma non ha libri associati.")
    else: 
        mostra_messaggio(f"Errore di sistema durante la ricerca: {libro}")

def ricerca_per_isbn():
    isbn_str = get_input_ricerca('ISBN')
    
    
    codice_stato, libro= cerca_libro_per_isbn(isbn_str)
    
    if codice_stato == "SUCCESSO":
        mostra_risultato(libro) 
    elif codice_stato == "NESSUN_LIBRO":
        mostra_messaggio(f"Nessun libro trovato con ISBN '{isbn_str}'.")
    elif codice_stato == "ISBN_NON_NUMERICO":
        mostra_messaggio("Errore: L'ISBN deve essere composto solo da numeri.")
    elif codice_stato == "PARAMETRO_VUOTO":
        mostra_messaggio("Ricerca annullata: ISBN non inserito.")
    else: 
        mostra_messaggio(f"Errore di sistema durante la ricerca per ISBN: {libro}")
def rimuovi_libro():
 
    isbn_str = get_input_isbn_rimuovi() 

    if not isbn_str:
        mostra_messaggio("Operazione annullata.")
        return
        
   
    codice_stato = rimuovi_libro_per_isbn(isbn_str)
    
    
    if codice_stato == "SUCCESSO":
        mostra_messaggio(f"Libro con ISBN {isbn_str} eliminato con successo.")
    elif codice_stato == "NON_TROVATO":
        mostra_messaggio(f"Nessun libro trovato con ISBN {isbn_str}.")
    elif codice_stato == "ISBN_NON_NUMERICO":
        mostra_messaggio("Errore: L'ISBN deve essere composto solo da numeri.")
    elif codice_stato == "PARAMETRO_VUOTO":
        mostra_messaggio("Errore: ISBN non inserito.")
    else: 
        mostra_messaggio(f"Errore DB durante l'eliminazione: {codice_stato}")
def visualizza_libreria():
   
    codice_stato, risultati_libri = visualizza_tutti_libri()
    
    if codice_stato == "SUCCESSO":
        
        mostra_risultato(risultati_libri)
        
    elif codice_stato == "NESSUN_LIBRO":
        mostra_messaggio("Nessun libro presente nella libreria.")
        
    else: 
        mostra_messaggio(f"Errore di sistema durante la visualizzazione: {risultati_libri}")

def menu():
    while True:
        scelta = mostra_menu_e_ottieni_scelta()
        match scelta :
            case "1":
                inserisci_libro()
            case "2":
                ricerca_per_titolo()
            case "3":
                ricerca_per_autore()
            case "4":
                ricerca_per_isbn()
            case "5":
                rimuovi_libro()
            case "6":
                visualizza_libreria()
            case "X"| "x":
                break
            case _:
                print("Scelta non valida, riprova.\n")

menu()
