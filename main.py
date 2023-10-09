#https://youtube.com/its54m
#enjoy the vending machine :]


























class VendingMachine:
    def __init__(self):
        self.products = {
            'A1': {'name': 'Soda 🥤', 'price': 1.50, 'quantity': 5},
            'A2': {'name': 'Chips 🍟', 'price': 1.00, 'quantity': 7},
            'B1': {'name': 'Chocolate 🍫', 'price': 2.00, 'quantity': 3},
            'B2': {'name': 'Candy 🍬', 'price': 0.75, 'quantity': 10}
        }
      #change this to your liking :]
        self.balance = 1.0

    def display_products(self):
        print("Available Products:")
        for code, product in self.products.items():
            print(f"{code}: {product['name']} - ${product['price']}")

    def insert_coins(self, amount):
        self.balance += amount

    def select_product(self, code):
        if code not in self.products:
            print("Invalid product code.")
            return

        product = self.products[code]
        if product['quantity'] <= 0:
            print("Product is out of stock.")
            return

        if self.balance < product['price']:
            print("Insufficient balance.")
            return

        self.balance -= product['price']
        product['quantity'] -= 1
        print(f"Dispensing {product['name']}.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def return_change(self):
        print(f"Returning change: ${self.balance:.2f}")
        self.balance = 0.0


vending_machine = VendingMachine()

while True:
    print("https://youtube.com/@its54m\n=======================================\n👋 | Welcome to the Vending Machine!")
    print("[1] Display Products")
    print("[2] Insert Money")
    print("[3] Select Product")
    print("[4] Check Balance")
    print("[5] Return Change")
    print("[6] Exit")
    choice = input("> Enter your choice: ")
    print('=======================================')
    if choice == '1':
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        vending_machine.display_products()
        print('=======================================')
    elif choice == '2':
        amount = float(input("Enter the amount of money to insert: "))
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        vending_machine.insert_coins(amount)
        print('=======================================')
    elif choice == '3':
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        code = input("Enter the product code: ")
        vending_machine.select_product(code)
        print('=======================================')
    elif choice == '4':
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        vending_machine.check_balance()
        print('=======================================')
    elif choice == '5':
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        vending_machine.return_change()
        print('=======================================')
    elif choice == '6':
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        print("Thank you for using the Vending Machine. \n  @its54m™ 2023.")
        import time
        time.sleep(3)
        break
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
    else:
      
        import os
      
        def clear_output():
          os.system('cls' if os.name == 'nt'           else 'clear')

        clear_output()
        print("❌ Invalid choice. Please try again.")
        print('=======================================')
