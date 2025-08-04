import ast
import matplotlib.pyplot as plt

# Reading the fitness function
lists = []
with open("fitness_log.txt", "r") as file:
    for line in file:
        lists.append(ast.literal_eval(line.strip()))

data = [min(scores) for scores in lists]

# Plotting
plt.plot(range(len(data)), data, marker='D')
plt.xlabel("Iteration of Evolution")
plt.ylabel("Minimum Fitness")
plt.title("Minimum Fitness per Iteration")
plt.grid(True)
plt.tight_layout()
plt.show()