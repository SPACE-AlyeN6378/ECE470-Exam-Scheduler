function students = student_data()
    fprintf("Extracting student samples from the spreadsheet... ")
    table = readtable("Final_College_Student_Dataset_NoDuplicates.xlsx");
    students = [table.Course1_Code, table.Course2_Code, table.Course3_Code, table.Course4_Code, table.Course5_Code];
    fprintf("DONE!\n")
end