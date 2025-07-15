function index = inverted_roulette_selection(scores)
    % Ensure scores is a row vector
    scores = scores(:)';

    % Invert scores: lower scores become higher weights
    max_score = max(scores);
    inverted = max_score - scores + 1;  % +1 ensures no zero weight

    % Compute cumulative sum
    cum_sum = cumsum(inverted);
    total = cum_sum(end);

    % Randomly select a value
    r = rand() * total;

    % Find the first index where cumulative sum exceeds r
    index = find(cum_sum >= r, 1, 'first');
end