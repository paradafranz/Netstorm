class Libro:
    def __init__(self, isbn, titolo, annoP, descrizione):
        self.isbn = isbn
        self.titolo = titolo
        self.annoP = annoP
        self.descrizione = descrizione
        
    def get_isbn(self):
        return self.isbn

    def get_titolo(self):
        return self.titolo

    def get_annoP(self):
        return self.annoP

    def get_descrizione(self):
        return self.descrizione

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_titolo(self, titolo):
        self.titolo = titolo

    def set_annoP(self, annoP):
        self.annoP = annoP

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    def to_tuple(self):
        return (self.isbn, self.titolo, self.annoP, self.descrizione)

    def __str__(self):
        return f"isbn: {self.isbn},\nTitolo: {self.titolo},\nAnno di Pubblicazione: {self.annoP}, \nDescrizione: {self.descrizione}"

class Autore:
    def __init__(self, nome, cognome, codice=None):
        self.codice=codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"Autore {self.nome} {self.cognome} con codice {self.codice}"
    
    def get_codice(self):
        return self.codice
    
    def get_nome(self):
        return self.nome
    
    def get_cognome(self):
        return self.cognome
    
    def set_codice(self, codice):
        self.codice = codice

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome
