import csv #always goes first - importing the database with card details of the customer (card_nr, student vs teacher, name, moneyincard)
from card import Card
from menu import Menu

card_nr = input("Please scan your card!")
with open("card.csv") as csvfile: #csv is the variable now
    reader = csv.reader(csvfile, delimiter=",") #it's gonna import the file intp the csv.
    #When delimiter reaches the "," it's a new value it has to read.

    valid_card_id = "" #create an empty string. We define an invalid card
    for row in reader: #read the row

        if card_nr == row[0]:
            print("Hi, " + row[2]) #row 2 is where we keep the names in the card.csv file
            valid_card_id = card_nr
            card = Card(card_nr, row[1], row[2], row[3]) #here we initial valid_card. gonna be used throughout the whole program
            break
csvfile.close()

    #if card_nr not in id_list:
            #print("Sorry not valid")
if valid_card_id == "": #We defined this as nothing. so if the initial value ("") doesn't change, we haven't found the valid card_nr.
    print("Sorry not valid")
    exit(0)

if card.balance < 20:
    print("Ya broke bruv")
    exit(0)
else:
    Menu.show()

print("Your current balance is "+ str(card.balance) + "kr") #we can't say row[3] anymore cause we exited that function. This is defined by card. is found on line 16
print(card.balance)




with open('card.csv', 'r', newline='\n') as file:
    # read a list of lines into data

    reader = csv.reader(file, delimiter=",")
    data = []
    print(next(reader))
    for row in reader:
        print(row)
        data.append(row)


    for index, row in enumerate(data):
        card_id = row[0]
        if card.id == card_id:
            card.pay(20)
            data[index] = [row[0], row[1], row[2], str(card.balance)]

file.close()
with open('card.csv', mode='w', newline='\n') as myfile:
    writer = csv.writer(myfile, delimiter=',')

    for row in data:
        writer.writerow(row)

myfile.close()
