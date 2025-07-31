
users = {
    "SBI": {"pin": 3456, "balance": 100},
    "ICICI": {"pin": 4986, "balance": 10},
    "INDIAN": {"pin": 1239, "balance": 200}
}

card_name = input("Enter your card name: ")

if card_name in users:
    pin = int(input("Enter your PIN: "))
    if pin == users[card_name]["pin"]:
        print(f"\nWelcome, {card_name}!")
        while True:
            print("\nChoose your option:")
            print("1. Withdraw")
            print("2. Check Balance")
            print("3. Add Money")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            def withdraw():
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= users[card_name]["balance"]:
                    users[card_name]["balance"] -= amount
                    print("Please wait for transaction...")
                    print("Transaction successful. Remaining balance:", users[card_name]["balance"])
                else:
                    print("Insufficient bank balance:", users[card_name]["balance"])

            def check_balance():
                print("Your balance:", users[card_name]["balance"])

            def add_money():
                amount = int(input("Enter the amount to add: "))
                users[card_name]["balance"] += amount
                print("Money added successfully.")
                print("Your current balance is:", users[card_name]["balance"])

            if choice == 1:
                withdraw()
            elif choice == 2:
                check_balance()
            elif choice == 3:
                add_money()
            elif choice == 4:
                print("Thank you for using our ATM service.")
                break;
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Wrong PIN.")
else:
    print("Card not found.")
