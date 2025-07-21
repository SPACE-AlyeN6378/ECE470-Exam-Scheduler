addpath("genetic_algorithm/");
addpath("genetic_algorithm/fitness");
addpath("dataset/");

% Configuration Parameters
POPULATION_SIZE = 6;
MIN_ALLOWED_PORTION = 40;
MAX_ALLOWED_PORTION = 60;
MAX_MUTATION_RATE = 15;
GOAL_SCORE = 200;

MAX_ITERATIONS = 100;


diary("exam_scheduler_log.txt")

% current_fitness_scores = table2array(readtable("csv/fitness_scores.csv"));

% 1. Initialize the student data
students = student_data();

% 2. Make the first evolution
[current_population, fitness_scores] = first_evolution(students, POPULATION_SIZE);

% 3. Iterate and evolve
for i=1:MAX_ITERATIONS

    % Check if the schedule meets the goal
    if any(fitness_scores < GOAL_SCORE)
        fprintf("AWESOME! Exam schedule successful! Terminating...\n");
        break
    end

    % Evolve
    [new_population, new_fitness_scores] = evolve(students, current_population, fitness_scores, ...
        i+1, MIN_ALLOWED_PORTION, MAX_ALLOWED_PORTION, MAX_MUTATION_RATE);

    % Update the current population and fitness 
    current_population = new_population;
    fitness_scores = new_fitness_scores;

end

[chosen_value, chosen_idx] = min(fitness_scores);
final_schedule = current_population{chosen_idx};  % <=== THIS IS WHAT WE NEED!!

% TODO: Write the Final schedule to CSV


diary off
