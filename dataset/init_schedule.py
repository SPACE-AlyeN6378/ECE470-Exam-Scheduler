import pandas as pd
import numpy as np

DEBUG = False
# Set print options to avoid wrapping
# np.set_printoptions(linewidth=np.inf)  # Set linewidth to infinity

class ScheduleMaker:

    def __init__(self, file_path='dataset/Final_Complete_Course_List.xlsx', sheet_name="Sheet1"):
        self.df = pd.read_excel(file_path, sheet_name=sheet_name)
        self.courses = self.df['CourseCode'].to_numpy()
        self.majors = self.__get_majors()
        self.TIME_SLOTS = 30
        self.ROOMS = 24

    def __get_majors(self, randomize=True):

        majors = np.unique(self.courses // 1000)

        if randomize:
            np.random.shuffle(majors)

        return majors
    
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
    
    def generate(self):

        print("Generating schedule...   ", end="")
        schedule = np.zeros((self.ROOMS, self.TIME_SLOTS), dtype=int)

        # Reshuffle the majors
        self.majors = self.__get_majors();
        
        middle_starting_pts = []

        # Fill the first half of the schedule
        for index in range(self.__courses_per_major_max_qty()):

            courses = self.__courses_by_index(index)
            courses_per_time_slot = courses[0:self.ROOMS]
            redundant_courses = courses[self.ROOMS:len(courses)]

            if index < self.__courses_per_major_max_qty() // 2:
                schedule[:, 3*index] = courses_per_time_slot
                schedule[0:len(redundant_courses), 3*index + 1] = redundant_courses
                middle_starting_pts.append(len(redundant_courses))

            else:
                mod_index1 = (3*index + 2) % self.TIME_SLOTS
                mod_index2 = (3*index + 1) % self.TIME_SLOTS
                start = middle_starting_pts[index % len(middle_starting_pts)]

                schedule[:, mod_index1] = courses_per_time_slot
                schedule[start:start+len(redundant_courses), mod_index2] = redundant_courses

        print("DONE!")

        if DEBUG:
            for i in range(0, 30, 6): 
                print(schedule[:, i:i+6])

        

        return schedule


if __name__ == "__main__":
    maker = ScheduleMaker()

    schedule = maker.generate()
    # flattened = schedule.flatten()
    # print(schedule == flattened.reshape((maker.ROOMS, maker.TIME_SLOTS)))