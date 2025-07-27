import random
import numpy as np

DEBUG = False

class Crossover:

    def __init__(self, min_allowed_portion, max_allowed_portion):
        self.min_allowed_portion = min_allowed_portion
        self.max_allowed_portion = max_allowed_portion

    def select_segment(self, parent_size, start, seg_size):
        # segment_size = round(len(flattened_parentA) * portion / 100)
        return [i % parent_size for i in range(start, start + seg_size)]
    
    def select_random_spots(self, parent_size, number_of_elements):
        
        selections = set()
        while len(selections) < number_of_elements:
            selections.add(random.randint(0, parent_size - 1))

        return list(selections)
    
    def make_child_no_rand(self, parentA, parentB, selections):

        A = parentA.flatten()
        B = parentB.flatten()

        # Select segment
        inverse_range = [i for i in range(len(A)) if i not in selections]

        child = np.zeros((len(B)))

        for i in selections:
            child[i] = A[i]

        if DEBUG: print(child)

        i = 0
        for num in B:
            if num not in child:
                child[inverse_range[i]] = num
                i += 1

        

        if DEBUG: print(child)

        child = child.reshape(parentA.shape)
        return child
    
    def make_child(self, parentA, parentB):
        parent_size = len(parentA.flatten())
        portion = random.randint(self.min_allowed_portion, self.max_allowed_portion)
        number_of_elements = round(parent_size * portion / 100)

        # Choose between segment selection and random spots
        if random.getrandbits(1):
            selections = self.select_random_spots(parent_size, number_of_elements)
        else:
            selections = self.select_segment(parent_size, random.randint(0, parent_size - 1), number_of_elements)

        return self.make_child_no_rand(parentA, parentB, selections)


if __name__ == "__main__":
    # Create a sample 2D NumPy array
    A = np.array(list(range(1, 21)))
    A = A.reshape((4, 5))

    B = A.flatten().copy()
    np.random.shuffle(B)
    B = B.reshape((4, 5))

    print(A)
    print(B)

    crossover = Crossover(40, 60)
    child = crossover.make_child(A, B)

    print(child)
    