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

        print("DONE!")
        return schedule

# For testing purposes
if __name__ == "__main__":
    maker = ScheduleMaker(
        time_slots_per_day=5,
        days=12
    )

    schedule = maker.generate(extra_rooms=6)
    np.savetxt("csv/init_schedule.csv", schedule, delimiter=',', fmt="%d")
