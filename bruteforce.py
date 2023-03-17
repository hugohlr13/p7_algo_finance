import csv
import itertools
import time
import psutil
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Read the file containing the information on the actions
with open("actions.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # sauter la première ligne
    actions = list(reader)

# Convert costs and benefits to floating numbers
for action in actions:
    action[1] = float(action[1])
    action[2] = float(action[2])

best_profit = 0
best_combination = []

# Measuring the computing time
start_time = time.time()

# Measuring RAM usage
memory_usage = [psutil.Process().memory_info().rss]

# Browse all possible combinations
for i in tqdm(range(1, len(actions) + 1)):
    for combination in itertools.combinations(actions, i):
        total_cost = sum(action[1] for action in combination)
        if total_cost <= 500:
            total_profit = sum(action[1] * (action[2]/100) for action in combination)
            if total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    # Measure RAM usage and elapsed time
    memory_usage.append(psutil.Process().memory_info().rss)

# Create a time sequence in seconds corresponding to the number of iterations of the algorithm
time_seq = np.arange(len(memory_usage)) * (time.time() - start_time) / len(memory_usage)

# Display the best combination and the best profit
print("Meilleure combinaison :")
for action in best_combination:
    print(action[0])
print("Bénéfice de la combinaison :", round(best_profit, 2))

# Display the calculation time
print(f"Temps d'exécution : {round(time.time() - start_time, 2)} secondes")

# Display the memory usage curve
plt.plot(time_seq, memory_usage)
plt.title("Courbe d'utilisation de la mémoire vive")
plt.xlabel("Temps (secondes)")
plt.ylabel("Mémoire utilisée (octets)")
plt.show()
