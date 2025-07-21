

function [newA, newB] = crossover(A, B, portion, sideways)

    % Performs crossover operation between two matrices A and B for genetic algorithms.
    % The function exchanges a specified portion of elements between A and B.
    % The 'portion' parameter defines the percentage of the matrix to be crossed over.
    % The 'sideways' boolean determines if the crossover is performed horizontally (true) or vertically (false).
    %
    % Inputs:
    %   A        - First input matrix.
    %   B        - Second input matrix.
    %   portion  - Percentage of the matrix to be crossed over (0-100).
    %   sideways - Boolean flag; true for horizontal crossover, false for vertical.
    %
    % Outputs:
    %   A_new    - Matrix A after crossover.
    %   B_new    - Matrix B after crossover.

    % Check the dimensions of A and B and see if they're equal
    if ~isequal(size(A), size(B))
        error('Input matrices A and B must have the same dimensions.');
    end

    [rows, cols] = size(A);

    % Set the number of swap based on the rate
    numberOfSwaps = ceil((portion/100) * (numel(A) / 2));
    newA = A; newB = B;

    for n = 0:(numberOfSwaps-1)
        
        if sideways
            i = floor(n / cols) + 1;
            j = mod(n, cols) + 1;
        else
            i = mod(n, rows) + 1;
            j = floor(n / rows) + 1;
        end
        
        num1 = A(i, j);
        num2 = A(A == B(i, j));

        newA(A == num1) = num2;
        newA(A == num2) = num1;

        newB(B == num1) = num2;
        newB(B == num2) = num1;

        A = newA;
        B = newB;
    end
end
