import requests
import pygame
import time
from colorama import init, Fore, Style
import random
from datetime import datetime


init()
address_target= input("enter your address:\t")
array_tokens=[]
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def print_random_color_text(text):
    color = random.choice(colors)  # Select a random color
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    print(f"{color}[{current_time}] {text}{Style.RESET_ALL}") 
    
while(True):
    burp0_url = "https://api-v2.solscan.io:443/v2/account/transfer?address="+address_target+"&page=1&page_size=10&remove_spam=false&exclude_amount_zero=false"
    burp0_cookies = {"cf_clearance": "IIUDJI2XmxYTg8P3b3gtJ5oQuRhiRaVEhnHfTdVEmrM-1726640722-1.2.1.1-hJ79kmABSv2d0YCAPnAwML9eBoHpJUsQgGmV_OdLE7egoaffESsbHq3GdVqRKWBQKNFOu.C3KnSkcjON9h3WpF4j.gBW.r4.GlNWXpG2tJHF6WELAFEjltUiTD7ncr_znYXPHKJIugplkHriBR_Qukzsf07tzhOZ07sPvleg2a2zvKNIZje3zucV_fJIac6c9ubm0bXxbtMvqypPf3OF1EPIk6hL4k9zXvpVL8_3DGnsTNVl3sXqBfyFw9M6AyXASTa8yHYcGk8iFZ3kI9PMmd7nKRVwzgaoxUkIMRKEI0s7wryC_D8.Y9sL2WhYHqoUvwP62jAwKSnc4irWNfbUCCpMeSFP_RfcdrPQ_o8RVEw", "_ga_PS3V7B7KV0": "GS1.1.1726640724.1.1.1726640734.0.0.0", "_ga": "GA1.1.907507646.1726640725"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Sol-Aut": "dnJLEUQ9j1LY6=hCoi6yYzB9dls0fKb0y8YDbBx=", "Origin": "https://solscan.io", "Referer": "https://solscan.io/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "If-None-Match": "W/\"1ce0-XBe+4SXjE/EePiQ6PtaPs918FNU\"", "Te": "trailers"}
    res = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    res = res.json()
    for item in res['data']:
        if 'So11111111' not in  item['token_address'] and item['token_address']  not in array_tokens:
            print_random_color_text(item['token_address'])
            pygame.mixer.init()
            sound = pygame.mixer.Sound('sound.wav')
            sound.play()
            pygame.time.delay(1000) 
            time.sleep(1)
            print
            array_tokens.append(item['token_address'])
    time.sleep(5)
