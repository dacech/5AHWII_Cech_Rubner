
import random

# liste mit 1-45 (index 0 - 44)
liste = list(range(1, 46))


# methode, um 2 indexe zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("Ungültige Indexpositionen")


# methode für index (range ändert sich mit ziehung 1-6)
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# method test
# vertausche_zwei_index(liste, 0, 2)
# print(liste)

# zufallszahl = generiere_zufallszahl(0, 45)
# print(zufallszahl)

zufallszahl1 = generiere_zufallszahl(0, 44)
vertausche_zwei_index(liste, zufallszahl1, 44)

zufallszahl2 = generiere_zufallszahl(0, 43)
vertausche_zwei_index(liste, zufallszahl2, 43)

zufallszahl3 = generiere_zufallszahl(0, 42)
vertausche_zwei_index(liste, zufallszahl3, 42)

zufallszahl4 = generiere_zufallszahl(0, 41)
vertausche_zwei_index(liste, zufallszahl4, 41)

zufallszahl5 = generiere_zufallszahl(0, 40)
vertausche_zwei_index(liste, zufallszahl5, 40)

zufallszahl6 = generiere_zufallszahl(0, 39)
vertausche_zwei_index(liste, zufallszahl6, 39)

letzte_sechs_zahlen = liste[39:45]
letzte_sechs_zahlen.sort()
print(letzte_sechs_zahlen)
