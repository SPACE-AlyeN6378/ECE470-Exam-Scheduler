function found = list_contains(cellArray, target)
    found = false;
    for i = 1:length(cellArray)
        if isequal(cellArray{i}, target)
            found = true;
            break;
        end
    end
end