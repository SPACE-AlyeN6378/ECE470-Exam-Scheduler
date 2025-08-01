import numpy as np
import time



def fitness_per_day(student_data, chunk_of_schedule):
    conflict_count = 0      # Students facing more than one exams simultaneously
    # TODO: Terminate the algorithm when the conflict_count is zero
    
    multiple_exam_count = 0

    for student_courses in student_data:
        courses_count = np.array([len(np.intersect1d(student_courses, time_slot)) for time_slot in chunk_of_schedule.T])

        # Exams cannot be taken simultaneously
        if max(courses_count) > 1:
            conflict_count += 1
        
        # Only one exam within 24-hour period is allowed
        exams = sum(int(x > 0) for x in courses_count)
        if exams > 1:
            multiple_exam_count += 1

    penalty = conflict_count * 10 + multiple_exam_count
    print(f"Conflicts: {conflict_count}    Students having MTO exams: {multiple_exam_count}  PENALTY: {penalty}")

    return conflict_count, multiple_exam_count, penalty

def fitness(student_data, schedule, slot_per_day):
    total_penalty = 0
    total_conflicts = 0
    total_mtos = 0

    for i in range(0, len(schedule[0]), slot_per_day):
        j = i + slot_per_day
        print(f"Analyzing per-day schedule, columns {i+1} to {j}...")
        conflicts, mtos, penalty = fitness_per_day(student_data, schedule[:, i:j])
        total_conflicts += conflicts
        total_mtos += mtos
        total_penalty += penalty

    print(f"\nTotal penalty = {total_penalty}\n")

    return total_conflicts, total_mtos, total_penalty
        

if __name__ == "__main__":
    schedule = np.loadtxt('csv/initial_schedule.csv', delimiter=',')
    schedule2 = np.loadtxt('csv/preview.csv', delimiter=',')
    student_data = np.loadtxt('csv/students.csv', delimiter=',', dtype=int)

    fitness = fitness(student_data, schedule2, 4)
    print(fitness)
    
    # print(slots)
    # zero_location = np.where(schedule[:, 16:20] == 0)
    # print(get_slots(schedule, exams))
    # for row in exams_per_student(student_data[456], schedule[:, 16:20]):
    #     print(row)


    # start = time.time()
    # score = fitness(student_data, schedule)
    # end = time.time()

    # print(f"Time: {end - start} seconds")



