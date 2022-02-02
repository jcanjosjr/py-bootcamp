# Resolving the blanks inputs with return statements.


def formatName(fName, lName):
    if fName == "" or lName == "":
        return "You didn't provide valid inputs."
    name = str(fName.title() + ' ' + lName.title())
    return print(name)


formatName("joSe", "carlos")
formatName("", "")

