from utils.all_utils import encryption as e, decryption as d
import sys

def main():
    print("\nChoose What action you want to perform : \n\n Enter 1 for Encryption \n Enter 2 for Decryption\n\n")
    while True:
        try:
            action = int(input("Enter your option here =  "))
        except ValueError:
            print("Sorry, I didn't understand that.\n")
            continue

        if action == 1:
            e.encrypt()
        elif action == 2:
            d.decrypt()
        elif action == 0:
            sys.exit("\n-> Successfully Exited from program, Thank You...")

        else:
            print("\nSelect any one option either 1 or 2, otherwise enter 0 to exit\n")
            continue

main()