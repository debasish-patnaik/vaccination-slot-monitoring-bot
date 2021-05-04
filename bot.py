import requests
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

VACCINATION_SLOT_API_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
IFTTT_URL = "https://maker.ifttt.com/trigger/crypto_alert/with/key/"

date = datetime.now().strftime("%d-%m-%Y")
pincode = "751030"

payload = {
    "pincode": pincode,
    "date": date,
}

proxy_username = os.getenv("proxy_username")
proxy_password = os.getenv("proxy_password")

proxy_url = (
    f"https://{proxy_username}:{proxy_password}@in-mum.prod.surfshark.com"
)

proxy = {
    "http": proxy_url,
    "https": proxy_url,
}

response = requests.get(
    VACCINATION_SLOT_API_URL, params=payload, proxies=proxy
).json()

if len(response["centers"]) > 0:
    message = "<b>Vaccination Slots are available, check COWIN API or website for details.</b>"
    print(response.json())
    print(
        requests.post(
            IFTTT_URL + os.getenv("ifttt_api_key"), data={"value1": message}
        ).content.decode("ascii")
    )
