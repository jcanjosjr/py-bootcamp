# Functions with Outputs. (return statement)


def myFunction():
    result = 3 * 2
    return result


print(myFunction())

# Function with Outputs is like a machine where in goes some
# empty bottles and after some processing, outcomes a bottle
# filled.


def formatName(fName, lName):
    name = str(fName.title() + ' ' + lName.title())
    return print(name)


formatName("joSe", "carlos")
