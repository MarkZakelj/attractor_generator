import numpy as np
from math import atan, pi
from PIL import ImageDraw, Image
import os

def calc_color1(x, y, value, width, height):
    a = x/width
    b = y/height
    i = 190
    j = 160
    k = 110
    #calculate r g b values
    r = int((2*i/pi)*atan(a*b*value*8/i))
    g = int((2*j/pi)*atan(b*value/j))
    b = int((2*k/pi)*atan(value*10/k))
    return (255-r, 255-g, 255-b)

def make_picture(matrix, width, height):
    im = Image.new('RGB', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    for (x, y), value in np.ndenumerate(matrix):
        if matrix[x][y] > 10:
            r, g, b = calc_color1(x, y, matrix[x][y], width, height)
            draw.point((x, y), fill=(r, g, b))
        else:
        	r, g, b = calc_color1(x, y, 9, width, height)
        	draw.point((x, y), fill=(r, g, b))
    save_image(im)

def save_image(im):
    #save picture to directory "attractor_pictures"
    i = 0
    current_path = os.getcwd()
    os.chdir("{}/attractor_pictures".format(current_path))
    while os.path.exists("attractor_{0:0=3}.png".format(i)):
        i += 1
    im.save("attractor_{0:0=3}.png".format(i))
        


def main():
    matrix = np.genfromtxt('matrix.csv', delimiter=',', dtype=int)
    width = np.shape(matrix)[0]
    height = np.shape(matrix)[1]
    make_picture(matrix, width, height)

if __name__ == '__main__':
    main()


