# The goal is to build a blind auction program.
#
# Demo
# https://appbrewery.github.io/python-day9-demo/
#
# Clearing the Output
# There are several ways of clearing the output.
# The easiest is to simply print "\n" many times
# so that the output scrolls down many lines.
#
# e.g.
#
# # This will add 20 new lines to the output
# print("\n" * 20)
# Functionality
# Each person writes their name and bid.
# The program asks if there are others who need to bid.
# If so, then the computer clears the output (prints several
# blank lines) then loops back to asking name and bid.
# Each person's name and bid are saved to a dictionary.
# Once all participants have placed their bid,
# the program works out who has the highest bid and prints it.


# Flowchart
# If you want to see my flowchart, you can download it here.

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

bid_dictionary = {}
auction_running = True
highest_bidder = ""
highest_bidding_amount = 0

while auction_running:
    # Ask the user for input
    user_name = input("What is your name?:")
    user_bid_price = int(input("What is your bid?: $"))

    # Save data into dictionary {name: price}
    bid_dictionary = {
        user_name: user_bid_price
    }

    # or
    # bid_dictionary[user_name] = user_bid_price

    any_user = input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if any_user == 'no':
        auction_running = False
    else:
        print("\n" * 20)

for bidder in bid_dictionary:
    if bid_dictionary[bidder] > highest_bidding_amount:
        highest_bidding_amount = bid_dictionary[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bidding_amount}")