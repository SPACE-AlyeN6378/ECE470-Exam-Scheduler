function [population, fitness_scores] = first_evolution(students, pop_size)
    fprintf("=========================================================\n");
    fprintf("                EVOLUTION 1                          \n");
    fprintf("=========================================================\n\n");

    population = init_population(pop_size);

    fitness_scores = zeros(1, length(population));  % Preallocate numeric array

    for i=1:length(population)
        fitness_scores(i) = fitness(population{i}, students, i);
    end
end