from PIL import Image, ImageDraw
import numpy as np

dim = (500, 500)

img = Image.new('RGBA', dim, (255, 255, 255, 0))
pixels = img.load()

def func(x, y, cR, cI):
    return x**2.0 - y**2.0 + cR, (x * y) * 2.0 + cI

def drawCircle(cR, cI):
    maxIter = 255
    xmin, xmax = -4.0, 4.0
    xstep = (xmax - xmin) / dim[0]
    ymin, ymax = -4.0, 4.0
    ystep = (ymax - ymin) / dim[1]
    raxis = []
    iaxis = []

    u = xmin
    while u < xmax:
        raxis += [u]
        u += xstep
    u = ymin
    while u < ymax:
        iaxis += [u]
        u += ystep

    for xa in range(dim[0]):
        for ya in range(dim[1]):
            x, y = raxis[xa], iaxis[ya]
            i = 0
            bounded = True
            while i < maxIter and bounded:
                x, y = func(x, y, cR, cI)
                i += 1
                if x < -10.0 or x > 10.0 or y < -10.0 or y > 10.0: bounded = False
            pixels[xa, ya] = (i * 20 % maxIter, 0, i * 40 % maxIter)

iters = 160.0
for i in range(int(iters) + 1):
    print i, (i / iters) * 8.0 - 4.0
    drawCircle((i / iters) * 8.0 - 4.0, 0.4)
    img.save('julias/julia' + ('0' if len(str(i + 1)) == 1 else '') + str(i + 1) + '.png', 'PNG')
