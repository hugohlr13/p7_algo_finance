import csv
import time

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

for action in actions:
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

# Afficher la meilleure combinaison et le meilleur profit
print("Meilleure combinaison :")
for action in meilleure_combinaison:
    print(action)
print("Meilleur profit après 2 ans (%):", round(meilleur_profit, 2))

# Afficher le temps de calcul
print(f"Temps de calcul : {round(time.time() - start_time, 2)} secondes")


