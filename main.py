from core.requestSystem import request_url
from core.fileHandler import make_wallpaper


def start():
    pattern = request_url("https://i.imgur.com/XY0StCU.jpg")
    print(pattern["message"])
    if pattern["error"]:
        return

    wallpaper = make_wallpaper(0, False, 15)
    print(wallpaper["message"])


if __name__ == '__main__':
    start()
