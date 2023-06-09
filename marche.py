import random
from tikz import *
pic = Picture(scale=3, line_cap='round')

# background grid
DIM_X, DIM_Y = 10, 4
NB_POINTS = 20
random.seed(42*42)
pic.draw((0, 0), grid((DIM_X, DIM_Y), xstep=DIM_X/NB_POINTS, ystep=1),
    help_lines=True, very_thin=True)

word="()(((()))()(()))(())"
coords = [(0,0)]
for c in word:
    x, y = coords[-1]
    coords.append((x+DIM_X/NB_POINTS, y+1 if c == '(' else y-1))
print(coords)
pic.draw(line(coords), thick=True, line_width='0.25mm')
pic.write_image(f"marche.pdf")
