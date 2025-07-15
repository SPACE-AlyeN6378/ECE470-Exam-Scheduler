addpath('genetic_algorithm/')

A = [1:10 * 5];
A = reshape(A, [10, 5])';

A
A = mutate(A);
A = mutate(A);
A