function [new_population, new_fit_scores] = evolve(student_data, current_pop, current_scores, iteration_number, ...
    portion_lb, portion_ub, mutation_rate)

    fprintf("=========================================================\n");
    fprintf("                     EVOLUTION %d       \n", iteration_number);
    fprintf("=========================================================\n\n");

    % Initialize an empty array of new population and fitness scores
    new_population = {};
    new_fit_scores = zeros(1, length(current_pop));

    % Iterate through each parent and calculate the fitness
    for i = 1:2:length(current_pop)
        % Select the parents with the low anti-fitness scores at random
        [idx1, idx2] = natural_selection(current_scores);

        % Produce children
        [child1, child2] = produce_offspring(current_pop{idx1}, current_pop{idx2}, portion_lb, portion_ub, mutation_rate);

        % Append those children to a new population, and calculate the anti-fitness of this child
        new_population{end + 1} = child1;
        new_fit_scores(i) = fitness(child1, student_data, i);
        
        % Do the same for child 2
        new_population{end + 1} = child2;
        new_fit_scores(i+1) = fitness(child2, student_data, i+1);
    
    end
end

