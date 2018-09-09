
import sys
import base64
import requests
import json

# put desired file path here
file_path = 'https://i.ytimg.com/vi/SERPH0lY0xE/hqdefault.jpg'
dog_path = "http://www.smalldogbreeds.info/wp-content/uploads/2016/02/teddy-bear-pomeranian.gif"
# image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read())
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({'src': file_path,
                     'ocr': ["math", "text"]}),
    headers={"app_id": "", "app_key": "",
            "Content-type": "application/json"})
print(json.dumps(json.loads(r.text), indent=4, sort_keys=True))