function penalty = fitness(schedule)
% FITNESS Evaluates the overall quality of a complete exam schedule.
%
%   penalty = fitness(schedule)
%
%   Inputs:
%     schedule - A matrix representing the full exam schedule. Each column is a time slot,
%                and each row represents rooms containing course IDs where the exam is scheduled 
%                at that time.
%
%   Output:
%     penalty  - A scalar penalty score that reflects the overall "badness" of the schedule.
%                Higher values indicate more student conflicts or clustering of exams.

    students = student_data();
    penalty = 0;

    for start = 1:6:size(schedule, 2)
        end_ = min(start + 5, size(schedule, 2));

        % Chunk of data from columns n to n+6
        chunk = schedule(:, start:end_);
        penalty = penalty + evaluate_chunk(students, chunk);
    end

end