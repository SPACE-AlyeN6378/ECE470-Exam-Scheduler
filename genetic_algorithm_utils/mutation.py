import random
import numpy as np

DEBUG = True

def swap_mutation(schedule, chance):
    
    rows, cols = schedule.shape
    selections = set()

    # Go through the entire table
    for row in range(rows):
        for col in range(cols):

            # chance is out of 1000
            if random.randint(1, 1000) < chance:
                other_row = random.randint(0, rows-1)
                other_col = random.randint(0, cols-1)

                # Swap it
                schedule[row, col], schedule[other_row, other_col] = schedule[other_row, other_col], schedule[row, col]




if __name__ == "__main__":
    # Create a sample 2D NumPy array
    A = np.array(list(range(1, 21)))
    A = A.reshape((4, 5))

    print(A)

    swap_mutation(A, 100)
    print(A)
