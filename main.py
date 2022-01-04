from PIL import Image


for i in range(201):
    number = str(i).rjust(3, '0')
    background = Image.open(r"bg.png")
    
    c = number[0]
    d = number[1]
    u = number[-1]

    first_digit = Image.open(rf"numbers/{c}.png")
    second_digit = Image.open(rf"numbers/{d}.png")
    third_digit = Image.open(rf"numbers/{u}.png")

    # Pasting img2 image on top of img1 
    # starting at coordinates (0, 0)
    posx_c = 43
    posx_d = 57
    posx_u = 71

    if u == "1":
        posx_u -= 4
    if u == "4":
        posx_u -= 2
    
    if d == "1":
        posx_d -= 4
        posx_u -= 4
    if d == "4":
        posx_d -= 2
        posx_u -= 2

    posy = 8 

    background.paste(first_digit, (posx_c, posy), mask = first_digit)
    background.paste(second_digit, (posx_d, posy), mask = second_digit)
    background.paste(third_digit, (posx_u, posy), mask = third_digit)

    # Displaying the image
    background.save(f"results/{c}{d}{u}.png","PNG")