import schedule
import utils
import config as cfg
from numpy import random
import keyboard


def main():
    print("\nWhat would you like to do?\n")
    tog = int(input("1. Open a random sub.\n2. Display a cum schedule.\n3. Open a random 'ExposedToStrangers' video.\n\n"))

    if tog == 1:
        tog1 = int(input(
            "\n\n1. Pick your own censor level.\n2. Let it be random.\nPress any other key to let the value from the config file be taken.\n\n"))
        if tog1 == 1:
            n1n = int(input(
                "\n\nEnter your censor level.\n0 is full nudity.\n1 is barely/occasionally.\n2 is completely non-nude.\n\n"))
            utils.random_sub(n1n)
        elif tog1 == 2:
            utils.random_sub(random.randint(0, 3))
        else:
            utils.random_sub(cfg.n)

    elif tog == 2:
        tog2 = int(input(
            "\n1. Choose the number of days and nudity level.\nPress any other key to let the config numbers be taken.\n\n"))
        if tog2 == 1:
            n2 = int(input(
                "\nEnter your censor level.\n0 is full nudity.\n1 is barely/occasionally.\n2 is completely non-nude.\n\n"))
            days2 = int(input("\nEnter the number of days.\n"))
            result = schedule.schedule(n2, days2)
        else:
            result = schedule.schedule(cfg.n, cfg.days)
        print("How would you like your result?\n")
        print_type = int(input("1. As a table.\n2. As a list.\n\n"))
        if print_type == 1:
            print(result)
        elif print_type == 2:
            schedule.lines(result)

    elif tog == 3:
        utils.random_ets()

    end = input("Do you want to start again? (Y/n)\n").lower()
    if end == "y":
        main()

    print("Press any key to continue")
    keyboard.read_key()
    print()


main()
