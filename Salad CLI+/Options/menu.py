import os
import time
import pyperclip
import webbrowser
from colorama import Fore
from options import authentication


def menu(saladuser, loginscreen, logo, cookie, headers, file_handler):

    os.system('cls')
    print(Fore.GREEN + loginscreen)
    print(f'{Fore.LIGHTRED_EX}Username {Fore.BLUE}> {Fore.YELLOW}' +
          str(saladuser['username']))
    print(f'{Fore.LIGHTRED_EX}Email {Fore.BLUE}> {Fore.YELLOW}' +
          str(saladuser['email']))
    print(f'{Fore.LIGHTRED_EX}User id {Fore.BLUE}> {Fore.YELLOW}' +
          str(saladuser['id']))
    print("\n\n")

    # Input Selection

    select = input(
        f"{Fore.CYAN}Select an option: {Fore.YELLOW}\n\n{Fore.YELLOW}1 - {Fore.WHITE}Start Mining \n{Fore.YELLOW}2 - {Fore.WHITE}Show Balance \n{Fore.YELLOW}3 - {Fore.WHITE}Show Lifetime Balance \n{Fore.YELLOW}4 - {Fore.WHITE}Show XP \n{Fore.YELLOW}5 - {Fore.WHITE}Show Earning Graph \n{Fore.YELLOW}6 - {Fore.WHITE}Copy Referral Code \n{Fore.YELLOW}7 - {Fore.WHITE}Open Salad Store \n{Fore.YELLOW}8 - {Fore.WHITE}Help{Fore.GREEN} \n{Fore.YELLOW}x - {Fore.WHITE}Exit\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")

    if select == "1":
        from options import mining
        mining.choose_pool(logo)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "2":
        from options import balance
        balance.show_balance(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "3":
        from options import lifetime
        lifetime.show_lifetime(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "4":
        from options import xp
        xp.show_experience(logo, cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "5":
        from options import salad_earnings_update
        salad_earnings_update.get_history(cookie, headers, file_handler)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "6":
        referral = authentication.authenticate('https://app-api.salad.io/api/v1/profile/referral-code',
                                               cookie, headers, file_handler)
        referral = referral.json()
        pyperclip.copy('Support me and use code ' + str(
            referral['code']) + ' for a 2x earning rate bonus on Salad! https://www.salad.com')
        print(f'\nCode copied to clipboard!')
        time.sleep(2)
        menu(saladuser, loginscreen, logo, cookie, headers, file_handler)

    elif select == "7":
        webbrowser.open('http://app.salad.io')

    elif select == "8":
        webbrowser.open('https://discord.gg/D2VBbJDz8c')

    elif select == "x":
        exit()
