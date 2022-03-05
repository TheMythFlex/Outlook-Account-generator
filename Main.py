
try:
    import colorama
    import ctypes
    import names
    import requests
    import multiprocessing.pool as mpool
    import uuid
    import logging
    import secrets
    import base64
    import datetime
    import os
    import random
    import re
    import threading
    import time
    import zipfile
    from selenium.webdriver.common.by import By
    from nordvpn_connect import initialize_vpn, rotate_VPN
    from selenium.webdriver.chrome.options import Options
    import requests
    import uuid
    from selenium import webdriver
    from selenium.webdriver import DesiredCapabilities, ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from termcolor import colored
    from selenium.webdriver.common.proxy import Proxy, ProxyType
except Exception as e:
    print(e)

colorama.init()

def genrandomusername():
    loademail = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm") for x in range(10))

    return loademail + "flextools"


def genrandompassword():
    load_pass = ''.join(random.choice("123456789qwertyuiopasdfghjklzxcvbnm") for x in range(6))

    return load_pass + "%Flextools"

s = requests.session()

account_counter = 0
failed_accounts = 0

print(colored("""
                
                ░█████╗░██╗░░░██╗████████╗██╗░░░░░░█████╗░██╗░░██╗██╗░░██╗    ░██████╗░███████╗███╗░░██╗
                ██╔══██╗██║░░░██║╚══██╔══╝██║░░░░░██╔══██╗██║░██╔╝██║░██╔╝    ██╔════╝░██╔════╝████╗░██║
                ██║░░██║██║░░░██║░░░██║░░░██║░░░░░██║░░██║█████═╝░█████═╝░    ██║░░██╗░█████╗░░██╔██╗██║
                ██║░░██║██║░░░██║░░░██║░░░██║░░░░░██║░░██║██╔═██╗░██╔═██╗░    ██║░░╚██╗██╔══╝░░██║╚████║
                ╚█████╔╝╚██████╔╝░░░██║░░░███████╗╚█████╔╝██║░╚██╗██║░╚██╗    ╚██████╔╝███████╗██║░╚███║
                ░╚════╝░░╚═════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝    ░╚═════╝░╚══════╝╚═╝░░╚══╝
                
                                                                 Dev Flex#8629
                                                                                                 
""", "blue", attrs=["bold"]))

openproxyfile = open("proxy.txt", "r")
proxies = openproxyfile.readlines()
proxycount = 0
for line in proxies:
    proxycount += 1

def  Main():
    global account_counter, proxycount, driver, failed_accounts
    while True:
        try:
            email = genrandomusername()
            password = genrandompassword()
            first_name = names.get_first_name(gender='male')
            last_name = names.get_last_name()

            print("\n")
            ctypes.windll.kernel32.SetConsoleTitleW("Outlook Account Gen - Made by Flex#8629 | Accounts Created: {} | Accounts Failed {}".format(account_counter,failed_accounts))
            proxytouse = proxies[random.randint(1, proxycount - 1)]
            PROXY = proxytouse
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--log-level=3")
            os.environ['WDM_LOG_LEVEL'] = '0'
            chrome_options.add_argument(
                'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            chrome_options.add_argument('--profile-directory=Default')  #
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--disable-site-isolation-trials')
            chrome_options.add_argument('--disable-application-cache')
            chrome_options.add_argument("window-size=500,500")
            logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
            logger.setLevel(logging.WARNING)
            chrome_options.add_argument('--proxy-server=%s' % PROXY)

            driver = webdriver.Chrome(options=chrome_options)

            print(colored("[+] Creating Account", "green", attrs=["bold"]))

            driver.get("https://outlook.live.com/owa/")

            driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/div").click()

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input").send_keys(email)

            print(colored("[-] Email Set To " + email + "@outlook.com", "magenta", attrs=["bold"]))

            time.sleep(0.5)

            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input").click()
            except:
                driver.find_element(By.ID, "iSignupAction").click()

            time.sleep(3)

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]").send_keys(password)

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[7]/div/div/div[2]/input").click()

            print(colored("[-] Password Set To " + password, "magenta", attrs=["bold"]))

            time.sleep(3)

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[1]/input").send_keys(first_name)

            print(colored("[-] First Name Set To " + first_name, "magenta", attrs=["bold"]))

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[2]/input").send_keys(last_name)

            print(colored("[-] Last Name Set To " + last_name, "magenta", attrs=["bold"]))

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[2]/div/div/div[2]/input").click()

            time.sleep(3)

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select/option[11]").click()
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select/option[11]").click()
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[3]/input").send_keys("1995")

            print(colored("[-] DOB Set To 10/10/1995", "magenta", attrs=["bold"]))

            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[6]/div/div/div[2]/input").click()

            time.sleep(6)

            print(colored("[-] Waiting On User To Solve Captcha.... ", "red", attrs=["bold"]))

            while True:
                if "Please solve the puzzle so we know you're not a robot." in driver.page_source:
                    pass
                else:
                    if "Stay signed in?" in driver.page_source:
                        account_counter += 1
                        ctypes.windll.kernel32.SetConsoleTitleW(
                            "Outlook Account Gen - Made by Flex#8629 | Accounts Created: {} | Accounts Failed {}".format(
                                account_counter, failed_accounts))
                        print(colored("[+] Account Created Saved to Outlook Accounts.txt | {}:{}".format(email + "@outlook.com", password),"green", attrs=["bold"]))
                        saveaccount = open("OutLook Accounts.txt", "a")
                        saveaccount.writelines("{}:{}\n".format(email + "@outlook.com", password))
                        saveaccount.close()
                        driver.quit()
                        break

        except Exception as e:
            failed_accounts += 1
            print(colored("[+] an error has occurred", "red", attrs=["bold"]))
            Main()
            driver.quit()

for i in range(1):
    x = threading.Thread(target=Main)
    x.start()
