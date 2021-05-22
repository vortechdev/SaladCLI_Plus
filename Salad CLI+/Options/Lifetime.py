import os
import requests
import sys
from time import sleep
from colorama import Fore, Back
from options import authentication


def show_lifetime(logo, cookie, headers, file_handler):
    sys.stdout.write("\x1b]2;Lifetime Balance\x07")
    while True:
        os.system('cls')
        balance = authentication.authenticate('https://app-api.salad.io/api/v1/profile/balance',
                                              cookie, headers, file_handler)
        balance = balance.json()

        print(Fore.GREEN + logo)

        print(f'{Fore.LIGHTRED_EX}Lifetime Balance {Fore.BLUE}> {Fore.YELLOW}$' +
              str(balance['lifetimeBalance']))
        print(Fore.GREEN)
        print('-------------------------------------')

        try:
            print(
                f'\n{Fore.GREEN}Press {Fore.RED}ctrl+c {Fore.GREEN}to Return to the menu!')
            sleep(5)
        except (KeyboardInterrupt):
            return False
