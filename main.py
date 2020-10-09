#we are impoerting a database with card details. (card_nr, student vs employee, name, balance)
import csv
from card import Card
from menu import Menu #this imports only the function show from my menu.py file
prompt = "> "




#We are asking the user to isert his card
card_nr = input("Please, scan your card " + prompt)
with open("card.csv") as csvfile:
    #here we openned the csv file, and with delimiter we are saying that inside the csv the different values are delimited by comas.
    reader = csv.reader(csvfile, delimiter=",")
    #Now we are findig the rows in the reader. We are validating the card.
    valid_card_id = "" #We are creating an empty string to see if the ID is good or not
    for row in reader: #read the row
        if card_nr == row[0]:
            print("Hi, " + row[2])
            valid_card_id = card_nr
            card = Card(card_nr, row[1], row[2], row[3]) #I am initializing my vlaid card.
            break

csvfile.close()

if valid_card_id == "": # It cannot find the valid card id, because the initial value did not change
    print("Sorry, this is not a valid card, please insert a valid KEA Student or KEA employee card")
    exit(0)

if card.balance < 20:
    print("Your balance is below 20 kr, please top up")
    exit(0)
else:
    Menu.show()

print("Your current balance is " + str(card.balance) + "kr")
print(card.balance)
