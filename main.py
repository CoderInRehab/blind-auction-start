from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("\nWelcome to the secret auction program.\n")


def highest_bidder(bid_data):
  
  high = 0
  high_name = ""
  for data in bid_data:
    #print(data, bidder[data])
    current_bid = bid_data[data]
    if current_bid > high:
      high = bid_data[data]
      high_name = data 

  print(f"The winner is {high_name} with a bid amount of {high}")


is_finished = False

# bidders_data key=name value=bid
bidder = {}

while not is_finished:
  bidder_name = input("What is your name?\t")
  bid_amount = int(input("What's your bid?\t$"))

  bidder[bidder_name] = bid_amount
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")  
  if choice == "no":
    is_finished = True
    highest_bidder(bidder)
  elif choice == "yes" :
    clear()

  


