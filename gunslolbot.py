import argparse
import sys
import os
import threading
import random
import time
from DrissionPage import ChromiumPage, ChromiumOptions
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("--time", type=int, required=True)
    parser.add_argument("--ua", default="user-agent.txt")
    parser.add_argument("--proxy",default=None,help="Proxy (ip:port or socks5://ip:port). Optional")
    parser.add_argument("--threading", action="store_true",default=0)

    args = parser.parse_args()

    url = args.url
    delayTİME = args.time
    ua_file = args.ua
    threading_flag = 1 if args.threading else 0
    proxy = args.proxy    
    print(url, delay, ua_file, threading_flag,proxy)
main()
if proxy==None:
    proxy=0
d="URL        :", url
c="TIME       :", delayTİME
b="THREADING  :", threading_flag
a="UA COUNT   :", len(ua_file)
f="PROXY :",proxy


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
     ==#@ *@%===-=====-=-====-----=====---=-====@ @*     
     ===@@  @@@@*=====---================---====@ @=     
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
URL = url
try:
    with open(ua_file, "r", encoding="utf-8") as f:
        useragent_list = f.read().splitlines()
    print(f"✅ {len(useragent_list)} founed agent")
except FileNotFoundError:
    print("❌ Hata: Error not founed file ")
    exit()
def notthear():
    for au_list in useragent_list:
        print(f"\n---🌐New AGENT---")
        
        co = ChromiumOptions()
        co.set_user_agent(au_list)
        co.set_argument("--disable-blink-features=AutomationControlled")
        co.set_argument("--incognito")
        co.set_argument("--no-first-run")
        args.proxy and co.set_proxy(args.proxy)
        try:
            page = ChromiumPage(co)
            print(f"🕵️ AGENT: {au_list[:50]}...")
            
            page.get(URL)
            
            page.wait.load_start()
            time.sleep(delayTİME) 
            target = page.ele('@@text():click to enter', timeout=delayTİME)
            if target:
                print("🎯 Element was Founed, click...")
                target.scroll.to_see()
                time.sleep(delayTİME)
                page.run_js('arguments[0].dispatchEvent(new MouseEvent("click", {bubbles: true}));', target)
                target.click() 
                print("✅ Success...")
                time.sleep(delayTİME)
            else:
                print("❌Button Not founed")
                page.get_screenshot(name="hata_goruntusu.png")

            page.quit()
            print("🚪 BROWSE was BEEN Shutdown.")

        except Exception as e:
            print(f"⚠️Error: {e}")
            try: page.quit()
            except: pass

        bekleme = delayTİME
        print(f"⏳ {bekleme} time to new User-Agent ...")
        time.sleep(bekleme)
if threading_flag==0:
    notthear()
elif threading_flag==1:
    print("STARTED WAS BEEN BACKGROUND PROGRAM!!!")
    t1 = threading.Thread(target=notthear)
else:
    print("ERROR")
print("\n✨ OKEY TO LİST!")


