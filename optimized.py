import csv
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
sac_a_dos = []

# Mesurer le temps de calcul
start_time = time.time()

# Mesurer l'utilisation de la mémoire vive
memory_usage = [psutil.Process().memory_info().rss]

# Mise en place de l'algorithme du sac à dos
for i, action in enumerate(actions):
    # mettre à jour les combinaisons précédentes dans le sac à dos
    nouvelles_combinaisons = []
    for combinaison, cout, benefice in sac_a_dos:
        if cout + action[1] <= 500:
            nouvelles_combinaisons.append((combinaison + [action[0]], cout + action[1], benefice + action[1] * action[2]))
            if benefice + action[1] * action[2] > meilleur_profit:
                meilleur_profit = benefice + action[1] * action[2]
                meilleure_combinaison = combinaison + [action[0]]

    sac_a_dos += nouvelles_combinaisons

    # ajouter l'action courante dans le sac à dos si possible
    if action[1] <= 500:
        sac_a_dos.append(([action[0]], action[1], action[1] * action[2]))
        if action[1] * action[2] > meilleur_profit:
            meilleur_profit = action[1] * action[2]
            meilleure_combinaison = [action[0]]
    
    # Mesurer l'utilisation de la mémoire vive
    memory_usage.append(psutil.Process().memory_info().rss)

# Afficher la meilleure combinaison et le meilleur profit
print("Meilleure combinaison :")
for action in meilleure_combinaison:
    print(action)
print("Meilleur profit après 2 ans (%):", round(meilleur_profit, 2))

# Afficher le temps de calcul
print(f"Temps de calcul : {round(time.time() - start_time, 2)} secondes")

# Créer une séquence de temps en secondes correspondant au nombre d'itérations de l'algorithme
time_seq = np.arange(len(memory_usage)) * (time.time() - start_time) / len(memory_usage)

# Afficher la courbe d'utilisation de la mémoire vive
plt.plot(time_seq, memory_usage)
plt.title("Courbe d'utilisation de la mémoire vive")
plt.xlabel("Temps (secondes)")
plt.ylabel("Mémoire utilisée (octets)")
plt.show()









