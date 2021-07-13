bidders = {}
bidding_continue = True
   
while bidding_continue == True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    continue_answer = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    bidders[name] = bid
    if continue_answer == "no":
        bidding_continue = False

highest_bid = 0
winner = ""

for person in bidders:
    bids = int(bidders[person]) 
    if bids > highest_bid:
        highest_bid = bids
        winner = person
        

print(f"The winner is {winner} with the bid of: ${highest_bid}")