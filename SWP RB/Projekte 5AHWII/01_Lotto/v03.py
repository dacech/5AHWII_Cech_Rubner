import random as ran
import matplotlib.pyplot as plt

# Initialisiere Statistik und mögliche Zahlen
dict_ziehungen_statistic = {i: 0 for i in range(1, 46)}  # Zahlen 1-45

def lottoziehung():
    zahlen = list(range(1, 46))  # Erstelle jedes Mal eine neue Liste von 1 bis 45
    gezogene_zahlen = ran.sample(zahlen, 6)  # Ziehe 6 zufällige Zahlen ohne Wiederholung
    return gezogene_zahlen

def lottoziehung_statistic(anzahl_ziehungen):
    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        for zahl in ziehung:
            dict_ziehungen_statistic[zahl] += 1
    return dict_ziehungen_statistic

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
