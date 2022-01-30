# Blackjack Game, rules below:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/Ling all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

import random
from art import logo


def dealCard():
    """Return a Random Card from a Deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(cards):
    """Calculate the scores about cards on Blackjack Game."""
    # Validate for a Blackjack count:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Validate if the A is 11 or 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Dealing the cards:
userCards = [dealCard(), dealCard()]
computerCards = [dealCard(), dealCard()]
gameOver = False

print(logo)

# Making a While loop, to validate if Games end.
while not gameOver:
    # Calculate the scores, reveal cards:
    userScore = calculateScore(userCards)
    computerScore = calculateScore(computerCards)
    print(f"Your cards: {userCards}, current score: {userScore}")
    print(f"Computer's first card: {computerCards[0]}.")

    # Validate if anyone lose:
    if userScore == 0 or computerScore == 0 or userScore > 21:
        gameOver = True
    else:
        # Giving the choice from another card to Player:
        userDeal = input("Type 'y' to get another card, type 'n' to pass: ")
        if userDeal == 'y':
            userCards.append(dealCard())
        else:
            gameOver = True

while computerScore != 0 and computerScore < 17:
    computerCards.append(dealCard())
    computerScore = calculateScore(computerCards)


def compare(userScore, computerScore):
    """Compare the Cards Scores for Blackjack results."""
    if userScore == computerScore:
        return f"It's a Draw."
    elif computerScore == 0:
        return f"Lose, opponent has Blackjack."
    elif userScore == 0:
        return f"Win with a Blackjack."
    elif userScore > 21:
        return f"You went over. You Lose."
    elif computerScore > 21:
        return f"Opponent went over. You win."
    elif userScore > computerScore:
        return f"You win."
    else:
        return f"You lose."


# Print the result!
print(f" Your final hand: {userCards}, final score: {userScore}")
print(f" Computer's final hand: {computerCards}, final score: {computerScore}")
print(compare(userScore, computerScore))
