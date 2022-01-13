import requests
from datetime import datetime
import smtplib
import time

mymail = "mailme.anonymous.1@gmail.com"
mymail2 = "aravindvasvav@gmail.com"
pasd = "mailme1997"
mylat = 15.828780
mylng = 80.196060
la = 0
lo = 0


def overh():
    global la, lo
    rsp = requests.get(url="http://api.open-notify.org/iss-now.json")
    rsp.raise_for_status()
    la = float(rsp.json()["iss_position"]["latitude"])
    lo = float(rsp.json()["iss_position"]["longitude"])
    # return True
    if (mylat - 5 <= la <= mylng + 5) and (mylng - 5 <= lo <= mylng + 5):
        return True


def nyt():
    # parm = {
    #     "lat": mylat,
    #     "lng": mylng,
    #     "formatted": 0
    # }

    # rsp3 = requests.get(url="https://api.sunrise-sunset.org/json", params=parm)
    # rsp3.raise_for_status()
    # d3 = rsp3.json()
    # sunr = int(d3["results"]["sunrise"].split("T")[1].split(":")[0])
    # suns = int(d3["results"]["sunset"].split("T")[1].split(":")[0])
    # return True
    nw = datetime.now().hour
    if 18 <= nw <= 23:
        return True


while True:
  time.sleep(10)
  if overh() and nyt():
      with smtplib.SMTP("smtp.gmail.com:587") as conct:
          conct.ehlo()
          conct.starttls()
          conct.login(user=mymail, password=pasd)
          conct.sendmail(from_addr=mymail,
                         to_addrs=mymail2,
                         msg=f"Subject:Look Up\n\nThe ISS is above you in the sky. "
                             f"Exactly in Latittude {la} Longitude {lo}")

