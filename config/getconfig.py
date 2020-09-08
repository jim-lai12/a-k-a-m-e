# -*- coding: utf-8 -*-
import logging
import sys
import os
import random
import cookielib

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='a+', format=FORMAT)

def checkFile(filepath):
    if os.path.isfile(filepath):
        logging.info(filepath+" is exist")
    else:
        logging.error(filepath +" file not found")
        sys.exit()

class Config:
    def __init__(self,configfile = "config.txt"):
        file = open(configfile, 'r')
        txt = file.readlines()
        file.close()
        if os.path.isfile("userAgent.txt"):
            file = open('userAgent.txt', 'r')
            self.userAgent = file.read()
            file.close()
        else:
            logging.error("userAgent.txt" + " file not found")
            userAgentl = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"]
            self.userAgent = userAgentl[random.randint(0,len(userAgentl)-1)]
        self.user = txt[0].split("#")[0].replace('user"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.gender = txt[1].split("#")[0].replace('gender"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.phone = txt[2].split("#")[0].replace('phone"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.time = txt[3].split("#")[0].replace('time"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.bookdate = txt[4].split("#")[0].replace('bookdate"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.booktime = txt[5].split("#")[0].replace('booktime"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.num = txt[6].split("#")[0].replace('num"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.cardNO = txt[7].split("#")[0].replace('cardNO"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.cardSecurityNO = txt[8].split("#")[0].replace('cardSecurityNO"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.cardExpireDate = txt[9].split("#")[0].replace('cardExpireDate"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.cardUser = txt[10].split("#")[0].replace('cardUser"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.email = txt[11].split("#")[0].replace('email"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.purposes = txt[12].split("#")[0].replace('purposes"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.note = txt[13].split("#")[0].replace('note"', "").replace('\n', "").replace('\r', "").replace('"', "")
        self.bookMode = txt[14].split("#")[0].replace('bookMode"', "").replace('\n', "").replace('\r', "").replace('"', "")
    def savecookie(self,s,cookiefile = "cookie.txt"):
        cj = cookielib.MozillaCookieJar()
        for s_cookie in s.cookies:
            cj.set_cookie(
                cookielib.Cookie(version=0, name=s_cookie.name, value=s_cookie.value, port='80', port_specified=False,
                                 domain=s_cookie.domain, domain_specified=True, domain_initial_dot=False,
                                 path="/", path_specified=True, secure=True,
                                 expires="1569592763",  # s_cookie['expiry']
                                 discard=False, comment=None, comment_url=None, rest=None,
                                 rfc2109=False))
        cj.save(cookiefile)




if __name__ == '__main__':
    config = Config()
    print config.user  # txt[0].split("#")[0].replace('user"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.gender  # txt[1].split("#")[0].replace('gender"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.phone  # txt[2].split("#")[0].replace('phone"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.time  # txt[3].split("#")[0].replace('time"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.bookdate  # txt[4].split("#")[0].replace('bookdate"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.num  # txt[5].split("#")[0].replace('num"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.cardNO  # txt[6].split("#")[0].replace('cardNO"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.cardSecurityNO  # txt[7].split("#")[0].replace('cardSecurityNO"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.cardExpireDate  # txt[8].split("#")[0].replace('cardExpireDate"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.cardUser  # txt[9].split("#")[0].replace('cardUser"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.email  # txt[10].split("#")[0].replace('email"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.purposes  # txt[11].split("#")[0].replace('purposes"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.note  # txt[12].split("#")[0].replace('note"', "").replace('\n', "").replace('\r', "").replace('"', "")
    print config.bookMode  # txt[13].split("#")[0].replace('bookMode"', "").replace('\n', "").replace('\r', "").replace('"', "")
