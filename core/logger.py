from datetime import datetime
import os


def log_path():
    directory = os.path.join(os.path.split(os.path.dirname(__file__))[0], "logs")
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass
    date = datetime.strftime(datetime.now(), "%d-%m-%y")
    path = os.path.join(directory, f"{date}.log")
    return path


def log_input(text, state):
    path = log_path()
    with open(path, "a") as file:
        time = datetime.strftime(datetime.now(), "[%H:%M:%S]")
        file.write(f"{time} [{state.upper()}]: {text}\n")
    return text
