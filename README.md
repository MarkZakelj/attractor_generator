# attractor_generator
Generate colorized representations of De Jong attractors.  
Knowledge of python recommended!
## Installation
Before using the program, you need two python libraries:
- pillow
- numpy
    
To install them, use:  
`pip install pillow` and `pip install numpy`  
  
## Basic usage
To generate attractors, open command line in the proper directory (linux or windows)  
and run 'make_matrix.exe' (just 'make_matrix' on linux) with 5 (or 7) arguments.  
  
example_1: `make_matrix.exe -2.3 1.5 -1.9 2.1 300000000`-windows  
example_2: `./make_matrix -2.3 1.5 -1.9 2.1 250000000 1200 1200`-linux   
  
Then run colorize.py: `python colorize.py`  
  
Your picture should appear inside 'attractor_pictures' directory.

## Arguments explained
Usage: `make_matrix.exe a b c d iters width(optional) height(optional)`
- a, b, c, d [float64] are parameters for the attractor equations:  
&nbsp;&nbsp; x<sub>n+1</sub> = sin(**a**\*y<sub>n</sub>) - cos(**b**\*x<sub>n</sub>)  
&nbsp;&nbsp; y<sub>n+1</sub> = sin(**c**\*x<sub>n</sub>) - cos(**d**\*y<sub>n</sub>)  
- iters [int64] is number of iterations  
- width and height [int32] are optional; by default they are set to 1100 each.  
  
You can also run `make_matrix.exe` without arguments for explanation of every argument.
## How to colorize
This is the creative part of the process. It's more of a experiment in the end.  
To change colors of the attractor, you should open the file `colorize.py` in your favourite text editor and change the code manualy.     Find the function `calc_color1`:
```
def calc_color1(x, y, value, width, height):
    w = x*1.0/width
    h = y*1.0/height
    i = 255
    j = 255
    k = 255
    #calculate r g b values
    r = int((2*i/pi)*atan(value/i))
    g = int((2*j/pi)*atan(value/j))
    b = int((2*k/pi)*atan(value/k))
    return (255-r, 255-g, 255-b)
 ```  
 To change the colors, you can change 'i' 'j' and 'k' values.  
 You can also multiply value for certain color with 'w' or 'h' and this color will change horizontally or vertically.  
 example_1: `r = int((2*i/pi)*atan(w*value/i))`  
 More examples and pictures will be added to wiki!
   
 Don't forget to save and run `colorize.py` again!
