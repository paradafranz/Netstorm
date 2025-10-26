import psycopg2
from model import *
from view import *
def connect():
    try:
        conn = psycopg2.connect(
            dbname="libreria",
            user="neondb_owner",
            password="npg_pQY5cUiEmLR0",
            host="ep-hidden-firefly-adjdaprl-pooler.c-2.us-east-1.aws.neon.tech",
            port="5432"
        )
        print("Connessione riuscita")
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print("Errore di connessione:", e)
        return 

conn, cur = connect()

def salva_libro(libro: Libro):
   try:
        # Controllo ISBN esistente (Logica DB)
        cur.execute("SELECT isbn FROM libro WHERE isbn = %s", (libro.get_isbn(),))
        if cur.fetchone():
            return "EXISTS" 
            
        # Inserimento Libro
        cur.execute(
            "INSERT INTO libro (isbn, titolo, annop, descrizione) VALUES (%s, %s, %s, %s)",
            (libro.get_isbn(), libro.get_titolo(), libro.get_annoP(), libro.get_descrizione()) 
        )
        conn.commit()
        return "SUCCESS"
        
   except Exception as e:
        conn.rollback()
        
def salva_autore(autore: Autore):
    try:
        cur.execute("SELECT codice FROM autore WHERE nome = %s AND cognome = %s",
                    (autore.get_nome().lower(), autore.get_cognome().lower()))
        autore_esistente = cur.fetchone()

        if autore_esistente:
            codice = autore_esistente[0]
        else:
            # Inserimento di un NUOVO AUTORE
            cur.execute("INSERT INTO autore (nome, cognome) VALUES (%s, %s) RETURNING codice",
                        (autore.get_nome().lower(), autore.get_cognome().lower()))
            codice = cur.fetchone()[0] 
            
        # RITORNO IL CODICE, MA NON FACCIO IL COMMIT QUI.
        return codice 
    except Exception as e:
        conn.rollback()

def aggiungi_scritto(isbn, codice):
    try:
        cur.execute("SELECT * FROM scritto WHERE isbn = %s AND codice = %s", (isbn, codice))
        if cur.fetchone():
            return "EXISTS" 

        cur.execute("INSERT INTO scritto (isbn, codice) VALUES (%s, %s)", (isbn, codice))
        conn.commit()
        return "SUCCESS"
    except Exception as e:
        conn.rollback()
    
def cerca_libri_per_titolo(titolo):
    if not titolo:
        return "PARAMETRO_VUOTO", [] 
    try:
        # Trova tutti i libri con quel titolo
        cur.execute("SELECT isbn, titolo, annop, descrizione FROM libro WHERE titolo LIKE %s", 
                     ('%' + titolo + '%',))
        righe_libri = cur.fetchall() 

        if not righe_libri:
            return "NESSUN_LIBRO", []
            
        risultati_coppie = []
        for riga in righe_libri:
            isbn_corrente = riga[0]
            
            # TROVA L'AUTORE DI QUESTO SPECIFICO LIBRO
            cur.execute("""
                SELECT a.nome, a.cognome FROM autore a
                JOIN scritto s ON a.codice = s.codice
                WHERE s.isbn = %s LIMIT 1
            """, (isbn_corrente,))
            autore_dati = cur.fetchone()
            
            # Costruisci l'oggetto Autore per questo specifico libro
            if autore_dati:
                # Se l'autore è stato trovato, usa i suoi dati
                autore_corrente = Autore(nome=autore_dati[0], cognome=autore_dati[1])
            else:
                # Altrimenti, usa il valore di default per gestire i casi in cui l'autore non sia collegato
                autore_corrente = Autore(nome="Sconosciuto", cognome="")
            
            libro = Libro(riga[0], riga[1], riga[2], riga[3])
            
            
            risultati_coppie.append((libro, autore_corrente))
        
        
        return "SUCCESSO", risultati_coppie 
        
    except Exception as e:
        return "ERRORE_DB", str(e)

def visualizza_libri_per_autore(autore):
    try:
        # Trova il codice dell'autore
        cur.execute("SELECT codice FROM autore WHERE nome = %s AND cognome = %s",
                    (autore.get_nome().lower(), autore.get_cognome().lower()))
        ex_autore = cur.fetchone()
        
        if ex_autore is None:
            return "AUTORE_NON_TROVATO", []
        
        codice = ex_autore[0]
        # Trova tutti i libri scritti da quell'autore
        cur.execute("""
            SELECT l.isbn, l.titolo, l.annop, l.descrizione
            FROM libro l
            JOIN scritto s ON l.isbn = s.isbn
            WHERE s.codice = %s
            ORDER BY l.titolo
        """, (codice,))
        righe_libri = cur.fetchall() 
        
        if not righe_libri:
            return "NESSUN_LIBRO", []
            
        risultati_coppie = []
        for riga in righe_libri: 
            libro = Libro(riga[0], riga[1], riga[2], riga[3]) 
            
            risultati_coppie.append((libro, autore)) 
            
        return "SUCCESSO", risultati_coppie 
        
    except Exception as e:
        return "ERRORE_DB", str(e)

def cerca_libro_per_isbn(isbn_str): 
    if not isbn_str:
        return "PARAMETRO_VUOTO", [] 
    try:
        isbn = int(isbn_str)
    except ValueError:
        return "ISBN_NON_NUMERICO", [] 

    try:
        cur.execute("""
                    SELECT 
                        l.isbn, l.titolo, l.annop, l.descrizione,
                        a.nome, a.cognome
                    FROM libro l
                    LEFT JOIN scritto s ON l.isbn = s.isbn
                    LEFT JOIN autore a ON s.codice = a.codice
                    WHERE l.isbn = %s
                    LIMIT 1
                """, (isbn,))
        riga = cur.fetchone()
        risultato = []
        if riga is None:
            return "NESSUN_LIBRO", [] 
        autore_nome = riga[4]
        autore_cognome = riga[5]

        # Gestisce i casi in cui i campi Autore sono NULL
        autore = Autore(autore_nome,autore_cognome)
        # Costruzione del singolo oggetto Libro
        libro= Libro(riga[0], riga[1], riga[2], riga[3])
        risultato.append((libro,autore))
        
        return "SUCCESSO", risultato
        
    except Exception as e:
        return "ERRORE_DB", str(e)
    
def rimuovi_libro_per_isbn(isbn_str):
    # Controllo base dell'input (ISBN)
    if not isbn_str:
        return "PARAMETRO_VUOTO"
    try:
        # Assumiamo che l'ISBN debba essere un intero per la query
        isbn = int(isbn_str) 
    except ValueError:
        return "ISBN_NON_NUMERICO"

    try:
        # Verifica l'esistenza del libro
        cur.execute("SELECT isbn FROM libro WHERE isbn = %s", (isbn,))
        if cur.fetchone() is None:
            return "NON_TROVATO"
            
        # Elimina prima la relazione (scritto) per vincoli di integrità
        cur.execute("DELETE FROM scritto WHERE isbn = %s", (isbn,))
        
        # Elimina il libro
        cur.execute("DELETE FROM libro WHERE isbn = %s", (isbn,))
        
        conn.commit()
        return "SUCCESSO"
        
    except Exception as e:
        conn.rollback()
        # Ritorna l'errore completo per il debug
        return "ERRORE_DB", str(e)
   
def visualizza_tutti_libri():
    try:
        cur.execute("SELECT isbn, titolo, annop, descrizione FROM libro ORDER BY titolo")
        righe_libri = cur.fetchall()
        
        if not righe_libri:
            return "NESSUN_LIBRO", []
            
        risultati_coppie = [] 
        
        for riga in righe_libri:
            isbn_corrente = riga[0]
            
            # Trova l'autore per questo specifico ISBN
            cur.execute("""
                SELECT a.nome, a.cognome FROM autore a
                JOIN scritto s ON a.codice = s.codice
                WHERE s.isbn = %s LIMIT 1
            """, (isbn_corrente,))
            autore_dati = cur.fetchone()

            if autore_dati:
                autore_corrente = Autore(nome=autore_dati[0], cognome=autore_dati[1])
            else:
                autore_corrente = Autore(nome="Sconosciuto", cognome="")
            
            libro = Libro(riga[0], riga[1], riga[2], riga[3])
            
            # Aggiungi la coppia (Libro, Autore) alla lista dei risultati
            risultati_coppie.append((libro, autore_corrente))
            
        # 3. Restituisci la lista di coppie come secondo parametro
        return "SUCCESSO", risultati_coppie
        
    except Exception as e:
        return "ERRORE_DB", str(e)
