from PIL import Image
import os
import traceback

from core.logger import log_input


def make_wallpaper(rotate=0, mini=False, layers=0):
    try:
        pattern_path = os.path.join(os.path.split(os.path.dirname(__file__))[0], "urlImage.png")
        wallpaper_path = os.path.join(os.path.split(os.path.dirname(__file__))[0], "wallpaper.png")

        pattern = Image.open(pattern_path)
        pattern = pattern.convert("RGBA")
        pattern = pattern.rotate(rotate, expand=True)
        start_pos = 0
        x, y = pattern.size
        x1 = int(layers + x * 0.2 + (x + x * 0.2) * 16)
        y1 = int(layers + y * 0.2 + (y + y * 0.2) * 9)
        wallpaper = Image.new("RGB", (x1, y1), color="black")
        repeats = 1
        if layers:
            repeats = 15
            start_pos -= -3
        for repeat in range(2, repeats + 2):
            for x_column in range(16):
                for y_line in range(9):
                    if mini:
                        temp_x = int(pattern.size[0] - pattern.size[0] * (0.0001 * x_column * 0.0001 * y_line))
                        temp_y = int(pattern.size[1] - pattern.size[1] * (0.0001 * x_column * 0.0001 * y_line))
                        pattern = pattern.resize((temp_x, temp_y))
                    wallpaper.paste(pattern, (int(start_pos * repeat + x * 0.2 + x_column * x + (x_column * x * 0.2)),
                                              int(start_pos * repeat + y * 0.2 + y_line * y + (y_line * y * 0.2))),
                                    pattern)
        wallpaper = wallpaper.resize((1920, 1080))
        wallpaper.save(wallpaper_path)
    except:
        return {"error": True, "message": log_input(traceback.format_exc(), "error")}
    else:
        return {"error": False, "message": log_input("Wallpaper already saved.", "INFO")}

