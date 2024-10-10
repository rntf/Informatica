piano = int(input("A quale piano vuoi andare? "))

if piano < 13: 
    piano_reale = piano
else: 
    piano_reale = piano - 1
    
# alternativa
piano_reale = piano
if piano_reale >= 13:
    piano_reale -= 1

if piano == 13:
    print("errore")

print(f"Ti porto al piano {piano_reale}")