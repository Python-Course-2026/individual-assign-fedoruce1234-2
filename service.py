import re
import colorsys
from fastapi import HTTPException


def convert_color(color: str) -> dict:
    """Принимает цвет в любом формате и возвращает все три представления."""
    color = color.strip()

    if color.startswith("#"):
        r, g, b = hex_to_rgb(color)
    elif color.lower().startswith("rgb"):
        r, g, b = parse_rgb(color)
    elif color.lower().startswith("hsl"):
        r, g, b = hsl_to_rgb(color)
    else:
        raise HTTPException(status_code=422, detail="Неизвестный формат. Используйте HEX, RGB или HSL")

    return {
        "hex": rgb_to_hex(r, g, b),
        "rgb": f"rgb({r}, {g}, {b})",
        "hsl": rgb_to_hsl(r, g, b),
    }


def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise HTTPException(status_code=400, detail="HEX должен содержать 6 символов")
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректный HEX цвет")
    return r, g, b


def parse_rgb(rgb_str: str):
    nums = re.findall(r"\d+", rgb_str)
    if len(nums) != 3:
        raise HTTPException(status_code=400, detail="RGB должен содержать три значения")
    r, g, b = int(nums[0]), int(nums[1]), int(nums[2])
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise HTTPException(status_code=400, detail="Значения RGB должны быть от 0 до 255")
    return r, g, b


def hsl_to_rgb(hsl_str: str):
    nums = re.findall(r"[\d.]+", hsl_str)
    if len(nums) != 3:
        raise HTTPException(status_code=400, detail="HSL должен содержать три значения")
    h, s, l = float(nums[0]), float(nums[1]), float(nums[2])
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return round(r * 255), round(g * 255), round(b * 255)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def rgb_to_hsl(r: int, g: int, b: int) -> str:
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return f"hsl({round(h * 360)}, {round(s * 100)}%, {round(l * 100)}%)"