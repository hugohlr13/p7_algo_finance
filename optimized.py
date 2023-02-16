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

# Mesurer le temps de calcul
start_time = time.time()

# Trier les actions par ordre de bénéfice décroissant
actions_triees = sorted(actions, key=lambda action: action[2], reverse=True)

# Initialiser les tableaux des résultats partiels et finaux
resultats_partiels = [0] * (500 + 1)
resultats_finaux = [0] * (500 + 1)

# Parcourir toutes les actions triées
for action in actions_triees:
    cout_action = int(action[1])
    benefice_action = action[2]

    # Mettre à jour les résultats partiels et finaux
    for i in range(cout_action, 500 + 1):
        nouveau_benefice = resultats_partiels[i - cout_action] + benefice_action
        if nouveau_benefice > resultats_partiels[i]:
            resultats_partiels[i] = nouveau_benefice
            resultats_finaux[i] = (resultats_finaux[i - cout_action] + [action[0]])

# Afficher la meilleure combinaison et le meilleur profit
print("Meilleure combinaison :")
for action in resultats_finaux[-1]:
    print(action)
print("Meilleur profit après 2 ans (%) :", round(resultats_partiels[-1] * 100, 2))

# Afficher le temps de calcul
print(f"Temps de calcul : {round(time.time() - start_time, 2)} secondes")
