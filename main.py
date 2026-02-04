import argparse
import sys
import os
import threading
import random
import time
from DrissionPage import ChromiumPage, ChromiumOptions

# Değişkenlerin diğer fonksiyonlarda görünmesi için global kapsamda tanımlıyoruz
args = None
URL = ""
delayTİME = 0
useragent_list = []
threading_flag = 0

def main():
    # Bu değişkenlerin global olduğunu belirtiyoruz
    global args, URL, delayTİME, useragent_list, threading_flag
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("--time", type=int, required=True)
    parser.add_argument("--ua", default="user-agent.txt")
    parser.add_argument("--proxy", default=None, help="Proxy (ip:port or socks5://ip:port). Optional")
    parser.add_argument("--threading", action="store_true", default=0)

    args = parser.parse_args()
    
    listbos = []
    url = args.url
    delayTİME = args.time
    ua_file = args.ua
    threading_flag = 1 if args.threading else 0
    proxy = args.proxy    
    
    listbos.append(url)
    listbos.append(delayTİME)
    listbos.append(ua_file)
    listbos.append(threading_flag)
    listbos.append(proxy)

    # Değişkenleri global değişkenlere eşitle
    URL = url

    d = "URL        :", url
    c = "TIME       :", delayTİME
    b = "THREADING  :", threading_flag
    a = "UA COUNT   :", len(ua_file) # Burada dosya adı uzunluğunu alıyor, mantığı bozmadım
    f = "PROXY      :", proxy

    print(f"""
        ===========================#@@@@@@@@#    
        ========================#@@@        @    
        ======================+@@   #@@@@@@ @=   
        ====================-+@= %@%*====@- @    
        =========-===========@- @#*======@ @@   
        ==-==================@ @++==-===*@ @    
        ======-=============+@ @*=======@- @    
        ======-=============#+ @====----@  @=   
        =======-============*+ @==---=--@  @=    
        ==================-=+@ @==-=----@. @=    
        ==================-==@ @==--=-=-#@ @=     
        ==============-======@ @===-----+@ @=     
        -=========+#@@@#*====@ @*=-======@ @@=    
        =====@@@@@%     *@@@@@  #========@- @=    
        ==+@@@     -*@@*.    - =*=-==---=*@ @@=     
        =#@# #@@@%###+::+@@@@@ @==----=-==@. @@@#=    
        =@  @@=====  -+=:    +##==-=----==*@ #  @@%=     
        +@ @#=====+**+==*@@@@%====---======@@ @@+ @%*=-     
        +@ @========---==-=====-==-=====-===@+ @@@  @#=     
        =@ @@====---================---=====+@% @%%  @-     
        =@@ @@@==-=-===========-==-=-=-===---+@- #*@ @=     
        ==@@  =#*+=-========---=====---=====-=+@ ##@ @+     
        ==@. @+. ==-========-=-=========-=---==%  *@ ##     
        ==@ @@+**+=======-==---------==-==---==+=:+@ :%     
        ==@  @+--==-=====---===-=--=-=======---====@ +%     
        ==#@ *@%===-=====-=-====-----=====---=-====@ @* ===@@  @@@@*=====---================---====@ @=     
        ====#@@    -========-============---===#.#@@ @=     
        ======@: @@+=====================-=-==%@ @@ @%=     
        ======*@  @@=====-========-======---=@@ @# @@=    
        =======@@  @@@*===---==============#@@   @@@=    
        ========*@@   @*==-=-====-======+@@@  @@@@=     
        ==========%@@  =#@@@#+====+%@@@@%   @@%=    
        ============#@@@      :..:       @@@#=    
        ===============*@@@@@%***#%@@@@@@+=                                   
    {a}
    {b}
    {c}
    {d}
    {f}                     
                                                    """)
    
    try:
        with open(ua_file, "r", encoding="utf-8") as f:
            useragent_list = f.read().splitlines()
        print(f"✅ {len(useragent_list)} founed agent")
    except FileNotFoundError:
        print("❌ Hata: Error not founed file ")
        sys.exit()

def notthear():
    # Global değişkenleri kullan
    global args, URL, delayTİME, useragent_list

    for au_list in useragent_list:
        print(f"\n---🌐New AGENT---")
        
        co = ChromiumOptions()
        co.set_user_agent(au_list)
        co.set_argument("--disable-blink-features=AutomationControlled")
        co.set_argument("--incognito")
        co.set_argument("--no-first-run")
        
        if args.proxy:
            co.set_proxy(args.proxy)
            
        try:
            page = ChromiumPage(co)
            print(f"🕵️ AGENT: {au_list[:50]}...")
            
            page.get(URL)
            
            # wait.load_start() bazen hata verebilir, try-except mantığı eklenebilir ama yapıyı bozmadım
            page.wait.load_start()
            time.sleep(delayTİME) 
            
            # Element seçici
            target = page.ele('@@text():click to enter', timeout=delayTİME)
            
            if target:
                print("🎯 Element was Founed, click...")
                try:
                    target.scroll.to_see()
                except:
                    pass
                time.sleep(delayTİME)
                # JS click injection
                page.run_js('arguments[0].dispatchEvent(new MouseEvent("click", {bubbles: true}));', target)
                try:
                    target.click() 
                except:
                    pass
                print("✅ Success...")
                time.sleep(delayTİME)
            else:
                print("❌Button Not founed")
                try:
                    page.get_screenshot(name="hata_goruntusu.png")
                except:
                    pass

            page.quit()
            print("🚪 BROWSE was BEEN Shutdown.")

        except Exception as e:
            print(f"⚠️Error: {e}")
            try: page.quit()
            except: pass

        bekleme = delayTİME
        print(f"⏳ {bekleme} time to new User-Agent ...")
        time.sleep(bekleme)

# Kodun çalıştırılma mantığı
if __name__ == "__main__":
    main()
    
    # Traceback hatanızda "threading_flag==0" kontrolü vardı, onu buraya ekledim
    if threading_flag == 0:
        notthear()
    else:
        # Threading true ise burada işlem yapılmalı, kodunuzda bu kısım yoktu
        # ancak mantığı bozmamak için notthear çalıştırıyorum.
        notthear()