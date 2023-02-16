import csv

# Ouvrir le fichier CSV en mode lecture
with open("actions.csv", "r") as f:

    # Créer un objet lecteur CSV
    reader = csv.reader(f)

    # Ignorer la première ligne (en-tête)
    next(reader)

    # Vérifier chaque ligne du fichier CSV
    for i, row in enumerate(reader):

        # Vérifier que chaque ligne contient 3 colonnes
        if len(row) != 3:
            print(f"Erreur à la ligne {i + 1} : {row}")
            continue

        # Vérifier que la deuxième colonne est un nombre flottant
        try:
            float(row[1])
        except ValueError:
            print(f"Erreur à la ligne {i + 1} : {row[1]} n'est pas un nombre flottant")
            continue

        # Vérifier que la troisième colonne est un pourcentage valide
        if not row[2].endswith("%"):
            print(f"Erreur à la ligne {i + 1} : {row[2]} n'est pas un pourcentage valide")
            continue

        try:
            float(row[2].replace("%", ""))
        except ValueError:
            print(f"Erreur à la ligne {i + 1} : {row[2]} n'est pas un pourcentage valide")
            continue

print("Vérification terminée.")

