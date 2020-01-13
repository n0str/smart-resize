from PIL import Image


def fix_size(fn, desired_w=256, desired_h=256, fill_color=(0, 0, 0, 255)):
    im = Image.open(fn)
    x, y = im.size

    w = max(desired_w, x)
    h = int(w * desired_h / desired_w)
    if h < y:
        h = y
        w = int(h * desired_w / desired_h)

    new_im = Image.new('RGBA', (w, h), fill_color)
    new_im.paste(im, ((w - x) // 2, (h - y) // 2))
    return new_im.resize((desired_w, desired_h))


img = fix_size("5.jpeg", 180, 200, (255, 255, 255, 255))
img.save("new.png")
