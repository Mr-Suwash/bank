# User interface (command-line menu)
from passwordss import encrypt_password, verify_password, decrypt_password
from bank import Bank
from account import Account
import random
def main():
    bank = Bank()
    logged_in_user = None

    while True:
        if not logged_in_user:
            print("\n --- BANK MENU ---")
            print("1. Add new admin")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")
            if choice == "1":
                name = input("Enter user name: ")
                print("1. Create password manually")
                print("2. Randomly generate password")
                cho = input("Enter choice: ")

                if cho == "1":
                    raw_password = input("Create password: ")
                elif cho == "2":
                    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+"
                    raw_password = ''.join(random.choice(letters) for _ in range(11))
                    print(f"Your password is {raw_password}")

                 #  Encrypt password before saving
                
                acc = Account(0, name)
                hashed_password = encrypt_password(raw_password)
 
                  # Save user with hashed password
                bank.add_user(name, 0, hashed_password)
                print(f"Admin '{name}' added successfully!")

                

            elif choice == "2":
                username = input("Enter your username: ").strip()  # remove leading/trailing spaces
                password = input("Enter your password: ").strip()

                
                  
                found_user = None
                for acc_no, account in bank.accounts.items():   #.items() method of a dictionary returns both keys and values together.
                    if account.name == username and verify_password(password, account.password):
                        found_user = acc_no
                        break


                if found_user is not None:
                    logged_in_user = found_user
                    print(f" Login successful! Welcome {username}.")
                else:
                    print(" Invalid username or password. Try again.")
            elif choice == "3":
                print(" Exiting...")
                break

            else:
                print(" Invalid choice, try again.")
   
        else:
            # Logged-in menu
            acc = bank.accounts[logged_in_user]
            print("\n--- ADMIN ACCOUNT MENU ---")
            print("1. Add Account")
            print("2. Deposit to Account")
            print("3. Withdraw from Account")
            print("4. Check Account Balance")
            print("5. View Account History")
            print("6. Delete Account")
            print("7. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter account holder's name: ")
                balance = float(input("Enter initial deposit: "))
                acc_no = bank.add_user(name, balance)
                print(f" Account created with Account No: {acc_no}")

            elif choice == "2":
                acc_no = int(input("Enter account number to deposit: "))
                amount = float(input("Enter amount to deposit: "))
                if bank.deposit(acc_no, amount):
                    print(" Deposit successful.")
                else:
                    print(" Deposit failed.")

            elif choice == "3":
                acc_no = int(input("Enter account number to withdraw: "))
                amount = float(input("Enter amount to withdraw: "))
                if bank.withdraw(acc_no, amount):
                    print(" Withdrawal successful.")
                else:
                    print(" Withdrawal failed (check balance).")

            elif choice == "4":
                acc_no = int(input("Enter account number: "))
                balance = bank.get_balance(acc_no)
                if balance is not None:
                    print(f" Balance: {balance}")
                else:
                    print(" Account not found.")

            elif choice == "5":
                acc_no = int(input("Enter account number: "))
                history, name = bank.get_history(acc_no)
                if history:
                    print(f"\n Transaction History for {name}:")
                    for record in history:
                        print(" -", record)
                else:
                    print(" No history or account not found.")

            elif choice == "6":
                acc_no = int(input("Enter account number to delete: "))
                if bank.delete_user(acc_no):
                    print(" Account deleted.")
                else:
                    print(" Account not found.")

            elif choice == "7":
                print(" Admin logged out.")
                logged_in_user = None
                break

            else:
                print(" Invalid choice, try again.")


if __name__ == "__main__":
    main()
