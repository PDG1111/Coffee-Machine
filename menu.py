from beverage import Beverage


class Menu:
    def show():
        print("""
        _____________________________________________________________________________________
        ¦                                   M E N U                                           ¦
        ¦_____________________________________________________________________________________¦
        ¦                                                                                     ¦
        ¦ Please, choose one of the following beverages:                                      ¦
        ¦      Coffees  ☕                        Teas    🍵                                    ¦
        ¦                                                                                     ¦
        ¦  1.Double Espresso      ᕦ(ò_óˇ)             6. Black Tea   ⚫                      ¦
        ¦                                                                                     ¦
        ¦ ~Black as the devil, hot as hell, pure as an angel, sweet as love.~                  ¦
        ¦                                                                                     ¦
        ¦  2.Americano   🇺🇸                            7. Green tea   💚                      ¦
        ¦                                                                                     ¦
        ¦             ~Without coffee something’s missing~                                    ¦
        ¦                                                                                     ¦
        ¦  3.Cappuccino     ☕                        8. Chai Latte    🕉                     ¦
        ¦                                                                                     ¦
        ¦          ~Learn from yesterday, live for today.~                                    ¦
        ¦                                                                                     ¦
        ¦  4. Cafe latte    🥛                                                                ¦
        ¦              ~Nothing will work unless you do.~                                     ¦
        ¦  5. Cortado      🇪🇸                                                                  ¦
        ¦                                                                                     ¦
        _______________________________________________________________________________________
        What kind of milk would you like?   🙂

        a. Semi-skinned            b. Whole milk
        c. Oat milk                d. No milk!


        Please, tell me how sweet you are:  💛
        1         2          3          4            5
        <O=========O==========O==========O============O>
        *1 means no sugar


        ¦_____________________________________________________________________________________¦
        """)
        beverage_nr = int(input("select something"))


        beverage_dictionary = {
        1: Beverage("espresso", "coffee"),
        2: Beverage("americano", "coffee", True, True),
        3: Beverage("tea", "tea")
        }

        milk_dictionary = {
        1: "Fat milk",
        2: "Oat milk"
        }


        selected_beverage = beverage_dictionary.get(beverage_nr)
        print("You have selected: " + selected_beverage.name)

        if selected_beverage.milk != None:
            print("Choose a type of milk pls: 1.Fat Milk or 2.Oat Milk")
            selected_milk = int(input())
            print("You selected " + milk_dictionary.get(selected_milk) + " type of milk")



        selected_beverage.milk_type = milk_dictionary.get(selected_milk)
        print("Modified beverage to contain:" + selected_beverage.milk_type)
