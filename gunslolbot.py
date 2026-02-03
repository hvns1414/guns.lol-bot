import random
import time
from DrissionPage import ChromiumPage, ChromiumOptions
URL = "https://guns.lol/sh3dowkkk"

ua_list = [

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",

    "Mozilla/5.0 (X11; Linux x86_64; Kali Linux) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; Kali) Gecko/20100101 Firefox/121.0",

    "Mozilla/5.0 (X11; Linux x86_64; Arch Linux) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; Arch) Gecko/20100101 Firefox/122.0",

    "Mozilla/5.0 (X11; Linux x86_64; BlackArch) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36",

    "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Debian; Linux x86_64) Gecko/20100101 Firefox/122.0",

    "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
]
#şimdi la burya proxy listesini okuyup ayarladın heee unutma
with open("dosya.txt", "r", encoding="utf-8") as f:
    proxy_list = f.read().splitlines()
with open("user-agent.txt", "r", encoding="utf-8") as f:
    ua_list  = f.read().splitlines()
#attack döngüsü
def attprox():
    for proxy in proxy_list:
        print(f"\n🧪 Testing proxy: socks5(h)://{proxy}")
        co = ChromiumOptions()
        # Proxy ayarı 
        co.set_proxy(f"socks5h://{proxy}")
        # User-Agent UNUTMAAAA yada yerine tor kullan
        ua = random.choice(ua_list)
        co.set_user_agent(ua)
        # yeni biri gibi olsun ki giriş sayısı artsın ua yı niye koyduk random-agent için
        co.set_argument("--incognito")
        co.set_argument("--disable-blink-features=AutomationControlled")
        co.set_argument("--no-first-run")
        co.set_argument("--disable-infobars")
        try:
            page = ChromiumPage(co)
            page.get(URL, timeout=5)
            print("✅ Successfull!")
            print("UA:", ua)
            print("Proxy:", proxy)
            time.sleep(5)  # Sayfa bot olduğumuzu anlamaması için otomatik
            page.quit()
        except Exception as e:
            print("❌ Error:", e)
            try:
                page.quit()
            except:
                pass
def wait_and_click(page, selector, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        try:
            ele = page.ele(selector)
            if ele:
                ele.click()
                return True
        except:
            pass
        time.sleep(0.5)
    return False
co = ChromiumOptions()
# Proxy ayarı 
 # User-Agent UNUTMAAAA yada yerine tor kullan
ua = random.choice(ua_list)
co.set_user_agent(ua)
# yeni biri gibi olsun ki giriş sayısı artsın ua yı niye koyduk random-agent için
co.set_argument("--incognito")
co.set_argument("--disable-blink-features=AutomationControlled")
co.set_argument("--no-first-run")
co.set_argument("--disable-infobars")
try:
    page = ChromiumPage(co)

    page.get(URL, timeout=10)
    print("✅ Successfull!")
    print("UA:", ua)

    ok = wait_and_click(page, 'text:contains(click to enter)', timeout=15)
    if ok:
        print("✅ click to enter was founded")
    else:
        print("❌ click to enter not found")

    time.sleep(5)
    page.quit()
except Exception as e:
        print("❌ Error:", e)
        try:
            page.quit()
        except:
            pass
