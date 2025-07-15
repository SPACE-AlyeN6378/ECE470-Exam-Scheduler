function combination = generate_combinations()
    course_table = readtable("Complete_Course_List.xlsx");

    % Extract a column by its name and shuffle it
    courses = course_table.CourseCode;
    courses = courses(randperm(length(courses)));

    % Split the courses into columns of 24 rows
    % Each column represents a time slot, and each row represents a
    % room where the exams would take place
    combination = reshape(courses, 24, []);
end
