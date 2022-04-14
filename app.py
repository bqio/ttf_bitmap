from PIL import Image, ImageDraw, ImageFont

def get_size(text_string, font):
    try:
        ascent, descent = font.getmetrics()

        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent

        return (text_width, text_height)
    except:
        return None


X_OFFSET = 0
X_PADDING = 15
Y_PADDING = 12
MAX_HEIGHT = 110
STROKE_WIDTH = 3
SPACE_WIDTH = 20
TOP = 0

FONT_NAME = "Roboto-Medium.ttf"
FONT_SIZE = 80
GRID_COLOR = "#FF00FF"
TEXT_COLOR = "#FFFFFF"
BORDER_COLOR = "#00FFFF"

RANGES = [
  (0x21, 0x7E),
  (0x0410, 0x044F),
  (0x0451, 0x0451)
]

PATCH_FONT = [
  [0x22, 0, -12],
  [0x24, 0, -5],
  [0x25, 0, -14]
]

wrapper = Image.new("RGB", (15000, MAX_HEIGHT + 1))
drawer = ImageDraw.Draw(wrapper)
font = ImageFont.truetype(FONT_NAME, FONT_SIZE)

for _range in RANGES:
  start, end = _range
  for ch in range(start, end + 1):
    y = TOP
    for patch in PATCH_FONT:
      if ch == patch[0]:
        y = patch[2]
    drawer.text((X_OFFSET, y), chr(ch), font=font, stroke_width=STROKE_WIDTH, stroke_fill=BORDER_COLOR, fill=TEXT_COLOR)
    bbox = drawer.textbbox((X_OFFSET, y), chr(ch), font=font, stroke_width=STROKE_WIDTH)
    print(bbox)
    drawer.rectangle([bbox[0], 0, bbox[2], MAX_HEIGHT], outline=GRID_COLOR)
    X_OFFSET = bbox[2] + STROKE_WIDTH

#wrapper.show()
wrapper.save("grid.png", "PNG")