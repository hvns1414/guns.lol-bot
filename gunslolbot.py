import random
import time
from DrissionPage import ChromiumPage, ChromiumOptions

URL = "https://guns.lol/sh3dowkkk"
try:
    with open("user-agent.txt", "r", encoding="utf-8") as f:
        useragent_list = f.read().splitlines()
    print(f"✅ {len(useragent_list)} founed agent")
except FileNotFoundError:
    print("❌ Hata: Error not founed file ")
    exit()

for au_list in useragent_list:
    print(f"\n--- 🌐 New AGENT ATTACK ---")
    
    co = ChromiumOptions()
    co.set_user_agent(au_list)
    co.set_argument("--disable-blink-features=AutomationControlled")
    co.set_argument("--incognito")
    co.set_argument("--no-first-run")

    try:
        page = ChromiumPage(co)
        print(f"🕵️ AGENT: {au_list[:50]}...")
        
        page.get(URL)
        
        page.wait.load_start()
        time.sleep(1) 
        target = page.ele('@@text():click to enter', timeout=10)
        if target:
            print("🎯 Element was Founed, click...")
            target.scroll.to_see()
            time.sleep(1)
            page.run_js('arguments[0].dispatchEvent(new MouseEvent("click", {bubbles: true}));', target)
            target.click() 
            print("✅ Success...")
            time.sleep(1)
        else:
            print("❌Button Not founed")
            page.get_screenshot(name="hata_goruntusu.png")

        page.quit()
        print("🚪 BROWSE was BEEN Shutdown.")

    except Exception as e:
        print(f"⚠️Error: {e}")
        try: page.quit()
        except: pass

    bekleme = random.randint(0, 3)
    print(f"⏳ {bekleme} time to new User-Agent ...")
    time.sleep(bekleme)

print("\n✨ OKEY TO LİST!")
