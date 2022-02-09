# Creating a new Object from a blueprint.

from turtle import Turtle, Screen

# timmy is a object, Tutle is the Class.
timmy = Turtle()

print(timmy)        # Print the object, and the ref from a mem.
# shape is a method from the object.
timmy.shape("turtle")
# color is a method from the object.
timmy.color("orange")
# forward i a method from the object.
timmy.forward(100)

myScreen = Screen()
# canvheight is a attribute.
print(myScreen.canvheight)
# exitonclick is a Method.
myScreen.exitonclick()