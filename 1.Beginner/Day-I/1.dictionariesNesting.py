# Dictionaires in Python work kind of similarly to dictionaries
# in real life, so if you were to look up a word in the dictionary,
# then you might find the definition.
# Really useful because they allow us to group together and tag
# related pieces of information.

dictionaries = { 
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easilly call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(dictionaries["Bug"])
# If we try to put in a key that doesn't exist, then we get key error.

# Adding new items to dictionary.
dictionaries["Loop"] = "Adding this again?"
print(dictionaries)

# Very often when you're writing code, it can be really helpful
# to start out with a empty dictionary, or a empty list.
emptyList = []
emptyDictionary = {}

# Edit an item in a dictionary:
dictionaries["Bug"] = "Come on, everyone make mistakes xD"
print(dictionaries["Bug"])

# Loop through a Dictionary, just gives the keys.
for key in dictionaries:
    print(key)
# For loop through a Dictionary with Key and value.
for key in dictionaries:
    print(key)
    print(dictionaries[key])

# Wipe an existing dictionary:
dictionaries = {}
print(dictionaries)
