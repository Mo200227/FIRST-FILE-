class Vendingmachine:
    def __init__(self,soda,water,coffee):
        self.soda = soda
        self.water = water
        self.coffee = coffee

    def purchase(self, drink_type):
        if drink_type == 1:
            if self.soda > 0:
                print("Enjoy your Soda!")
                self.soda -= 1
            else:
                print("Sorry, Soda is out of stock.")
        elif drink_type == 2:
            if self.coffee > 0:
                print("Enjoy your Coffee!")
                self.coffee -= 1
            else:
                print("Sorry, Coffee is out of stock.")
        elif drink_type == 3:
            if self.water > 0:
                print("Enjoy your Water!")
                self.water -= 1
            else:
                print("Sorry, Water is out of stock.")
        else:
            print("Invalid drink type. Please enter a valid option.")

    def restock(self, drink_type, amount):
        if drink_type == 1:
            self.soda += amount
        elif drink_type == 2:
            self.coffee += amount
        elif drink_type == 3:
            self.water += amount
        else:
            print("Invalid drink type. Please enter a valid option.")

    def report_inventory(self):
        print("Inventory")
        print(f"Soda: {self.soda} bottles")
        print(f"Coffee: {self.coffee} bottles")
        print(f"Water: {self.water} bottles")

vending_machine = Vendingmachine(10, 10, 10)

while True:
    command = input(":> ").lower()

    if command in ['quit', 'q']:
        break
    elif command == 'buy':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        drink_type = int(input(":> "))
        vending_machine.purchase(drink_type)
    elif command == 'restock':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        drink_type = int(input(":> "))
        amount = int(input("Please enter an amount: "))
        vending_machine.restock(drink_type, amount)
    elif command == 'inventory':
        vending_machine.report_inventory()
    else:
        print("Invalid command. Please enter a valid command.")



    

