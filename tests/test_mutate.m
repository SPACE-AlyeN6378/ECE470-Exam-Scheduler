addpath('genetic_algorithm/')

A = [1:10 * 5];
A = reshape(A, [10, 5])';

A
for i=1:50
    if rand() < 0.3
        A = mutate(A);
    end
end
A