import random
import matplotlib.pyplot as plt

# Initialisiere Statistik und mögliche Zahlen
dict_ziehungen_statistic = {i: 0 for i in range(1, 46)}  # Dic mit Zahlen 1-45 und Anz (0)


# Methode, um 2 Indizes zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]


# Methode für Zufallszahl innerhalb eines Bereichs
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)


def lottoziehung():
    # Liste mit 1-45 (Index 0 - 44)
    liste = list(range(1, 46))

    # Ziehe 6 Zahlen durch zufälliges Tauschen
    for i in range(6):
        zufallszahl = generiere_zufallszahl(0, 44 - i)  # Zufallsindex aus dem Bereich 0 bis (44 - i)
        vertausche_zwei_index(liste, zufallszahl, 44 - i)  # Tausche die gezogene Zahl mit der letzten in der Liste

    # Sortiere die letzten 6 Zahlen, um Konsistenz zu gewährleisten
    letzte_sechs_zahlen = sorted(liste[-6:])
    return letzte_sechs_zahlen


def lottoziehung_statistic(anzahl_ziehungen):
    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        for zahl in ziehung:
            dict_ziehungen_statistic[zahl] += 1     #zahl = key
    return dict_ziehungen_statistic

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! vllt noch main() programmieren !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Führe 100.000 Ziehungen durch
data = lottoziehung_statistic(100000)

# Plot der Ergebnisse
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots()
axs.bar(names, values)
fig.suptitle('Lottoziehungen Statistik')
axs.set_ylabel('Anzahl der gezogenen Zahlen')
axs.set_xlabel('Mögliche Zahlen')

plt.show()
