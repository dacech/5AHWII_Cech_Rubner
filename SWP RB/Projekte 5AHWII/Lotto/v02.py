
import random

# Liste mit 1-45 (Index 0 - 44)
liste = list(range(1, 46))

# Methode, um 2 Indizes zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("Ungültige Indexpositionen")

# Methode für Zufallszahl innerhalb eines Bereichs
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# Ziehe 6 Zahlen
for i in range(6):
    zufallszahl = generiere_zufallszahl(i, 44)
    vertausche_zwei_index(liste, zufallszahl, 44 - i)


letzte_sechs_zahlen = sorted(liste[-6:])
print(letzte_sechs_zahlen)