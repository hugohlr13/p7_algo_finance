import csv
import itertools
import time
import psutil
import numpy as np
import matplotlib.pyplot as plt

# Lecture du fichier contenant les informations sur les actions
with open("actions.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # sauter la première ligne
    actions = [row for row in reader]

# Convertir les coûts et bénéfices en nombres flottants
for action in actions:
    action[1] = float(action[1])
    action[2] = float(action[2].replace("%", "")) / 100

meilleur_profit = 0
meilleure_combinaison = []

# Mesurer le temps de calcul
start_time = time.time()

# Mesurer l'utilisation de la mémoire vive
memory_usage = [psutil.Process().memory_info().rss]
time_usage = [0]

# Parcourir toutes les combinaisons possibles
for i in range(1, 21):
    for combinaison in itertools.combinations(actions, i):
        cout_total = sum(action[1] for action in combinaison)
        if cout_total <= 500:
            benefice_total = sum(action[1] * action[2] for action in combinaison)
            if benefice_total > meilleur_profit:
                meilleur_profit = benefice_total
                meilleure_combinaison = combinaison

    # Mesurer l'utilisation de la mémoire vive et le temps écoulé
    memory_usage.append(psutil.Process().memory_info().rss)
    time_usage.append(time.time() - start_time)

# Afficher la meilleure combinaison et le meilleur profit
print("Meilleure combinaison :")
for action in meilleure_combinaison:
    print(action[0])
print("Meilleur profit après 2 ans (%) :", round(meilleur_profit, 2))

# Afficher le temps de calcul
print(f"Temps de calcul : {round(time.time() - start_time, 2)} secondes")

# Afficher la courbe d'utilisation de la mémoire vive
plt.plot(time_usage, memory_usage)
plt.title("Courbe d'utilisation de la mémoire vive")
plt.xlabel("Temps (secondes)")
plt.ylabel("Mémoire utilisée (octets)")
plt.show()


