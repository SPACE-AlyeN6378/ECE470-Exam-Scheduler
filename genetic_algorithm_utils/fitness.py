import numpy as np
import time

def fitness_per_day(student_data, chunk_of_schedule):
    conflict_count = 0
    multiple_exam_count = 0

    for student_courses in student_data:

        courses_count = [len(np.intersect1d(student_courses, time_slot)) for time_slot in chunk_of_schedule.T]

        # Exams cannot be taken simultaneously
        if max(courses_count) > 1:
            conflict_count += 1
        
        # Only one exam within 24-hour period is allowed
        exams = sum(int(x > 0) for x in courses_count)
        if exams > 1:
            multiple_exam_count += 1

    penalty = conflict_count * 10 + multiple_exam_count
    print(f"Conflicts: {conflict_count}    Students having MTO exams: {multiple_exam_count}  PENALTY: {penalty}")

    return penalty

def fitness(student_data, schedule):

    total_penalty = 0
    for i in range(0, len(schedule[0]), 3):
        j = i + 3
        print(f"Analyzing per-day schedule, columns {i} to {j}...")

        total_penalty += fitness_per_day(student_data, schedule[:, i:j])

    print(f"\nTotal penalty = {total_penalty}\n")

    return total_penalty
        

if __name__ == "__main__":
    schedule = np.loadtxt('csv/schedule.csv', delimiter=',')
    student_data = np.loadtxt('csv/students.csv', delimiter=',', dtype=int)

    print(student_data)

    # start = time.time()
    # score = fitness(student_data, schedule)
    # end = time.time()

    # print(f"Time: {end - start} seconds")



