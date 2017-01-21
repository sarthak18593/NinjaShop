from PIL import Image, ImageDraw
im = Image.open('GroceryStoreFinal.jpg')
draw = ImageDraw.Draw(im)
draw.line((50,200, 50,300), fill=150)
im.show()
