from PIL import Image, ImageDraw, ImageFont

X_OFFSET = 18
Y_OFFSET = 0

X_PADDING = 15
Y_PADDING = 0

X_MIN = X_OFFSET
X_MAX = 11645

Y_MIN = 0
Y_MAX = 88

FONT_NAME = "Neucha-Regular.ttf"
FONT_SIZE = 80
FONT_STROKE_WIDTH = 3

GRID_STROKE_WIDTH = 1

GRID_COLOR = "#FF00FF"
TEXT_COLOR = "#FFFFFF"
BORDER_COLOR = "#00FFFF"

# Glyph ranges
RANGES = [
    (0x21, 0x7E),
    (0x410, 0x44F),
    (0x451, 0x451),
    (0x20, 0x20)
]

# Patch glyph offsets (glyph, x, y)
PATCH_FONT = [
    [0x22, 0, 0],
    [0x23, 0, -3],
    [0x24, 0, 6],
    [0x25, 0, 4],
    [0x28, 0, 2],
    [0x29, 0, 2],
    [0x2a, 0, 3],
    [0x2f, 0, 8],
    [0x40, 0, 3],
    [0x5b, 0, 6],
    [0x5c, 0, 6],
    [0x5d, 0, 6],
    [0x7b, 0, 6],
    [0x7c, 0, 6],
    [0x7d, 0, 6],
    [0x41b, 7, 0],
    [0x42a, 2, 0],
    [0x42f, 2, 0],
    [0x431, 0, 10],
    [0x43b, 7, 0],
    [0x44f, 5, 0],
    [0x419, 0, 10],
    [0x416, 2, 2],
    [0x6a, 7, 0],
    [0x62, 0, 4],
    [0x64, 0, 4],
    [0x59, 2, 0]
]

if __name__ == "__main__":
    wrapper = Image.new("RGBA", (X_MAX, Y_MAX + GRID_STROKE_WIDTH))
    drawer = ImageDraw.Draw(wrapper)
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)

    for _range in RANGES:
        start, end = _range
        for ch in range(start, end + 1):
            x = X_OFFSET
            y = Y_OFFSET
            for patch in PATCH_FONT:
                if ch == patch[0]:
                    x += patch[1]
                    y += patch[2]
            drawer.text((x, y), chr(ch), font=font, stroke_width=FONT_STROKE_WIDTH,
                        stroke_fill=BORDER_COLOR, fill=TEXT_COLOR)
            text_box = drawer.textbbox((x, y), chr(ch), font=font, stroke_width=FONT_STROKE_WIDTH)
            box_x0 = text_box[0] - X_PADDING
            box_y0 = Y_MIN - Y_PADDING
            box_x1 = text_box[2] + X_PADDING
            box_y1 = Y_MAX + Y_PADDING
            drawer.rectangle(((box_x0, box_y0), (box_x1, box_y1)), outline=GRID_COLOR, width=GRID_STROKE_WIDTH)
            X_OFFSET = text_box[2] + FONT_STROKE_WIDTH + X_PADDING * 2

    wrapper.save("grid.png", "PNG")
