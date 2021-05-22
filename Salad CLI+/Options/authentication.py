import requests
from colorama import Fore
import json
import logging
from time import sleep


def get_auth_key():
    with open('./config.json') as f:
        js = json.load(f)
    salad_auth = js['salad_key']
    cookie = {"Salad.Authentication": salad_auth}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.5.3 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
    }
    return cookie, headers


def authenticate(url, cookie, headers, file_handler):
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    try:
        saladuser = requests.get(url=url,
                                 headers=headers, cookies=cookie, timeout=10)
        saladuser.raise_for_status()
        logger.info("Authentication succeeded.")

    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error:" + str(errh))
        print(f'{Fore.RED}AN ERROR OCCURRED DURING THE REQUEST FOR AUTHENTICATION!')
        if saladuser.status_code == 401:
            print(f'{Fore.RED}REPLACE YOUR SALAD AUTH CODE!')
            logger.error("REPLACE YOUR SALAD AUTH CODE!")
        sleep(20)

    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting:" + str(errc))
        print(f'{Fore.RED}CHECK YOUR INTERNET CONNECTION!')
        sleep(20)

    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", str(errt))
        print(f'{Fore.RED}TIMEOUT ERROR!')
        sleep(20)

    except requests.exceptions.RequestException as err:
        logger.error("Oops: Something Else:" + str(err))
        print(f'{Fore.RED}AN ERROR OCCURRED DURING THE REQUEST FOR AUTHENTICATION!')
        sleep(20)

    return saladuser
