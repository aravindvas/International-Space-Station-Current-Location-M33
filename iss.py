import requests
import smtplib

mymail = "mailme.anonymous.1@gmail.com"
mymail2 = "mailme.anonymous2@gmail.com"
pasd = "mailme1997"
# mylat = 15.828780
# mylng = 80.196060
mylat = 28.052570
mylng = -82.387840

# def overh():
rsp = requests.get(url="http://api.open-notify.org/iss-now.json")
rsp.raise_for_status()
la = float(rsp.json()["iss_position"]["latitude"])
lo = float(rsp.json()["iss_position"]["longitude"])
    # if mylat - 5 <= la <= mylng + 5 and mylng - 5 <= lo <= mylng + 5:
    #     return True

# while True:
#     if overh() :

with smtplib.SMTP("smtp.gmail.com:587") as conct:
    conct.ehlo()
    conct.starttls()
    conct.login(user=mymail, password=pasd)
    conct.sendmail(from_addr=mymail,
                    to_addrs=mymail2,
                    msg=f"Subject:Look Up\n\nThe ISS is above you in the sky. "
                        f"Exactly in Latittude {la} Longitude {lo}")


# rsp = requests.get(url="http://api.open-notify.org/iss-now.json")
# rsp.raise_for_status()
# la = float(rsp.json()["iss_position"]["latitude"])
# lo = float(rsp.json()["iss_position"]["longitude"])
#
# print(la, lo)