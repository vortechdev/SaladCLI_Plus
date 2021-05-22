import sys
import os
import logging
from options import authentication, menu
from art import art


def main():
    # Configure logging
    formatter = logging.Formatter(
        '%(levelname)s  -  %(asctime)s  -  %(name)s  |  %(message)s')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('logs.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Get art
    loginscreen = art.read_art('./art/Login screen.txt')
    logo = art.read_art('./art/art.txt')

    # Clear screen
    os.system('cls')
    sys.stdout.write("\x1b]2;Salad CLI+ | By Walkx\x07")

    # Get Auth
    cookie, headers = authentication.get_auth_key()
    saladuser = authentication.authenticate('https://app-api.salad.io/api/v1/profile',
                                            cookie, headers, file_handler)
    saladuser = saladuser.json()

    # Open menu
    menu.menu(saladuser, loginscreen, logo, cookie, headers, file_handler)


if __name__ == "__main__":
    main()
