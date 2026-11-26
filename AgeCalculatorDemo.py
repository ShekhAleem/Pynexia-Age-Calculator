
# AgeCalculatorDemo.py <--------Main Project

from AgeExcept import InvalidDateError, FutureDateError
from AgeMenu import menu
from AgeOperations import calculate_age

while True:
    try:
        menu()

        ch = int(input("ENTER YOUR CHOICE: "))

        match(ch):

            case 1:
                try:
                    calculate_age()

                except InvalidDateError:
                    print("\t\tPLEASE ENTER A VALID DATE")

                except FutureDateError:
                    print("\t\tFUTURE DATE IS NOT ALLOWED")

            case 2:
                print("\t\tTHANKS FOR USING THIS PROGRAM")
                break

            case _:
                print("\t\tYOUR SELECTION IS WRONG -- TRY AGAIN")

    except ValueError:
        print("\tDON'T ENTER ALPHABETS / SYMBOLS FOR CHOICE")
