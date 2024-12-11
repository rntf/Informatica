from csv import reader, writer

def main():
    file_processato = False
    while not file_processato:
        try:
            input_file_name = input("Introduci il nome del file da leggere: ")
            output_file_name = input("Introduci il nome del file da scrivere: ")
            processa_file(input_file_name, output_file_name)
            file_processato = True
        except OSError:
            print(f"Il file {input_file_name} non esiste")
        except ValueError as errore:
            print("Errore nei dati in input")
            print(errore)
        except RuntimeError as errore3:
            print(f"Il database contiene un film vietato: {errore3}")
        except Exception as errore2:
            print(errore2)

def processa_file(input_file_name, output_file_name):
    # apro i due file
    # leggo ogni riga del primo file
    #   se corrisponde ai criteri, scrivo la riga nel secondo file
    # chiudo i file

    try:
        input_file = open(input_file_name, "r", encoding="utf-8", newline="")
        output_file = open(output_file_name, "w", encoding="utf-8", newline="")

        csv_reader = reader(input_file)
        csv_writer = writer(output_file)

        # gestisco l'intestazione del file a parte
        next(csv_reader)

        for riga in csv_reader:
            anno = int(riga[1])
            titolo = riga[0]
            if titolo == "American Beauty":
                raise RuntimeError(titolo)
            if 1990 <= anno <= 1999:
                csv_writer.writerow([riga[0], anno, riga[4]])
    
    finally: 
        input_file.close()
        output_file.close()
    return

main()