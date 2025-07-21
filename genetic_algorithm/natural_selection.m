function [indexA, indexB] = natural_selection(fitness_scores)
    % Select two indexes
    indexA = inverted_roulette_selection(fitness_scores);
    indexB = inverted_roulette_selection(fitness_scores);

    % Avoid duplicate parents
    while indexB == indexA
        % Then select again
        indexB = inverted_roulette_selection(fitness_scores);
    end
end


