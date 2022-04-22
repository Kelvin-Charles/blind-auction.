import subprocess
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is Your Name?: ")
    price =float(input("What is Ammount You want to Bid? Tsh"))
    bids[name] = price
    finish_status = input("Are there other bidders? 'yes' or 'no': ")
    if finish_status == "no":
        bidding_finished = True
    elif finish_status == 'yes':
        subprocess.call("clear")
def find_highest_bidder(bidding_record):
    highest_ammount = 0
    winner = ""
    for bidder in bids:
        bid_ammount = bids[bidder]
        if bid_ammount > highest_ammount:
            highest_ammount = bid_ammount
            winner = bidder
    print(f"Highest bidder is {winner} with bid of Tsh{highest_ammount}")
find_highest_bidder(bids)

