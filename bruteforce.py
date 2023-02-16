import csv
import itertools

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

# Parcourir toutes les combinaisons possibles
for i in range(1, 21):
    for combinaison in itertools.combinations(actions, i):
        cout_total = sum(action[1] for action in combinaison)
        if cout_total <= 500:
            benefice_total = sum(action[1] * action[2] for action in combinaison)
            if benefice_total > meilleur_profit:
                meilleur_profit = benefice_total
                meilleure_combinaison = combinaison

# Afficher la meilleure combinaison et le meilleur profit
print("Meilleure combinaison :")
for action in meilleure_combinaison:
    print(action[0])
print("Meilleur profit :", meilleur_profit)



