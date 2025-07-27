import numpy as np

def inverse_roulette_selection(values, k=1):
    values = np.array(values, dtype=float)
    
    # Prevent division by zero by adding a small epsilon
    epsilon = 1e-6
    inverse_values = 1 / (values + epsilon)
    
    # Normalize to get probabilities
    probabilities = inverse_values / np.sum(inverse_values)
    
    # Select k elements based on the inverse probabilities
    selected_indices = np.random.choice(len(values), size=k, p=probabilities, replace=False)
    return int(selected_indices[0]), int(selected_indices[1])

def natural_selection(fitness_scores, population_size):
    selections = []

    while len(selections) < population_size:
        selections.append(inverse_roulette_selection(fitness_scores, k=2))

    return selections

# Example usage:
if __name__ == "__main__":
    fitness_scores = [100000, 80000, 30000, 10000, 5000, 1000]
    selected = natural_selection(fitness_scores, 5)
    print("Selected indices:", selected)
