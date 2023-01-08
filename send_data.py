import requests


BASE_URL = "https://1aksik8wwi.execute-api.ap-south-1.amazonaws.com/dev"
Header = {
	"x-api-key" : "aZ8qDvmtFe3J03G09TYP78w8ANKs6HWGjQ5gGaag"
}

def send_update(car_no):
    """
    function for sending tracked car detail to local police station
    """

    details = {
        "title": f"Alert! {car_no} is spotted",
        "description": f"Car with license number: {car_no} is spotted at Ruby More Kolkata",
        "topicName" : "Belghoria Police Station",
        "carNumber" : car_no
    }

    respons = requests.post(url=f'{BASE_URL}/send-notification', headers=Header, json=details)
    print(respons)


def send_update_to_app(car_no):
    """
    function for sending tracked car detail app which is tracking it manually
    """

    details = {
        "title": "Car found",
        "description": "Car is found at this location",
        "topicName" : car_no,
        "carNumber" : car_no
    }

    respons = requests.post(url=f'{BASE_URL}/send-notification', headers=Header, json=details)
    print(respons)

def update_tracking_details(car_no):

    details = {
        "number" : car_no,
        "policeStation" : "Belghoria Police Station",
        "location": "Ruby General Hospital"
    }
    respons = requests.post(url=f'{BASE_URL}/lost-cars/update-tracking-details', headers=Header, json=details)
    print(respons)