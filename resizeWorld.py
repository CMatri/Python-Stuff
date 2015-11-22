from PIL import Image
world = Image.open('world.png')
world = world.resize((720, 360), Image.BICUBIC)
world.save('worldResized.png')