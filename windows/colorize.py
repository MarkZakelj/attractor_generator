
import numpy as np
from math import atan, pi, sqrt
from PIL import ImageDraw, Image
import os

border = 40

def calc_color1(x, y, value, width, height):
    w = x*1.0/width
    h = y*1.0/height
    i = 255
    j = 255
    k = 160
    #calculate r g b values
    r = int((2*i/pi)*atan(sqrt(value)*10*h*w/i))
    g = int((2*j/pi)*atan(value*10/j))
    b = int((2*k/pi)*atan(h*value*10/k))
    return (r, 255-g, 255-b)

def calc_color2(x, y, value, width, height):
    w = x/width
    h = y/height
    i = 255
    j = 255
    k = 200
    #calculate r g b values
    r = int((2*i/pi)*atan(sqrt(value)*10*h*w/i))
    g = int((2*j/pi)*atan(value*2/j))
    b = int((2*k/pi)*atan(h*value*10/k))
    return (255-r, 255-g, 255-b)


def make_picture(matrix, width, height):
    im = Image.new('RGB', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    for (x, y), value in np.ndenumerate(matrix):
        if matrix[x][y] > border:
            r, g, b = calc_color1(x, y, matrix[x][y], width, height)
            draw.point((x, y), fill=(r, g, b))
        else:
        	r, g, b = calc_color1(x, y, border, width, height)
        	draw.point((x, y), fill=(r, g, b))
    save_image(im)

def save_image(im):
    #save picture to directory "attractor_pictures"
    i = 0
    current_path = os.getcwd()
    if not os.path.exists("{}/attractor_pictures".format(current_path)):
        os.mkdir("attractor_pictures")
    os.chdir("{}/attractor_pictures".format(current_path))
    while os.path.exists("attractor_{0:0=3}.png".format(i)):
        i += 1
    im.save("attractor_{0:0=3}.png".format(i))
        


def main():
	try:
		matrix = np.genfromtxt('matrix.csv', delimiter=',', dtype=int)
		width = np.shape(matrix)[0]
		height = np.shape(matrix)[1]
		make_picture(matrix, width, height)
	except (OSError, IOError):
		print("\tRun 'make_matrix.exe' ('make_matrix' on linux) first to generate matrix of values, then run colorize.py")

if __name__ == '__main__':
    main()


