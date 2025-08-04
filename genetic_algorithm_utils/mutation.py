import random
import numpy as np

DEBUG = True

def exams_per_student(student_courses, chunk_of_schedule):
    exams = []
    for time_slot in chunk_of_schedule.T:
        exams.extend(np.intersect1d(student_courses, time_slot).tolist())
    
    exams = [int(exam) for exam in exams]
    return exams

def get_slots(schedule, exams):
    return [np.where(schedule == exam) for exam in exams]

def fill_first_empty_room(schedule, chunk_start, slots_per_day, course: int):
    # Define the chunk from the starting position
    if chunk_start % slots_per_day != 0:
        raise ValueError(f"'chunk_start' must be in multiples of {slots_per_day}")

    chunk = schedule[:, chunk_start:chunk_start+slots_per_day]

    # Find the first zero in the subarray
    zero_indices = np.argwhere(chunk == 0)
    if zero_indices.size > 0:
        rel_index = tuple(zero_indices[0])
        abs_index = (rel_index[0], rel_index[1] + chunk_start)
        schedule[abs_index] = course

        return True
    else:
        return False
    
def remove_exam(schedule, course: int):
    # Find the first zero in the subarray
    schedule[schedule == course] = 0

def student_has_mto(schedule, student_courses, slot_per_day):
    time_slots = schedule.shape[1]
    for i in range(0, time_slots, slot_per_day):
        exams = exams_per_student(student_courses, schedule[:, i:i+4])
        if len(exams) > 1:
            return True
        
    return False

def spread_mutation_per_student(schedule, student_courses, slots_per_day):

    time_slots = schedule.shape[1]
    excess_courses = []

    # Iterate through each day and find the one with MTO exams
    for i in range(0, time_slots, slots_per_day):
        exams = exams_per_student(student_courses, schedule[:, i:i+slots_per_day])
        # If the exam slot has more than one courses, add the excess ones to the list
        if len(exams) > 1:
            # Add the excess exams to the list
            excess_courses.extend(exams[1:])

    # Iterate through each excess courses and add them to days where students don't have exams
    if excess_courses:
        # Take all the chunks with no exams
        chunk_numbers_with_no_exams = [i for i in range(0, time_slots, slots_per_day) 
                                       if not exams_per_student(
                                           student_courses, schedule[:, i:i+slots_per_day]
                                           )]
        
        # Each of the exams are placed to no exams at random
        random.shuffle(chunk_numbers_with_no_exams)

        for suspect, chunk_number in zip(excess_courses, chunk_numbers_with_no_exams):
            remove_exam(schedule, suspect)
            fill_first_empty_room(schedule, chunk_number, slots_per_day, suspect)

def spread_mutation(schedule, student_data, portion_of_students, slots_per_day):
    student_size = student_data.shape[0]
    selected_students_qty = student_size * portion_of_students // 100

    for student_courses in student_data[np.random.choice(student_size, size=selected_students_qty, replace=False)]:
        spread_mutation_per_student(schedule, student_courses, 
                                    slots_per_day)
        
# For testing purposes
if __name__ == "__main__":

    schedule = np.loadtxt('csv/initial_schedule.csv', delimiter=',', dtype=int)
    student_data = np.loadtxt('csv/students.csv', delimiter=',', dtype=int)

    spread_mutation(schedule, student_data, 40, 4)
    np.savetxt('csv/preview.csv', schedule, delimiter=',', fmt="%d")                
        