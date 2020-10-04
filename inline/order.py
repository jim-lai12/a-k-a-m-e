# -*- coding: utf-8 -*-
import time
import logging
import sys



"""

h1 = {
     'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
     'Accept-Encoding': 'gzip, deflate, br',
     'Connection': 'keep-alive',
     'Accept': '*/*',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
     'Host': 'inline.app',
     'Referer': 'https://inline.app/booking/'+urlparse[0]+'/'+urlparse[1],
}
r = s.get("https://inline.app/booking/api/branch/"+urlparse[0]+"/"+urlparse[1],headers = h1)
bookrule = r.json()
r = s.get("https://inline.app/api/booking-capacities?companyId="+urlparse[0]+"&branchId="+urlparse[1],headers = h1)
timetable = r.json()


"""




class Order:
    def __init__(self,config,s,url):
        self.config = config
        self.session = s
        self.prepay = False
        self.message = False
        self.urlparse = url.split("?")[0].replace("https://inline.app/booking/", "").split("/")
        self.header = {
            'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'Host': 'inline.app',
            'Referer': 'https://inline.app/booking/' + self.urlparse[0] + '/' + self.urlparse[1],
        }
        self.header["User-Agent"] = self.config.userAgent
        self.header1 = {'origin': 'https://inline.app',
             'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
             'accept-encoding': 'gzip, deflate, br',
             'accept': '*/*',
             'dnt': '1',
             'referer': url,
             'content-type': 'application/json'
            }
        self.header1["User-Agent"] = self.config.userAgent
        self.header2 = {'origin': 'https://js.tappaysdk.com',
                        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept': '*/*',
                        'referer': 'https://js.tappaysdk.com/tpdirect/v5.1.0/api/html?%7B%22appKey%22%3A%22kI2T6Zsa7X1CNKcmaSk6G4VIgm8iLib22lySlQCh%22%2C%22appID%22%3A%2210869%22%2C%22serverType%22%3A%22production%22%2C%22hostname%22%3A%22inline.app%22%2C%22origin%22%3A%22https%3A%2F%2Finline.app%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22href%22%3A%22https%3A%2F%2Finline.app%2Fbooking%2F-LKPRufcYORCJA52hdpC%3Ainline-live-2a466%2F-LKPRuhT_j4KpaE3VDsl%2Fform%22%2C%22port%22%3A%22%22%2C%22protocol%22%3A%22https%3A%22%2C%22sdk_version%22%3A%22v5.1.0%22%7D',
                        'pragma': 'no-cache',
                        'cache-control': 'no-cache',
                        'x-api-key': 'kI2T6Zsa7X1CNKcmaSk6G4VIgm8iLib22lySlQCh',
                        'content-type': 'application/x-www-form-urlencoded'
                        }
        self.header2["User-Agent"] = self.config.userAgent
        if self.config.phone[0:2] == "09":
            self.config.phone =  "+886" + self.config.phone[1:]
        if self.config.gender == "M":
            self.config.gender = 0
        elif self.config.gender == "F":
            self.config.gender = 1
        self.orderData = {
            "language":"zh-tw",
            "company":self.urlparse[0],
            "branch":self.urlparse[1],
            "groupSize":self.config.num,
            "kids":0,
            "gender":self.config.gender,
            "purposes":[self.config.purposes],
            "email":"",
            "name":self.config.user,
            "phone":self.config.phone,
            "note":self.config.note,
            "date":self.config.bookdate,
            "time":self.config.booktime,
            "numberOfKidChairs":0,
            "numberOfKidSets":0,
            "skipPhoneValidation":"false",
            "referer":url,
}
    def setTimer(self):
        a = time.strftime("%H"":""%M"":""%S")
        if self.config.time == "xx:xx:xx":
            logging.info("start")
        else:
            while a != self.config.time:
                a = time.strftime("%H"":""%M"":""%S")
                time.sleep(0.01)
    def needprepay(self):
        getprime = 'jsonString={"cardnumber":"'+self.config.cardNO+'","cardduedate":"'+self.config.cardExpireDate+'","appid":"10869","appkey":"kI2T6Zsa7X1CNKcmaSk6G4VIgm8iLib22lySlQCh","appname":"inline.app","url":"https://inline.app","port":"","protocol":"https:","fraudid":"","cardccv":"'+self.config.cardSecurityNO+'"}'
        r = self.session.post("https://js.tappaysdk.com/tpdirect/production/getprime",headers = self.header2,data = getprime)
        try:
            prime = r.json()["card"]["prime"]
        except Exception as e:
            logging.error(e)
            logging.error(r.text)
            sys.exit()
        self.orderData["patronInvoice"] = {"type":"tw_duplicate_uniform_invoice"}
        self.orderData["payment"] = {
                        "type":"cardToken",
                        "prime":prime,
                        "cardholder":self.config.cardUser,
                        "phone":self.config.phone,
                        "email":self.config.email
                        }
        r = self.session.post("https://inline.app/api/reservations", headers=self.header1, json=self.orderData)
        print(r.text)
        if self.message :
            self.needprepay(r.text)
    def needotp(self,resp):
        print "還沒支持"
    def checkdetail(self):
        r = self.session.get("https://inline.app/booking/api/branch/" + self.urlparse[0] + "/" + self.urlparse[1], headers=self.header1)
        bookrule = r.json()
        r = self.session.get("https://inline.app/api/booking-capacities?companyId=" + self.urlparse[0] + "&branchId=" + self.urlparse[1],headers=self.header)
        timetable = r.json()
        # webBookingTableSelectorEnabled是否要選桌型不選也沒關係
        # requirePhoneVerification是否要驗證手機
        # print bookrule["paymentSettings"],bookrule["paymentSettings"]
        if "paymentSettings" in bookrule:
            if bookrule["paymentSettings"] != None:
                if "default" in bookrule["paymentSettings"]:
                    print "需要使用信用卡付款"
                self.prepay = True
        if "requirePhoneVerification" in bookrule:
            if bookrule["paymentSettings"] == "true":
                print "訂位時需要使用手機收驗證碼"
                self.message = True
    def sendorder(self):
        if self.prepay:
            print "pre"
            self.needprepay()
        else:
            r = self.session.post("https://inline.app/api/reservations", headers=self.header1, json=self.orderData)
            end = r.text
            print(end)
            full = u"訂位已滿，請修改人數、日期或時間"
            if end == full:
                print "error"
            while end == u"Service busy, please try again later: Service busy, please try again later":
                r = self.session.post("https://inline.app/api/reservations", headers=self.header1, json=self.orderData)
                end = r.text
            if self.message:
                self.needotp(r.text)




