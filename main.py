from PIL import Image, ImageFont, ImageDraw 


title_font = ImageFont.truetype('nevis.ttf', 50)

W, H = (843,106)

for i in range(201):
    background = Image.open(r"background.png")
    quantity = str(i)
    image_editable = ImageDraw.Draw(background)
    w, h = image_editable.textsize(quantity, font=title_font)
    print(w,h)
    image_editable.text(((W-w)/2,13), quantity, fill="white", font=title_font)
    #image_editable.text((377,21), quantity, (255, 255, 255), font=title_font)
    filename = f'{i}.png'
    background.save(filename)