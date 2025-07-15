addpath("dataset/");
addpath("genetic_algorithm/fitness/")

schedule = generate_combinations();
% chunk = schedule(:, 7:12);

% Retrieve a table of students with rows indicating the 5 courses taken
students = student_data();

fitness_penalty = fitness(schedule)
