coffee_type_selection = {"1": "1.Espresso", "2": "2.Double_Espresso", "3": "3.Capucino", "4": "4.Cafe_Late", "5": "5.Cortado"}
tea_type_selection = {"6": "6.Green_tea", "7": "7.Black_tea", "8": "8.Chai_latte"}

coffee_price = {"Espresso": 9.95, "Americano": 11.95, "Cappuccino":12.95, "Cafe_Late":12.95,"Cortado":12.45}
tea_price = {"Green_tea":9.95, "Black_tea":9.95, "Chai_latte":12.95}

class order:
    def __init__(self):
        self.coffee_type()
        self.tea_type()


#print(coffee_type_selection[1].append(str(coffee_type["Espresso"]))

values = coffee_price.values()
values = tea_price.values()
values = coffee_type_selection.values()
values = tea_type_selection.values()

for values in coffee_type_selection.values():
    print(values)

for values in tea_type_selection.values():
    print(values)

for values in coffee_price.values():
    print(values)

for values in tea_price.values():
    print(values)
