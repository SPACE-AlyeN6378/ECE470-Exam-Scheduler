function [child1, child2] = produce_offspring(parentA, parentB, portion_lb, portion_ub, mutation_rate)

    % Portioning is randomized
    portion = randi([portion_lb, portion_ub]);

    % Iterating sideways is a coin toss
    sideways = rand() > 0.5;

    % Perform crossover between the two parents
    [child1, child2] = crossover(parentA, parentB, portion, sideways);

    % Perform mutation 720 times
    for i=1:numel(child1)
        % There a given likelihood (mutation_rate) as to how much mutation would occur
        if rand() < (mutation_rate / 100)   % Mutate the first child
            mutate(child1);
        end

        if rand() < (mutation_rate / 100)   % Mutate the second child
            mutate(child2);
        end
    end

end
