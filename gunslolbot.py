#import requests
#import os
#import time
#proxylist=[]
#url="https://guns.lol/sh3dowkkk"
#with open("dosya.txt", "r", encoding="utf-8") as file:
#    for satir in file:
#        proxylist.append(satir)
#
#socks5proxylist=[""]
#for socks5proxy in proxylist:
#    tt="socks5://"+socks5proxy
#    socks5proxylist.append(tt)
#print(socks5proxylist)
#for  ff in socks5proxylist :
#    time.sleep(0.5)
#    os.system("cls")
#    try:
#        dwn=requests.get(url,proxies=socks5proxylist[2],timeout=10)
#        print(dwn)
#    except Exception as e:
#        print(f"Error: {e}")
#    time.sleep(0.5)
def hatalı2():
    import requests
    import os
    import time

    url = "https://guns.lol/sh3dowkkk"
    proxylist = []

    with open("dosya.txt", "r", encoding="utf-8") as file:
        for satir in file:
            proxylist.append(satir.strip())

    for proxy in proxylist:
        time.sleep(0.5)

        socks_proxy = f"socks5h://{proxy}"

        proxies = {
            "socks5": socks_proxy,
            "socks5": socks_proxy
        }
        print(proxies)
        print(socks_proxy)
        print(proxy)
        try:
            r = requests.get(url, proxies=proxies, timeout=10,verify=False)
            print("Status:", r.status_code)
            break  
        except Exception as e:
            print("Error:", proxy,e)
            print(e)
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://guns.lol/sh3dowkkk"

with open("dosya.txt", "r", encoding="utf-8") as f:
    proxylist = f.read().splitlines()

for proxy in proxylist:
    socks_proxy = f"socks5h://{proxy}"
    proxies = {
        "http": socks_proxy,
        "https": socks_proxy
    }

    print("socks proxy testing:", socks_proxy)

    try:
        r = requests.get(
            url,
            proxies=proxies,
            timeout=30,
            verify=False
        )
        print("✅ success | Status:", r.status_code)
        break
    except Exception as e:
        print("❌ error:", e)





