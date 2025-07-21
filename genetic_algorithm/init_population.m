function population = init_population(pop_size)
    % Array to store population of unique combinations of schedule
    population = {};

    fprintf("\nInitializing population of %d combinations... ***************************************\n", pop_size);

    while length(population) < pop_size
        fprintf("%d) ", length(population) + 1);
        combination = generate_combinations();
        if ~any(cellfun(@(x) isequal(x, combination), population))
            population{end+1} = combination;
        end 
    end

    fprintf("************************************************************************************\n\n");
end