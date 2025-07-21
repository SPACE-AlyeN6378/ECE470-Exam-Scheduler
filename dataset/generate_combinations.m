function combination = generate_combinations()
    fprintf("Extracting complete course list ");
    course_table = readtable("Final_Complete_Course_List_NoDuplicates.xlsx");

    % Extract a column by its name and shuffle it
    courses = course_table.CourseCode;

    % Error guard to ensure that all the courses are unique to each other
    if numel(courses) ~= numel(unique(courses))
        error("The course IDs need to be unique to each other");
    end

    fprintf("/ Randomizing and splitting to 24 rows... ");
    courses = courses(randperm(length(courses)));

    % Split the courses into columns of 24 rows
    % Each column represents a time slot, and each row represents a
    % room where the exams would take place
    combination = reshape(courses, 24, []);
    fprintf("OK\n");
end
