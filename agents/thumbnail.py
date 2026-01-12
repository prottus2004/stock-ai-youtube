from PIL import Image, ImageDraw, ImageFont

def make_thumbnail(text, out):
    img = Image.new("RGB", (1280, 720), (20,20,20))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()

    draw.text((50,300), text[:80], fill=(255,255,0), font=font)
    img.save(out)
    return out

