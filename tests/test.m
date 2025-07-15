addpath("genetic_algorithm/")

scores = [5, 12, 55, 104, 6, 9];
selected_index = inverted_roulette_selection(scores);
disp(['Selected index: ', num2str(selected_index), ...
      ', value: ', num2str(scores(selected_index))]);