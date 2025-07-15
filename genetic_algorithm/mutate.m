function A = mutate(A)
    % TODO: In the main program, make sure that there is a CHANCE that mutation has been happening
    % We want there to have multiple mutations (e.g. 720 mutations by random)

    % Retreive two positions at random
    pos1 = randi([1, numel(A)]);
    pos2 = randi([1, numel(A)]);

    % If the two positions are equal, then re-generate them
    while isequal(pos1, pos2)
        pos1 = randi([1, numel(A)]);
        pos2 = randi([1, numel(A)]);
    end

    temp = A(pos1);
    A(pos1) = A(pos2);
    A(pos2) = temp;
end