import csv


def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        with open(file_path, "r") as f:
            csvReader =csv.reader(f)
            biblioteca = []
            num_sezioni = int(next(csvReader)[0].strip())# salta la prima riga


            for line in csvReader:
                titolo=line[0]
                autore=line[1]
                anno=int(line[2])
                pagine=int(line[3])
                sezione=int(line[4])
                libro={
                    "titolo":titolo,
                    "autore":autore,
                    "anno":anno,
                    "pagine":pagine,
                    "sezione":sezione,
                }
                biblioteca.append(libro)

            return biblioteca
    except FileNotFoundError:
        print("File non trovato.")
        return None




def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    sezioni_valide = {1, 2, 3, 4, 5}
    if sezione not in sezioni_valide:
        print(f" Sezione '{sezione}' non esistente. ")
        return None
    for libro in biblioteca:
        if libro["titolo"].lower() == titolo.lower():
            print(" Libro già presente nella biblioteca.")
            return None
    nuovo_libro={
        "titolo": titolo,
        "autore": autore,
        "anno": anno,
        "pagine": pagine,
        "sezione": sezione,
    }
    biblioteca.append(nuovo_libro)
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            riga = f"{titolo},{autore},{anno},{pagine},{sezione}\n"
            f.write(riga)
    except FileNotFoundError:
        print(f" File non trovato")
        return None


    print(f" Libro '{titolo}' aggiunto con successo!")
    return nuovo_libro



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""


    #se il libro è presente viene restituita una stringa
    for libro in biblioteca:
        if libro["titolo"].lower() == titolo.lower():
            return f"{libro['titolo']}, {libro['autore']}, {libro['anno']}, {libro['pagine']}, sezione {libro['sezione']}"
    return None

    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""

    # TODO
    sezione_valida = {1, 2, 3, 4, 5}

    if sezione not in sezione_valida:
        print(f"Sezione '{sezione}' non esistente.")
        return None

    #crea una nuova lista per sezione
    libri_nella_sezione = []
    for libro in biblioteca :
         if libro["sezione"] == sezione:
             libri_nella_sezione.append(libro["titolo"])
    #gestione sezione vuota
    if not libri_nella_sezione:
        print(f"Nessun libro trovato nella sezione {sezione}.")
        return None

    # Ordina alfabeticamente i libri per titolo
    libri_ordinati = sorted(libri_nella_sezione)

    return libri_ordinati


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

