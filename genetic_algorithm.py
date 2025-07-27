import numpy as np
from dataset.init_schedule import ScheduleMaker
from genetic_algorithm_utils.crossover import Crossover
from genetic_algorithm_utils.fitness import fitness
from genetic_algorithm_utils.natural_selection import natural_selection
from genetic_algorithm_utils.mutation import swap_mutation

class GeneticAlgorithm:

    @staticmethod
    def init_population(pop_size: int):
        # Helper function to initialize the population
        def contains(target, population):
            return any(np.array_equal(target, element) for element in population)
        
        sch_maker = ScheduleMaker()     
        population = []

        while len(population) < pop_size:
            schedule = sch_maker.generate()

            if not contains(schedule, population):
                population.append(schedule)

        return population
    
    def __init__(self, pop_size, min_allowed_portion, max_allowed_portion, mutation_rate):
        self.student_data = np.loadtxt('csv/students.csv', delimiter=',', dtype=int)
        self.population = GeneticAlgorithm.init_population(pop_size)
        self.crossover = Crossover(min_allowed_portion, max_allowed_portion)
        self.fitness_scores = []
        self.mutation_rate = mutation_rate      # NOTE: mutation_rate out of 1000

    def evaluate_fitness(self):
        print("\nEvaluating fitness...")
        self.fitness_scores.clear()
        
        for i, schedule in enumerate(self.population):
            print()
            print(f"************** SCHEDULE {i+1} **************")
            self.fitness_scores.append(fitness(self.student_data, schedule))

        with open("fitness_log.txt", "a") as file:
            file.write(str(self.fitness_scores) + "\n")

    def produce_children(self):
        new_population = []
        for i1, i2 in natural_selection(self.fitness_scores, len(self.population)):
            child = self.crossover.make_child(self.population[i1], self.population[i2])
            swap_mutation(child, chance=self.mutation_rate)    
            new_population.append(child)

        # Replace the old population witht the new
        self.population = new_population

        print("Population updated with new children.")

    def iterate_and_evolve(self, goal_fitness, max_iteration):

        # Make a log life to keep track of the fitness scores
        file = open("fitness_log.txt", "w")
        file.close()

        iteration = 1

        print("===========================================================")
        print(f"                  ITERATION {iteration}")
        print("===========================================================")

        # 1. Evaluate fitness
        self.evaluate_fitness()

        while iteration <= max_iteration and min(self.fitness_scores) > goal_fitness:
            
            

            # 2. Check if the fitness reached its goal
            if min(self.fitness_scores) <= goal_fitness:
                print(f"GOAL FITNESS REACHED!  Iterations: {iteration}")
                break
            else:
                print(f"Minimum fitness failed to reach {goal_fitness}. Evolving...")

            #   3. Otherwise replace the population with new children
                self.produce_children()

                iteration += 1
                print("===========================================================")
                print(f"                  ITERATION {iteration}")
                print("===========================================================")
                self.evaluate_fitness()

            

        chosen_index = self.fitness_scores.index(min(self.fitness_scores))
        return self.population[chosen_index]
    
if __name__ == "__main__":
    genetic = GeneticAlgorithm(4, 40, 60, 5)
    schedule = genetic.iterate_and_evolve(1000, 100)

