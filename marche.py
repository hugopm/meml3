import random
from tikz import *


# background grid
DIM_X, DIM_Y = 10, 4
NB_POINTS = 20
random.seed(42*42)

def up(pic, x1, x2, **kwargs):
    pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=180), **kwargs)

word="()(((()))()(()))(())"
coords = [(0,0)]
couplage = []
pile = []
for i in range(len(word)):
    c = word[i]
    x, y = coords[-1]
    if c == '(':
        y = y+1
        pile.append(i)
    else:
        y = y-1
        couplage.append((pile.pop()*DIM_X/NB_POINTS, (i+1)*DIM_X/NB_POINTS))
    coords.append((x+DIM_X/NB_POINTS, y))
    pic = Picture(scale=3, line_cap='round')
    if c == ')':
        pic.draw((0, 0), grid((DIM_X, DIM_Y), xstep=DIM_X/NB_POINTS, ystep=1),
            help_lines=True, very_thin=True)
        pic.draw(line(coords), thick=True, line_width='0.25mm')
        print(i, coords, couplage)
        for x1, x2 in couplage[:-1]:
            up(pic, x1, x2, thin=True, color="gray", dashed=True)
        x1, x2 = couplage[-1]
        up(pic, x1, x2, thick=True, color="red")
        pic.write_image(f"marche_{i}.pdf")
