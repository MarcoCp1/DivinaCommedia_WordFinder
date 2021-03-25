trova = input("Cosa cerchi?  ")
a =len(trova)
b = len("abc")

if a<b :
    print("Devi inserire una parola o una frase di tre caratteri o più")
    exit()

divina_commedia = open("Inferno.csv" , "r" , encoding="utf-8")
contatore_inferno = 0 
while True :
    testo = divina_commedia.readline()
    if not testo :
        break

    if trova.upper() in testo.upper() : 
        print(testo)
        contatore_inferno = contatore_inferno+1
       
divina_commedia.close()

purgatorio = open("Purgatorio.csv" , "r" , encoding="utf-8")
contatore_purgatorio = 0 
while True :
    testo = purgatorio.readline()
    if not testo :
        break

    if trova.upper() in testo.upper() : 
        print(testo)
        contatore_purgatorio = contatore_purgatorio+1

paradiso = open("Paradiso.csv" , "r" , encoding="utf-8")
contatore_paradiso = 0 
while True :
    testo = paradiso.readline()
    if not testo :
        break

    if trova.upper() in testo.upper() : 
        print(testo)
        contatore_paradiso = contatore_paradiso+1

print("Ho trovato:", trova,"nell' 'Inferno' ", contatore_inferno, "volte")
print("Ho trovato:", trova, "nel 'Purgatorio'", contatore_purgatorio, "volte")
print("Ho trovato:", trova, "nel 'Paradiso'", contatore_paradiso, "volte")

divina_commedia.close()

print("In totale ho trovato" , trova, contatore_inferno+contatore_purgatorio+contatore_paradiso, "volte")
