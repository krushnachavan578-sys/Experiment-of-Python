# create student records
grades = {"Om Patil": "A", "Krushna Chavan": "B"}
attendance = {"Krushna Jadhav": "100", "Om Patil": "99"}

# update a student grade and attendance
grades["Krushna Chavan"] = "A+"
attendance["Krushna Jadhav"] = 75

print(grades)
print(attendance)

# Add a new student
grades["karunesh Jadhav"] = "A"
attendance["karunesh Jadhav"] = 89

print("After inserting new student:", grades)
print("After inserting new student:", attendance)

# Remove a student
grades.pop("Krushna Chavan")
attendance.pop("Om Patil")

print("After deleting new student:", grades)
print("After deleting new student:", attendance)

# display student records
for Gradeskey, GradesValue in grades.items():
    print(Gradeskey, GradesValue)

for Gradeskey, GradesValue in attendance.items():
    print(Gradeskey, GradesValue)
