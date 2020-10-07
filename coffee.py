coffees = ["Espresso", "Americano", "Cappuccino", "Cafe_Late","Cortado" ]
teas = ["Green_tea", "Black_tea", "Chai_latte"]

class beverage:
    def __init__(self, coffees, teas):
        self.coffees()
        self.teas()
    def coffee (self, name, single_vs_double, size, milk, sugar, extras, decor):
            self.name = input("What kind of coffee would you like?")
            self.single_vs_double = input("Would you like a single shot or a double shot?")
            self.size = input("Would you like a small, medium or large" + name + "?")
            self.milk = input("Would you like some milk?")
            if yes:
                light_milk = 1
                fat_milk = 2
                oat_milk = 3
                no_milk = 0
                milk_type = input("""\nWhat kind of milk?
                - Light milk, choose 1
                - Fat milk, choose 2
                - Oat Milk (Vegan), choose 3
                - I don't want any milk
                """)

                    if milk_type == 1:
                        print ("your" + coffee + "will be made with" + 1 + "milk")
                    elif milk_type == 2:
                        print ("your" + coffee + "will be made with" + 2 + "milk")
                    elif milk_type == 3:
                        print ("your" + coffee + "will be made with" + 3 + "milk")
                    elif milk_type == 0:
                        print ("You've chosen not to add any milk")
                    else:
                        print ("Please, make a selection.")
