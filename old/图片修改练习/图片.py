from PIL import Image

img_file = Image.open("./15.jpg")
for x in range(img_file.size[1]):
    for y in range(img_file.size[0]):
        gay = img_file.getpixel((y, x))
        # print(gay)
        if gay[0]==255 and gay[1]==255 and gay[2]==255:
            img_file.putpixel((y,x),(231,96,177,0))
img_file = img_file.convert('RGB')
img_file.save('3.png')
