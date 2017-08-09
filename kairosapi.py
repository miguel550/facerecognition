import requests
import base64
from io import BytesIO
try:
    from constants import *
except ImportError as e:
    raise Exception("Necesitas crear el archivo constants.py con las constantes APP_KEY y APP_ID")


class KairosApi(object):
    def __init__(self, gallery_name="Gente"):
        self.header = {
            'app_id': APP_ID,
            'app_key': APP_KEY
        }
        self.values = {
            "gallery_name": gallery_name
        }

    def enroll(self, subject_id, image):
        path = '/enroll'
        values = self.values.copy()
        values.update({"subject_id": subject_id})
        return self._send(path, values, image)

    def recognize(self, image):
        path = '/recognize'
        values = self.values.copy()
        values.update({"multiple_faces": "true"})
        return self._send(path, values, image)

    def _send(self, path, values, image):
        url = "https://api.kairos.com" + path
        img = base64.decodebytes(bytes(image, 'utf-8'))
        files = {"image": BytesIO(img)}
        r = requests.post(url, data=values, headers=self.header, files=files)
        return r.json()
