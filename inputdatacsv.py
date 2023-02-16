import csv

# Données à écrire dans le fichier CSV
data = [
    ["Action-1", 20.00, "5%"],
    ["Action-2", 30.00, "10%"],
    ["Action-3", 50.00, "15%"],
    ["Action-4", 70.00, "20%"],
    ["Action-5", 60.00, "17%"],
    ["Action-6", 80.00, "25%"],
    ["Action-7", 22.00, "7%"],
    ["Action-8", 26.00, "11%"],
    ["Action-9", 48.00, "13%"],
    ["Action-10", 34.00, "27%"],
    ["Action-11", 42.00, "17%"],
    ["Action-12", 110.00, "9%"],
    ["Action-13", 38.00, "23%"],
    ["Action-14", 14.00, "1%"],
    ["Action-15", 18.00, "3%"],
    ["Action-16", 8.00, "8%"],
    ["Action-17", 4.00, "12%"],
    ["Action-18", 10.00, "14%"],
    ["Action-19", 24.00, "21%"],
    ["Action-20", 114.00, "18%"],
]

# Ouvrir le fichier CSV en mode écriture
with open("actions.csv", "w", newline="") as f:

    # Créer un objet écrivain CSV
    writer = csv.writer(f)

    # Écrire les en-têtes de colonnes dans le fichier CSV
    writer.writerow(["Actions", "Cout", "Benefice"])

    # Écrire les données dans le fichier CSV
    for row in data:
        writer.writerow(row)

print("Fichier CSV créé avec succès.")
