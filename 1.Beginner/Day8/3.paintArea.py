# Painting a wall.
import math

wallHeight = int(input("Height of wall: "))
wallWidth = int(input("Width of wall: "))
coverage = 5

def paintCalc(height, width, cover):
    area = height * width
    numCans = math.ceil(area / cover)
    print(f"You'll need {numCans} cans of paint.")

paintCalc(height = wallHeight, width = wallWidth, cover = coverage)
