function students = student_data()
    table = readtable("College_Student_Dataset_With_Codes.xlsx");
    students = [table.Course1Code, table.Course2Code, table.Course3Code, table.Course4Code, table.Course5Code];
end