import requests
from datetime import datetime as dt

APP_ID = "30fd34e2"
APP_KEY = "c79942e1ca572069d9179a26d5ce8e0b"
SHEETY_ENDPOINT = "https://api.sheety.co/8a461f59119ecc0a5bfa0a662a700c7b/myWorkout/sheet1"

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
execise = input("Tell me which exercises you did: ")
tracker_parameter = {
    "query": execise,
    "gender": "Male",
    "weight_kg": "73",
    "height_cm": "176",
    "age": "19",
}

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response_tracker = requests.post(excercise_endpoint, json=tracker_parameter, headers=header)
result = response_tracker.json()
print(result)

today = dt.now()
date = today.date().strftime("%d/%m/%Y")
time = today.time().strftime("%H:%M:%S")
exercise = result["exercises"][0]["user_input"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs)
print(response_sheety.text)

# today_date = dt.now().strftime("%d/%m/%Y")
# now_time = dt.now().strftime("%X")
#
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
# sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
#
# print(sheet_response.text)




