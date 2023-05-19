#silent auction bidding program
import math

bids = {}

still_bidding = True

def add_to_bidding_pool(name,bid):
    bids[name] = bid

def find_higest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while still_bidding:
    bid = int(input('Whats your bid?\n$'))
    name = input('Thanks, Your name?\n')

    add_to_bidding_pool(name, bid)

    end_bidding = input('Are there still bids? yes or no?').lower()
    if end_bidding == 'no':
        still_bidding = False
        find_higest_bidder(bids)
        print(bids)