import requests
from datetime import datetime

from dotenv import load_dotenv
import os

from fake_useragent import UserAgent

ua = UserAgent()

load_dotenv()

pincode = os.getenv("pincode")
proxy_username = os.getenv("proxy_username")
proxy_password = os.getenv("proxy_password")
ifttt_applet_name = os.getenv("ifttt_applet_name")

VACCINATION_SLOT_API_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
IFTTT_URL = f"https://maker.ifttt.com/trigger/{ifttt_applet_name}/with/key/"

date = datetime.now().strftime("%d-%m-%Y")

payload = {
    "pincode": pincode,
    "date": date,
}

headers = {"User-Agent": ua.random}


proxy_url = (
    f"https://{proxy_username}:{proxy_password}@in-mum.prod.surfshark.com"
)

proxy = {
    "http": proxy_url,
    "https": proxy_url,
}

response = requests.get(
    VACCINATION_SLOT_API_URL, params=payload, proxies=proxy, headers=headers
).json()

if len(response["centers"]) > 0:

    all_sessions = []

    for center in response["centers"]:
        for session in center["sessions"]:
            all_sessions.append(session)

    age_groups = set([session["min_age_limit"] for session in all_sessions])

    message = f"<b>Vaccination Slots are available for age-group {age_groups}, check COWIN API or website for details.</b>"
    print(response)
    print(
        requests.post(
            IFTTT_URL + os.getenv("ifttt_api_key"), data={"value1": message}
        ).content.decode("ascii")
    )
else:
    print("No updates yet!!")
