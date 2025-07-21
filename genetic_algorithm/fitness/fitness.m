function totalPenalty = fitness(schedule, students, pop_number)
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

    totalPenalty = 0;

    fprintf("* COMBINATION %d\n", pop_number);

    % TODO: Change this to divide by 3, since we're switching a chunk to be a day
    for start = 1:3:size(schedule, 2)
        end_ = min(start + 2, size(schedule, 2));

        % Debug to console
        fprintf("Analyzing samples from time slots %d to %d...   ", start, end_);

        % Chunk of data from columns n to n+6
        chunk = schedule(:, start:end_);
        totalPenalty = totalPenalty + evaluate_chunk(students, chunk);
    end

    totalPenalty
end