from PIL import Image, ImageDraw, ImageFont

X_OFFSET = 18
X_PADDING = 15
Y_PADDING = 12
MAX_HEIGHT = 88
STROKE_WIDTH = 3
SPACE_WIDTH = 20
TOP = 0
MAX = 0

FONT_NAME = "Neucha-Regular.ttf"
FONT_SIZE = 80
GRID_COLOR = "#FF00FF"
TEXT_COLOR = "#FFFFFF"
BORDER_COLOR = "#00FFFF"

RANGES = [
  (0x21, 0x7E),
  (0x410, 0x44F),
  (0x451, 0x451),
  (0x20, 0x20)
]

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

wrapper = Image.new("RGBA", (11645, MAX_HEIGHT + 1))
drawer = ImageDraw.Draw(wrapper)
font = ImageFont.truetype(FONT_NAME, FONT_SIZE)

for _range in RANGES:
  start, end = _range
  for ch in range(start, end + 1):
    x = X_OFFSET
    y = TOP
    for patch in PATCH_FONT:
      if ch == patch[0]:
        x += patch[1]
        y = patch[2]
    drawer.text((x, y), chr(ch), font=font, stroke_width=STROKE_WIDTH, stroke_fill=BORDER_COLOR, fill=TEXT_COLOR)
    bbox = drawer.textbbox((x, y), chr(ch), font=font, stroke_width=STROKE_WIDTH)
    drawer.rectangle([bbox[0] - X_PADDING, 0, bbox[2] + X_PADDING, MAX_HEIGHT], outline=GRID_COLOR)
    if MAX < bbox[3]:
      MAX = bbox[3]
    X_OFFSET = bbox[2] + STROKE_WIDTH + X_PADDING * 2
print(X_OFFSET)
print(MAX)

#wrapper.show()
wrapper.save("grid.png", "PNG")