travelLog = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def addNewCountry(countryVisited, timesVisited, citisVisited):
    newCountry = {}
    newCountry["country"] = countryVisited
    newCountry["visits"] = timesVisited
    newCountry["cities"] = citisVisited
    travelLog.append(newCountry)

addNewCountry("Russia", 2, ["Moscow", "Saint Peterburg"])

print(travelLog)
