import requests

from util.dateutils import get_ddmmyy_date

BASE_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"


def fetch_vaccine_appointments():
    params = {
        "pincode": "411045",
        "date": get_ddmmyy_date()
    }
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "content-type": "application/json",
        }
        response = requests.get(BASE_URL, data=params, headers=headers)
        print('Response from API', response)
        data = response.json()
        sessions = data["sessions"]
        appointments = []
        for session in sessions:
            address = session["address"]
            district = session["district"]
            block = session["block"]
            pincode = session["pincode"]
            info = {
                "name": session["name"],
                "address": "{address} {district} {block} {pincode}".format(address=address, district=district, block=block, pincode=pincode),
                "from": session["from"],
                "to": session["to"],
                "min_age_limit": session["min_age_limit"],
                "date": session["date"],
                "vaccine": session["vaccine"]
            }
            appointments.append(info)
    except:
        print("Response error")
        return []
    return appointments
