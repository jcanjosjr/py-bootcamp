# I used a Flowchart to help understand the focus from exercise.
# Goal was to create code to simulation a Secret Auction.

from click import clear
from art import logo

# Starting the Project.
print(logo)

bids = {}
biddingFinished = False


# Creating the function for resolves bids.
def highBidder(biddingRecord):
    # {"Jose": 123, "James": 321}
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = int(biddingRecord[bidder])
        # print(bidAmount)
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}.")


# Making the loop for the "front" are of the Program:
while not biddingFinished:
    # Inputs collecting Data for a user.
    name = input("Please, tell your name: ")
    price = input("What is your bid? $")
    bids[name] = price
    # Making sure if the Loop need happens:
    shouldContinue = input("Are there any other bidders? Type [yes/no]: ")
    if shouldContinue == "no":
        biddingFinished = True
        # Calling the Function to resolves the Bid Winner.
        highBidder(bids)
    elif shouldContinue == "yes":
        clear()
