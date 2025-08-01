import numpy as np
from dataset.init_schedule import ScheduleMaker
from genetic_algorithm_utils.crossover import Crossover
from genetic_algorithm_utils.fitness import fitness
from genetic_algorithm_utils.natural_selection import natural_selection
from genetic_algorithm_utils.mutation import spread_mutation

class ExamScheduler:

    def init_population(self, pop_size):
        # Helper function to initialize the population
        def contains(target, population):
            return any(np.array_equal(target, element) for element in population)
        
        sch_maker = ScheduleMaker(self.slots_per_day, self.days)     
        population = []

        while len(population) < pop_size:
            schedule = sch_maker.generate(self.extra_rooms)

            if not contains(schedule, population):
                population.append(schedule)

        return population
    
    def __init__(self, pop_size, slots_per_day, days, extra_rooms, min_allowed_portion, max_allowed_portion, mutation_rate):
        self.extra_rooms = extra_rooms
        self.days = days
        self.slots_per_day = slots_per_day
        self.student_data = np.loadtxt('csv/students.csv', delimiter=',', dtype=int)
        self.population = self.init_population(pop_size)
        self.crossover = Crossover(min_allowed_portion, max_allowed_portion)
        self.fitness_scores = []
        self.conflict_scores = []
        self.mutation_rate = mutation_rate      # NOTE: mutation_rate out of 1000

    def evaluate_fitness(self):
        print("\nEvaluating fitness...")
        self.fitness_scores.clear()
        self.conflict_scores.clear()
        
        for i, schedule in enumerate(self.population):
            print()
            print(f"************** SCHEDULE {i+1} **************")
            conflict, _, penalty = fitness(self.student_data, schedule, self.slots_per_day)
            self.fitness_scores.append(penalty)
            self.conflict_scores.append(conflict)

        with open("fitness_log.txt", "a") as file:
            file.write(str(self.fitness_scores) + "\n")

    def produce_children(self):
        new_population = []
        population_number = 1

        for i1, i2 in natural_selection(self.fitness_scores, len(self.population)):
            print(f"Generating child {population_number}...  ", end="")
            child = self.crossover.make_child(self.population[i1], self.population[i2])
            print("Crossover complete. Performing mutation...  ", end="")
            spread_mutation(child, self.student_data, self.mutation_rate, self.slots_per_day)
             
            new_population.append(child)
            population_number += 1
            print("OK")

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

        while iteration <= max_iteration \
        and min(self.fitness_scores) > goal_fitness \
        and min(self.conflict_scores) > 0:
            
            # 2. Check if the fitness reached its goal
            if min(self.fitness_scores) <= goal_fitness or min(self.conflict_scores) == 0:
                print(f"GOAL FITNESS REACHED!  Iterations: {iteration}")
                break
            else:
                print(f"Minimum fitness failed to reach {goal_fitness}. Evolving...")
                self.save_to_csv()
            #   3. Otherwise replace the population with new children
                self.produce_children()

                iteration += 1
                print("===========================================================")
                print(f"                  ITERATION {iteration}")
                print("===========================================================")
                self.evaluate_fitness()
                
            

        chosen_index = self.fitness_scores.index(min(self.fitness_scores))
        self.save_to_csv()
        return self.population[chosen_index]
    
    def save_to_csv(self):
        chosen_index = self.fitness_scores.index(min(self.fitness_scores))
        optimized_sch = self.population[chosen_index]
        cols = optimized_sch.shape[1]
        header = ','.join([f"Day {i//3 + 1}/Slot {(i%3 + 1)}" for i in range(cols)])
        np.savetxt("csv/preview.csv", optimized_sch, header=header, delimiter=',', fmt="%d")
    
if __name__ == "__main__":
    exam_scheduler = ExamScheduler(
        pop_size=4,
        slots_per_day=4,
        days=10,
        extra_rooms=6,
        min_allowed_portion=40,     # For crossover
        max_allowed_portion=60,
        mutation_rate=40            # portion of students selected in %
    )
    schedule = exam_scheduler.iterate_and_evolve(10000, 100)

