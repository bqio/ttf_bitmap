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
X_PADDING = 20
Y_PADDING = 20
MAX_HEIGHT = 100

FONT_NAME = "Neucha-Regular.ttf"
GRID_COLOR = "#FF00FF"
TEXT_COLOR = "#FFFFFF"
BORDER_COLOR = "#00FFFF"

RANGES = [
  (0x20, 0x7F),
  (0x0410, 0x0451)
]

wrapper = Image.new("RGBA", (15000, MAX_HEIGHT + 1))
drawer = ImageDraw.Draw(wrapper)
font = ImageFont.truetype(FONT_NAME, 70)

for _range in RANGES:
  start, end = _range
  for ch in range(start, end + 1):
    w = 0
    h = 0
    dim = get_size(chr(ch), font)
    if ch == 0x20:
      drawer.rectangle([X_OFFSET, 0, X_OFFSET + 20 + (X_PADDING * 2), MAX_HEIGHT], outline=GRID_COLOR)
      X_OFFSET += 20 + X_PADDING * 2
      continue
    if not dim:
      ch = 0x0023
      w, h = get_size(chr(ch), font)
    w, h = get_size(chr(ch), font)
    drawer.text((X_OFFSET + X_PADDING, 0 + Y_PADDING), chr(ch), font=font, stroke_width=4, stroke_fill=BORDER_COLOR, fill=TEXT_COLOR)
    drawer.rectangle([X_OFFSET, 0, X_OFFSET + w + (X_PADDING * 2), MAX_HEIGHT], outline=GRID_COLOR)
    X_OFFSET += w + X_PADDING * 2

wrapper.save("grid.png", "PNG")