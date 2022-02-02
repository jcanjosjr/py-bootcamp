# Access a database of stundents in the format of a dict.
studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 92
}

studentGrades = {}

# Add grades to student
for student in studentScores:
    score = studentScores[student]
    if score > 90:
        studentGrades[student] = "Outstanding!"
    elif score > 80:
        studentGrades[student] = "Exceeds Expectations."
    elif score > 71:
        studentGrades[student] = "Acceptable."
    else:
        studentGrades[student] = "Fail."

print(studentGrades)
