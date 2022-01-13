import requests
from datetime import datetime

mylat = 15.828780
mylng = 80.196060
parm = {
    "lat": mylat,
    "lng": mylng,
    "formatted": 0
}

rsp3 = requests.get(url="https://api.sunrise-sunset.org/json", params=parm)
rsp3.raise_for_status()
d3 = rsp3.json()
sunr = d3["results"]["sunrise"].split("T")[1].split(":")[0]
suns = d3["results"]["sunset"].split("T")[1].split(":")[0]
d31 = (sunr, suns)
print(d31)
nw = datetime.now()
print(nw.hour)