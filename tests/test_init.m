addpath("genetic_algorithm/");
addpath("genetic_algorithm/fitness/")
addpath('dataset/');

fprintf("=========================================================\n");
fprintf("                EVOLUTION 1                          \n");
fprintf("=========================================================\n\n");

SAVE_TO_CSV = false;

% scores = [5, 12, 55, 104, 6, 9];
% selected_index = inverted_roulette_selection(scores);
% disp(['Selected index: ', num2str(selected_index), ...
%       ', value: ', num2str(scores(selected_index))]);

students = student_data();
population = init_population(8);

if SAVE_TO_CSV
    for i=1:length(population)
        filename = sprintf("csv/population%d.csv", i);
        writematrix(population{i}, filename);
    end
end

fitness_scores = population_fitness(population, students);

if SAVE_TO_CSV
    writematrix(fitness_scores, "csv/fitness_scores.csv");
end


% fitness(population{4}, students, 4);

% fitness(population{3}, students)
