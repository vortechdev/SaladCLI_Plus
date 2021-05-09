import os
import time
import sys
from time import sleep
import json
from colorama import Fore, Back

with open('./Art/art.txt', encoding='utf-8') as f:
    art = f.read()

with open('config.json') as f:
    js = json.load(f)
wallet = js['wallet']

sys.stdout.write("\x1b]2;Choose miner...\x07")

print(Fore.GREEN + art)

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
    os.system('python "./Start.py"')

os.system("cls")
print(Fore.GREEN + art)

select = input(
    f"{Fore.YELLOW}Miners are listed from 'best' to 'worst'.\n\n{Fore.BLACK}{Back.CYAN}Cyan{Back.BLACK}{Fore.YELLOW} = GPU Miner\n{Fore.BLACK}{Back.GREEN}Green{Back.BLACK}{Fore.YELLOW} = CPU Miner\n\n\n{Fore.CYAN}Select a miner: \n\n{Fore.YELLOW}{Fore.YELLOW}1 - {Fore.CYAN}T-rex (Ethash) \n{Fore.YELLOW}2 - {Fore.CYAN}NBMiner (Ethash) \n{Fore.YELLOW}3 - {Fore.CYAN}Phoenixminer (Ethash) \n{Fore.YELLOW}4 - {Fore.CYAN}ETHMiner (Ethash) \n{Fore.YELLOW}5 - {Fore.CYAN}Gminer (BeamhashIII) \n{Fore.YELLOW}6 - {Fore.CYAN}T-rex (KawPow) \n{Fore.YELLOW}7 - {Fore.CYAN}XMRig nVidia (KawPow) \n{Fore.YELLOW}8 - {Fore.CYAN}XMRig AMD (KawPow) \n{Fore.YELLOW}9 - {Fore.GREEN}XMRig (RandomXMonero)\n\n{Fore.YELLOW}Type {Fore.RED}exit {Fore.YELLOW}to exit.\n\n{Fore.GREEN}Select {Fore.BLUE}>> {Fore.GREEN}")

if select == "1":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\Trex\t-rex.exe --algo ethash --url stratum+tcp://daggerhashimoto." +
              region + ".nicehash.com:3353 --user " + (wallet))

if select == "2":
    os.system("OptimizeGPU.bat")
    os.system(
        r"Miners\NBMiner\nbminer.exe -a ethash -o nicehash+tcp://daggerhashimoto." + region + ".nicehash.com:3353 -u " + (wallet) + r" -d 0 --no-watchdog")

if select == "3":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\PhoenixMiner-5.4c\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto." +
              region + ".nicehash.com:3353 -ewal " + (wallet) + " -esm 3 -allpools 1 -allcoins 0")

if select == "4":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\ETHMiner\ethminer.exe -P stratum2+tcp://" +
              (wallet) + r"@daggerhashimoto." + region + ".nicehash.com:3353 -U")

if select == "5":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\Gminer\miner.exe -a beamhashIII --proto stratum --server beamv3." +
              region + ".nicehash.com:3387 -u " + (wallet))

if select == "6":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\Trex\t-rex.exe --algo kawpow --url stratum+tcp://kawpow." +
              region + ".nicehash.com:3385 --user " + (wallet))

if select == "7":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\XMRig-6.7.0\xmrig.exe --no-cpu --cuda -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
              (wallet) + r" -k --nicehash")

if select == "8":
    os.system("OptimizeGPU.bat")
    os.system(r"Miners\XMRig-amd-2.14.6\xmrig-amd.exe --donate-level=1 -a kawpow -o stratum+tcp://kawpow." + region + ".nicehash.com:3385 -u " +
              (wallet) + r" -k --nicehash")

if select == "9":
    os.system("cls")
    os.system(r"Miners\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero." + region + ".nicehash.com:3380 --coin=monero -u " +
              (wallet) + r" -k --nicehash")

if select == "exit":
    os.system("python ../Start.py")
