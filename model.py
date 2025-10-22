class Libro:
    def __init__(self, titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.autore = autore  # Oggetto Autore

    def __str__(self):
        return f"Titolo: {self.titolo}, ISBN: {self.isbn}, Autore: {self.autore.nome}"

class Autore:
    def __init__(self, nome, bio=""):
        self.nome = nome
        self.bio = bio

    def __str__(self):
        return f"{self.nome} - {self.bio}"