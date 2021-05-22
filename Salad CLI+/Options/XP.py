import os
import requests
import sys
from time import sleep
from colorama import Fore, Back
from options import authentication


def show_experience(logo, cookie, headers, file_handler):
    sys.stdout.write("\x1b]2;Experience\x07")
    while True:
        os.system('cls')
        experience = authentication.authenticate('https://app-api.salad.io/api/v1/profile/xp',
                                                 cookie, headers, file_handler)
        experience = experience.json()

        print(Fore.GREEN + logo)

        print(f'{Fore.LIGHTRED_EX}Experience {Fore.BLUE}> {Fore.YELLOW}' +
              str(experience['lifetimeXp']) + ' XP')
        print(Fore.GREEN)
        print('-------------------------------------')

        try:
            print(
                f'\n{Fore.GREEN}Press {Fore.RED}ctrl+c {Fore.GREEN}to Return to the menu!')
            sleep(5)
        except (KeyboardInterrupt):
            return False
