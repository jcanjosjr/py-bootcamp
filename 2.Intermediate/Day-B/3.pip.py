from prettytable import PrettyTable

# Creating a new Object:
table = PrettyTable() 

# Using the method add_column from the object table.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# We can also change the object's attributes, like align to the left:
table.align = "l"

# Order the table from the column "Pokemon Name"
print(table.get_string(sortby="Pokemon Name"))
