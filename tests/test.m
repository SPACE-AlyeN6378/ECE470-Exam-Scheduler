addpath("genetic_algorithm/");
addpath("genetic_algorithm/fitness/")
addpath('dataset/');

% scores = [5, 12, 55, 104, 6, 9];
% selected_index = inverted_roulette_selection(scores);
% disp(['Selected index: ', num2str(selected_index), ...
%       ', value: ', num2str(scores(selected_index))]);

students = student_data();
population = init_population(8);
fitness_scores = cellfun(@(comb) fitness(comb, students), population)

% fitness(population, students)
