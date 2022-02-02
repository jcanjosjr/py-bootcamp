# Imagine a list or a dictionary being something like a folder
# where lots of things can be stored inside it, then nesting
# lists and dictionaries is just a matter of putting one inside
# the other.

# {
#   Key: [List],
#   Key2: {Dict}
# }

from re import M


capitals = {
    "France" : "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary:
travelLog = {
    # We have one key value pair, and the value is a list.
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# This idea of nesting isn't limited dictionaries btw.
# Could also just nest a list in a list.
nestingList = ["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary:
travelLogg = {
    "France": {
        "citiesVisited": ["Paris" , "Lille", "Dijon"],
        "totalVisits": 12
    },
    "Germany": {
        "citiesVisited": ["Berlin", "Hamburg", "Stuttgart"],
        "totalVisits": 5
    }
}


# Nesting a Dictionary in a List
travelLoggg = [
    {
        "Country": "France",
        "citiesVisited": ["Paris", "Lille", "Dijon"],
        "totalVisits": 12
    },
    {
        "Country": "Germany",
        "citiesVisited": ["Berlin", "Hamburg", "Stuttgart"],
        "totalVisits": 5
    }
]
