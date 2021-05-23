import os
import time
import sys
from time import sleep
import json
from colorama import Fore, Back


def choose_pool(logo):
    os.system('cls')

    sys.stdout.write("\x1b]2;Choose mining region.\x07")

    print(Fore.GREEN + logo)

    select_pool = input(
        f"{Fore.CYAN}Select a pool: \n\n{Fore.YELLOW}1 - {Fore.CYAN}Nicehash \n{Fore.YELLOW}2 - {Fore.CYAN}Ethermine \n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}"
    )

    if select_pool == "1":
        # Select Region
        os.system('cls')

        sys.stdout.write("\x1b]2;Choose mining region.\x07")

        print(Fore.GREEN + logo)

        select_region = input(
            f"{Fore.CYAN}Select a pool region: \n\n{Fore.YELLOW}1 - {Fore.CYAN}EU-West \n{Fore.YELLOW}2 - {Fore.CYAN}EU-North \n{Fore.YELLOW}3 - {Fore.CYAN}USA-West \n{Fore.YELLOW}4 - {Fore.CYAN}USA-East \n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}"
        )

        if select_region == "1":
            region = "eu-west"

        if select_region == "2":
            region = "eu-north"

        if select_region == "3":
            region = "usa-west"

        if select_region == "4":
            region = "usa-east"

        if select_region == "exit":
            return False

        # Additional miner commands

        os.system("cls")
        print(Fore.GREEN + logo)

        miner_commands = input(
            f"{Fore.CYAN}Type additional miner commands here (optional) \nPress enter to skip. \n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}"
        )

        # Select miner

        os.system("cls")
        print(Fore.GREEN + logo)

        with open('config.json') as f:
            js = json.load(f)
        nicehash_wallet = js['nicehash_wallet']

        select = input(
            f"{Fore.YELLOW}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.YELLOW} = GPU Miner\n{Fore.BLACK}{Back.GREEN}Green{Back.BLACK}{Fore.YELLOW} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.YELLOW}{Fore.YELLOW}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.YELLOW}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.YELLOW}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.YELLOW}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.YELLOW}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.YELLOW}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.YELLOW}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.YELLOW}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.YELLOW}9 - {Fore.CYAN}Gminer (Zhash) \n{Fore.YELLOW}10 - {Fore.GREEN}XMRig (RandomXMonero)\n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")

        if select == "1":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 --user " + (nicehash_wallet) + " " + (miner_commands))

        if select == "2":
            os.system("OptimizeGPU.bat")
            os.system(
                r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (nicehash_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

        if select == "3":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
                      region + ".nicehash.com:3353 -ewal " + (nicehash_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

        if select == "4":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
                      (nicehash_wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U" + " " + (miner_commands))

        if select == "5":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
                      region + ".nicehash.com:3387 -u " + (nicehash_wallet) + " " + (miner_commands))

        if select == "6":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
                      region + ".nicehash.com:3385 --user " + (nicehash_wallet) + " " + (miner_commands))

        if select == "7":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-6.7.0\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "8":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\XMRig-amd-2.14.6\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "9":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Gminer\miner.exe -a 144_5 --pers auto --proto stratum --server zhash." +
                      region + ".nicehash.com:3369 -u " + (nicehash_wallet) + " " + (miner_commands))

        if select == "10":
            os.system("cls")
            os.system(r"Miners\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
                      (nicehash_wallet) + r" -k --nicehash" + " " + (miner_commands))

        if select == "exit":
            return False

        sleep(10)
        return False

    if select_pool == "2":
        # Select Region
        os.system('cls')

        sys.stdout.write("\x1b]2;Choose mining region.\x07")

        print(Fore.GREEN + logo)

        select_region = input(
            f"{Fore.CYAN}Select a pool region: \n\n{Fore.YELLOW}1 - {Fore.CYAN}Europe \n{Fore.YELLOW}2 - {Fore.CYAN}Asia \n{Fore.YELLOW}3 - {Fore.CYAN}USA-West \n{Fore.YELLOW}4 - {Fore.CYAN}USA-East \n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}"
        )

        if select_region == "1":
            region = "eu1"

        if select_region == "2":
            region = "asia1"

        if select_region == "3":
            region = "us2"

        if select_region == "4":
            region = "us1"

        if select_region == "exit":
            return False

        # Additional miner commands

        os.system("cls")
        print(Fore.GREEN + logo)

        miner_commands = input(
            f"{Fore.CYAN}Type additional miner commands here (optional) \nPress enter to skip. \n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}"
        )

        # Select miner

        os.system("cls")
        print(Fore.GREEN + logo)

        with open('config.json') as f:
            js = json.load(f)
        ethermine_wallet = js['ethermine_wallet']

        select = input(
            f"{Fore.YELLOW}Miners are listed from 'best' to 'worst'.\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.YELLOW}{Fore.YELLOW}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.YELLOW}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.YELLOW}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.YELLOW}4 - {Fore.CYAN}ETHMiner (Ethash) \n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")

        if select == "1":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+ssl://" +
                      region + ".ethermine.org:5555 --user " + (ethermine_wallet) + " " + (miner_commands))

        if select == "2":
            os.system("OptimizeGPU.bat")
            os.system(
                r"Miners\NBMiner\nbminer.exe -a ethash -o stratum+ssl://" + region + ".ethermine.org:5555 -u " + (ethermine_wallet) + r" -d 0 --no-watchdog" + " " + (miner_commands))

        if select == "3":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\PhoenixMiner-5.6d\PhoenixMiner.exe -rmode 0 -rvram 1 -log 0 -pool ssl://" +
                      region + ".ethermine.org:5555 -ewal " + (ethermine_wallet) + " -esm 3 -allpools 1 -allcoins 0" + " " + (miner_commands))

        if select == "4":
            os.system("OptimizeGPU.bat")
            os.system(r"Miners\ETHMiner\ethminer.exe -P stratum+ssl://" +
                      (ethermine_wallet) + r"@" + region + ".ethermine.org:5555" + " " + (miner_commands))

        if select == "exit":
            return False

        sleep(10)
        return False
