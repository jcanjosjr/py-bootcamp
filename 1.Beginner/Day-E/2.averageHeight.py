stundentHeight = input("Input a list of student heights: ").split()

loop = 0
totalHeight = 0

for n in range(0, len(stundentHeight)):
    stundentHeight[n] = int(stundentHeight[n])
    loop += 1
    totalHeight += stundentHeight[n]
print(stundentHeight)

averageHeight = totalHeight / loop

print(f"The average for the values are: {averageHeight}")