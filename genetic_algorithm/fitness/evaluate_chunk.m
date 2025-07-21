function penalty = evaluate_chunk(students, chunk)
% EVALUATE_CHUNK Calculates a penalty score for a given 48-hour (or less) exam schedule.
%
%   penalty = evaluate_chunk(students, chunk)
%
%   Inputs:
%     students - A matrix where each row contains course IDs taken by a student.
%     chunk    - A matrix representing a 48-hour schedule. Each column is a time slot,
%                and each row is a room associated scheduled at that time.
%
%   Output:
%     penalty  - A scalar penalty score. Higher penalties indicate worse schedules
%                due to overlapping exams or excessive exams in a short period.

    penalty = 0;

    % Iterate through each student
    for student_id = 1:size(students, 1)  % ================================================================

        % Grab the number of courses taken
        courses_taken = students(student_id, :);
        total_courses_per_chunk = 0;

        % Iterate through each column of the chunk
        for col = 1:size(chunk, 2)
            % Get the courses taken by a student from the time slot
            courses_per_time_slot = intersect(chunk(:, col), courses_taken);
            
            
            if size(courses_per_time_slot, 1) > 0
                % Hell no, I'm not gonna two exams simulatenously!!!
                % The penalty is way heavier! So +10
                if size(courses_per_time_slot, 1) > 1
                    penalty = penalty + 10;
                end

                % Increment the total number of courses per chunk
                total_courses_per_chunk = total_courses_per_chunk + size(courses_per_time_slot, 1);
            end
        end

        % TODO: There's too much restriction. Make the fitness such that there is only one exam within __24 HOURS__
        % Impose a penalty if the total courses in a 48-hour period is more than one
        if total_courses_per_chunk > 0
            penalty = penalty + total_courses_per_chunk - 1;
        end

    end
    fprintf("PENALTY: %d\n", penalty);
end