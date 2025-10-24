def mostra_risultati(risultati):
    if risultati:
        print("\n--- RISULTATI ---")
        for libro in risultati:
            print(libro)  
    else:
        print("Nessun libro trovato.")
    print()