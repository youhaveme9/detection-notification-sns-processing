import requests

Hearder = {'X-Api-Key': '/mlYOZmBL3SZgvnSFiJOZA==1rSMVYLqMGGCFFX2'}
api_url = 'https://api.api-ninjas.com/v1/imagetotext'
image_file_descriptor = open('runs/detect/exp38/crops/plate/image0.jpg', 'rb')
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files, headers=Hearder)
print(r.json())