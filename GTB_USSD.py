# GTB USSD Transfer *737#

def ussd_menu():
    print("Welcome to USSD Banking.")
    print("Please note that a N6.98 network charge will be applied to your bank account for banking services on this channel.\n")
    print("By clicking YES, you hereby consent to the processing of all personal data submitted in accordance with GTBank's Privacy Policy")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nProceeding to banking options...")
    elif choice == "2":
        print("\nYou have declined. Exiting...")
    else:
        print("\nInvalid input.")

ussd_menu()

# Variables
correct_pin = "1234"
current_balance = 350000
minimum_transaction_amount = 100
maximum_transaction_amount = 20000

def validate_pin(pin):
    if len(pin) != 4:
        print("Invalid Pin")
        return False
    elif pin != correct_pin:
        print("Incorrect Pin")
        return False
    return True

def check_balance(amount):
    if current_balance >= int(amount):
        return True
    else:
        print("Insufficient Balance")
        return False    

def validate_number(phone_number):
    if len(phone_number) != 11:
        print("Invalid Phone Number")
        return False
    return True 

def validate_amount(amount):
    amount = int(amount)
    if amount < minimum_transaction_amount or amount > maximum_transaction_amount:
        print(f"The requested amount is too low. Minimum transaction amount on this platform is N{minimum_transaction_amount}, maximum amount is N{maximum_transaction_amount}")
        return False
    return True

def validate_account_number(account_number):
    if len(account_number) != 10:
        print("Invalid account Number")
        return False
    return True 


option = input("1. Airtime-Self\n2. Airtime-Others\n3. Data\n4. Trsf-GTB\n5. Trsf-Others\n6. Transfers\n7. Cable TV\n8. Pay Bills\n9. Link BVN/NIN\n10. Next\n\n")

if option == "1":
    amount = input("Enter the amount:")
    if validate_amount(amount) and check_balance(amount):
        pin = input("Enter your pin \n 0.Back \n")
        if validate_pin(pin):
            print("You have successfully bought airtime of ", amount)
            current_balance -= int(amount)


if option == "2":
    amount = input("Enter the amount:")
    if validate_amount(amount) and check_balance(amount):
            phone_number = input("Enter phone number:")
            if validate_number(phone_number):
                pin = input("Enter your pin \n 0.Back \n")
                if validate_pin(pin):
                    print("You have successfully bought airtime of ", amount, " for ", phone_number)
                    current_balance -= int(amount)


# Bundle lists for each Network Provider
data_bundles = {
    "1": {  # MTN
        "1": ("75MB", 75),
        "2": ("1.230MB", 200),
        "3": ("1GB", 500)
    },
    "2": {  # Airtel
        "1": ("100MB", 100),
        "2": ("500MB", 300),
        "3": ("2GB", 1000)
    },
    "3": {  # Glo
        "1": ("90MB", 100),
        "2": ("1.25GB", 500),
        "3": ("2.5GB", 1000)
    },
    "4": {  # 9mobile
        "1": ("500MB", 200),
        "2": ("1.5GB", 500),
        "3": ("4.5GB", 1500)
    }
}

if option == "3":
    phone_number = input("Enter phone number:")
    if validate_number(phone_number):
        print("Select Network:\n1. MTN\n2. Airtel\n3. Glo\n4. 9mobile")
        network_provider = input("Enter option: ")

        if network_provider in ["1", "2", "3", "4"]:
            print("Select your Data Bundle:")
            provider_bundles = data_bundles[network_provider]
            for key in provider_bundles:
                name, price = provider_bundles[key]
                print(f"{key}. {name} - N{price}")

            data_bundle = input("Enter bundle option: ")

            if data_bundle in provider_bundles:
                bundle_name, amount = provider_bundles[data_bundle]
                if check_balance(amount):
                    pin = input("Enter your pin \n 0.Back \n")
                    if validate_pin(pin):  
                        print(f"You have successfully bought {bundle_name} - N{amount} for {phone_number}")      
                        current_balance -= amount


if option == "4":
    amount = input("Enter the amount:")
    if validate_amount(amount) and check_balance(amount):
        account_number = input("Enter account number:")
        if validate_account_number(account_number):
            pin = input("Enter your pin \n 0.Back \n")
            if validate_pin(pin):
                print("You have successfully transferred ", amount, " to GTBank account: ", account_number)
                current_balance -= int(amount)

bank_name = {
    "1": "Access Bank",
    "2": "Zenith Bank",
    "3": "UBA",
    "4": "First Bank",
    "5": "Fidelity Bank",
    "6": "Union Bank",
    "7": "Stanbic IBTC",
    "8": "Keystone Bank"
}

if option == "5":
    amount = input("Enter the amount: ")
    if validate_amount(amount) and check_balance(amount):
        account_number = input("Enter recipient account number: ")
        if validate_account_number(account_number):
            print("Select recipient bank:")

            for key in bank_name:
                print(f"{key}. {bank_name[key]}")
            bank_choice = input("Enter option: ")

            if bank_choice in bank_name:
                selected_bank = bank_name[bank_choice]
                pin = input("Enter your pin \n 0.Back \n")
                if validate_pin(pin):
                    current_balance -= int(amount)
                    print(f"You have successfully transferred {amount} to {account_number} at {selected_bank}")

