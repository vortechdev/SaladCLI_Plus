import os
import time
import requests
import sys
import pyperclip
import json
import webbrowser
from colorama import Fore, Back

os.system("cls")
sys.stdout.write("\x1b]2;Salad CLI+ | By Walkx\x07")

with open('config.json') as f:
    js = json.load(f)
salad_auth = js['salad_key']
cookie = {
    "Salad.Authentication": salad_auth
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.5.3 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
}
with open('./Art/Login screen.txt', encoding='utf-8') as f:
    loginscreen = f.read()


sladusr = requests.get(
    url='https://app-api.salad.io/api/v1/profile', headers=headers, cookies=cookie)
if sladusr.status_code != 200:
    print(f'{Fore.RED}REPLACE YOUR SALAD AUTH CODE!')
    input(f'{Fore.RED}Press Enter to Exit...')
sladusr = sladusr.json()

rfrl = requests.get(url='https://app-api.salad.io/api/v1/profile/referral-code',
                    headers=headers, cookies=cookie)
if rfrl.status_code != 200:
    print(f'{Fore.RED}REPLACE YOUR SALAD AUTH CODE!')
    input(f'{Fore.RED}Press Enter to Exit...')
rfrl = rfrl.json()

print(Fore.GREEN + loginscreen)
print(f'{Fore.LIGHTRED_EX}Username {Fore.BLUE}> {Fore.YELLOW}' +
      str(sladusr['username']))
print(f'{Fore.LIGHTRED_EX}Email {Fore.BLUE}> {Fore.YELLOW}' +
      str(sladusr['email']))
print(f'{Fore.LIGHTRED_EX}User id {Fore.BLUE}> {Fore.YELLOW}' +
      str(sladusr['id']))
print("\n\n")


# Input Selection
select = input(
    f"{Fore.CYAN}Select an option: {Fore.YELLOW}\n\n{Fore.YELLOW}1 - {Fore.WHITE}Start Mining \n{Fore.YELLOW}2 - {Fore.WHITE}Show Balance \n{Fore.YELLOW}3 - {Fore.WHITE}Show Lifetime Balance \n{Fore.YELLOW}4 - {Fore.WHITE}Show XP \n{Fore.YELLOW}5 - {Fore.WHITE}Show Earning Graph \n{Fore.YELLOW}6 - {Fore.WHITE}Copy Referral Code \n{Fore.YELLOW}7 - {Fore.WHITE}Open Salad Store \n{Fore.YELLOW}8 - {Fore.WHITE}Help\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")
if select == "1":
    os.system('python ./Options/Mining.py')

if select == "2":
    os.system('python ./Options/Balance.py')

if select == "3":
    os.system('python ./Options/Lifetime.py')

if select == "4":
    os.system('python ./Options/XP.py')

if select == "5":
    os.system('python ./Options/salad_earnings_update.py')

if select == "6":
    pyperclip.copy('Support me and use code ' +
                   str(rfrl['code']) + ' for a 2x earning rate bonus on Salad! https://www.salad.com')
    print(f'\nCode copied to clipboard!')
    time.sleep(2)

if select == "7":
    webbrowser.open('http://app.salad.io')

os.system('python Start.py')
