studentScore = input("Input a list of student scores: ").split()

high = 0

for n in range (0, len(studentScore)):
    studentScore[n] = int(studentScore[n])
    if high < studentScore[n]:
        high = studentScore[n]
print(studentScore)

print(high)

