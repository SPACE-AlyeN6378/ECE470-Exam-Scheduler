import pandas as pd
import numpy as np
import math

DEBUG = False
# Set print options to avoid wrapping
# np.set_printoptions(linewidth=np.inf)  # Set linewidth to infinity

class ScheduleMaker:

    def __init__(self, time_slots_per_day, days,
                 file_path='dataset/Final_Complete_Course_List.xlsx', sheet_name="Sheet1"):
        self.df = pd.read_excel(file_path, sheet_name=sheet_name)
        self.courses = self.df['CourseCode'].to_numpy()
        self.time_slots_per_day = time_slots_per_day
        self.days = days
    
    def __courses_per_major(self, major):
        courses_per_major = self.courses[self.courses // 1000 == major]
        courses_per_major.sort()
        return courses_per_major
    
    def __courses_per_major_max_qty(self):
        return max(len(self.__courses_per_major(major)) for major in self.majors)
    
    def __courses_by_index(self, index):
        return np.array([self.__courses_per_major(major)[index] 
                         for major in self.majors 
                         if index < len(self.__courses_per_major(major))])
    
    def generate(self, extra_rooms=0):

        print(f"Generating schedule...   ", end="")
        total_slots = self.time_slots_per_day * self.days
        minimum_rooms = math.ceil(len(self.courses) / total_slots)

        # Make a set of clustered courses
        np.random.shuffle(self.courses)
        clustered_schedule = self.courses.reshape((minimum_rooms, total_slots))
        
        # Make an empty set of schedule
        rooms = minimum_rooms + extra_rooms
        schedule = np.zeros((rooms, total_slots), dtype=int)
        schedule[0:minimum_rooms] = clustered_schedule
        np.random.shuffle(schedule)


        # Reshuffle the majors
        # self.majors = self.__get_majors()
        
        # middle_starting_pts = []

        # # Fill the first half of the schedule
        # for index in range(self.__courses_per_major_max_qty()):

        #     courses = self.__courses_by_index(index)
        #     courses_per_time_slot = courses[0:self.ROOMS]
        #     redundant_courses = courses[self.ROOMS:len(courses)]

        #     if index < self.__courses_per_major_max_qty() // 2:
        #         schedule[0:self.ROOMS, 3*index] = courses_per_time_slot
        #         schedule[0:len(redundant_courses), 3*index + 1] = redundant_courses
        #         middle_starting_pts.append(len(redundant_courses))

        #     else:
        #         mod_index1 = (3*index + 2) % self.TIME_SLOTS
        #         mod_index2 = (3*index + 1) % self.TIME_SLOTS
        #         start = middle_starting_pts[index % len(middle_starting_pts)]

        #         schedule[0:self.ROOMS, mod_index1] = courses_per_time_slot
        #         schedule[start:start+len(redundant_courses), mod_index2] = redundant_courses

        print("DONE!")
        return schedule

        # if DEBUG:
        #     for i in range(0, 30, 6): 
        #         print(schedule[:, i:i+6])

        

        # return schedule


if __name__ == "__main__":
    maker = ScheduleMaker(
        time_slots_per_day=5,
        days=12
    )

    schedule = maker.generate(extra_rooms=6)
    np.savetxt("csv/init_schedule.csv", schedule, delimiter=',', fmt="%d")
    # flattened = schedule.flatten()
    # print(schedule == flattened.reshape((maker.ROOMS, maker.TIME_SLOTS)))