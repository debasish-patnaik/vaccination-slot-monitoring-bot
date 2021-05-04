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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

response = requests.get(
    VACCINATION_SLOT_API_URL, params=payload, headers=headers
)
print(response)

# if len(response["centers"]) > 0:
#     message = "<b>Vaccination Slots are available, check COWIN API or website for details.</b>"
#     print(
#         requests.post(
#             IFTTT_URL + os.getenv("ifttt_api_key"), data={"value1": message}
#         ).content.decode("ascii")
#     )
