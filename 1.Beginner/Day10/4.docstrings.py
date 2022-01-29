# Docstrings are basically a way for us to create little
# bits of documentation as we're coding along in our functions
# or in our other blocks of code.

lenght = len()
# Return the numbers of items in a container.

def formatName(fName, lName):
    """Transform the name on Title Case."""
    fName = fName.title()
    lName = lName.title()
    return f"{fName} {lName}"

