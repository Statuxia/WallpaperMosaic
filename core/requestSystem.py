import traceback
from urllib.request import urlopen
import os

from core.logger import log_input


def request_url(url=None):
    try:
        img_data = urlopen(url)
    except Exception:
        return {"error": True, "message": log_input(traceback.format_exc(), "error")}

    directory = os.path.join(os.path.split(os.path.dirname(__file__))[0], "urlImage.png")
    with open(directory, 'wb') as handler:
        handler.write(img_data.read())
    return {"error": False, "message": log_input("Image already saved.", "INFO")}


def request_path(path=None):
    try:
        with open(path, 'rb') as handler:
            content = handler.read()
    except:
        return {"error": True, "message": log_input(traceback.format_exc(), "error")}

    directory = os.path.join(os.path.split(os.path.dirname(__file__))[0], "urlImage.png")
    with open(directory, 'wb') as handler:
        handler.write(content)
    return {"error": False, "message": log_input("Image already saved.", "INFO")}


def request_delete():
    directory = os.path.join(os.path.split(os.path.dirname(__file__))[0], "urlImage.png")
    os.remove(directory)
