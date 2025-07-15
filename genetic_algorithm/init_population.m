function population = init_population(pop_size)
    % Array to store population of unique combinations of schedule
    population = {};

    while length(population) < pop_size
        combination = generate_combinations();
        if ~any(cellfun(@(x) isequal(x, combination), population))
            population{end+1} = combination;
        end 
    end
end