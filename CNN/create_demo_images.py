from pathlib import Path

from PIL import Image, ImageDraw


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
IMAGE_SIZE = 128


def make_background(color):
    return Image.new("RGB", (IMAGE_SIZE, IMAGE_SIZE), color)


def draw_cat(path, bg_color, fur_color, eye_color, ear_offset):
    img = make_background(bg_color)
    draw = ImageDraw.Draw(img)

    # Head
    draw.ellipse((28, 36, 100, 108), fill=fur_color, outline=(60, 40, 35), width=3)

    # Pointed ears, a simple cat cue.
    draw.polygon(
        [(35, 48), (48 + ear_offset, 16), (62, 50)],
        fill=fur_color,
        outline=(60, 40, 35),
    )
    draw.polygon(
        [(66, 50), (82 - ear_offset, 16), (96, 48)],
        fill=fur_color,
        outline=(60, 40, 35),
    )

    # Face
    draw.ellipse((46, 62, 56, 72), fill=eye_color)
    draw.ellipse((72, 62, 82, 72), fill=eye_color)
    draw.polygon([(64, 77), (59, 84), (69, 84)], fill=(245, 130, 145))
    draw.arc((52, 78, 64, 94), 0, 120, fill=(45, 30, 25), width=2)
    draw.arc((64, 78, 76, 94), 60, 180, fill=(45, 30, 25), width=2)

    # Whiskers
    for y in (78, 84, 90):
        draw.line((16, y, 54, 82), fill=(45, 30, 25), width=2)
        draw.line((74, 82, 112, y), fill=(45, 30, 25), width=2)

    img.save(path)


def draw_dog(path, bg_color, fur_color, ear_color, tongue=False):
    img = make_background(bg_color)
    draw = ImageDraw.Draw(img)

    # Floppy ears, a simple dog cue.
    draw.ellipse((18, 42, 48, 98), fill=ear_color, outline=(60, 42, 28), width=3)
    draw.ellipse((80, 42, 110, 98), fill=ear_color, outline=(60, 42, 28), width=3)

    # Head and muzzle
    draw.ellipse((30, 30, 98, 104), fill=fur_color, outline=(60, 42, 28), width=3)
    draw.ellipse((44, 70, 84, 104), fill=(245, 230, 205), outline=(60, 42, 28), width=2)

    # Face
    draw.ellipse((47, 56, 57, 66), fill=(20, 20, 20))
    draw.ellipse((71, 56, 81, 66), fill=(20, 20, 20))
    draw.ellipse((59, 76, 69, 86), fill=(40, 28, 20))
    draw.arc((52, 80, 64, 96), 0, 120, fill=(40, 28, 20), width=2)
    draw.arc((64, 80, 76, 96), 60, 180, fill=(40, 28, 20), width=2)

    if tongue:
        draw.rounded_rectangle((59, 93, 69, 113), radius=5, fill=(238, 105, 125))

    img.save(path)


def main():
    cat_dir = DATA_DIR / "cat"
    dog_dir = DATA_DIR / "dog"
    cat_dir.mkdir(parents=True, exist_ok=True)
    dog_dir.mkdir(parents=True, exist_ok=True)

    cat_styles = [
        ((235, 247, 255), (220, 150, 95), (30, 120, 70), 0),
        ((245, 240, 255), (80, 80, 88), (55, 170, 80), 4),
        ((255, 246, 232), (245, 205, 80), (30, 95, 150), -4),
        ((235, 255, 244), (250, 250, 245), (65, 130, 65), 2),
        ((252, 238, 245), (165, 118, 85), (60, 120, 160), -2),
    ]

    dog_styles = [
        ((238, 248, 235), (190, 130, 75), (115, 75, 48), False),
        ((250, 240, 230), (245, 230, 205), (100, 70, 45), True),
        ((236, 242, 255), (120, 90, 70), (60, 45, 35), False),
        ((255, 248, 225), (215, 170, 95), (135, 90, 50), True),
        ((240, 250, 250), (235, 235, 230), (120, 120, 115), False),
    ]

    for i, style in enumerate(cat_styles, start=1):
        draw_cat(cat_dir / f"cat_{i}.png", *style)

    for i, style in enumerate(dog_styles, start=1):
        draw_dog(dog_dir / f"dog_{i}.png", *style)

    print(f"Da tao 10 anh mau trong: {DATA_DIR}")


if __name__ == "__main__":
    main()
