import random
from tikz import *
# background grid
DIM_X, DIM_Y = 10, 4
NB_POINTS = 20
random.seed(42*42)

def draw(pic, x1, x2, angle=180, **kwargs):
    pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=angle), **kwargs)

class Mot:
    def __init__(self, w):
        self.word = w
        self.couplage, self.pile = [], []
    def iter(self, i):
        c = self.word[i]
        if c == '(':
            self.pile.append(i)
            return y+1
        else:
            self.couplage.append(((self.pile.pop()+0.5)*DIM_X/NB_POINTS, (i+0.5)*DIM_X/NB_POINTS))
            return y-1

up = Mot("()(((()))()(()))(())")
down = Mot("((()))()()(())()()()")
coords = [(0,0)]
beamer = 1
print("\only<%s>{\includegraphics[width=\\textwidth]{marche/all.pdf}}" % (beamer))
for i in range(len(up.word)):
    x, y = coords[-1]
    y = up.iter(i)
    down.iter(i)
    coords.append((x+DIM_X/NB_POINTS, y))
    if up.word[i] == ')':
        pic = Picture(scale=3, line_cap='round')
        pic.draw((0, 0), grid((DIM_X, DIM_Y), xstep=DIM_X/NB_POINTS, ystep=1),
            help_lines=True, very_thin=True)
        pic.draw(line(coords), thick=True, line_width='0.25mm')
        #print(i, up.couplage)
        for x1, x2 in up.couplage[:-1]:
            draw(pic, x1, x2, thin=True, color="gray", dashed=True)
        x1, x2 = up.couplage[-1]
        draw(pic, x1, x2, thick=True, color="red")
        pic.write_image(f"marche/{i}.pdf")
        beamer += 1
        print("\only<%s>{\includegraphics[width=\\textwidth]{marche/%s.pdf}}" % (beamer, i))

# marche only
pic = Picture(scale=3, line_cap='round')
pic.draw((0, 0), grid((DIM_X, DIM_Y), xstep=DIM_X/NB_POINTS, ystep=1),
    help_lines=True, very_thin=True)
pic.draw(line(coords), thick=True, line_width='0.25mm')
pic.write_image("marche/all.pdf")

# couplage en prio
pic = Picture(scale=3, line_cap='round')
pic.draw((0, 0), grid((DIM_X, DIM_Y), xstep=DIM_X/NB_POINTS, ystep=1),
    help_lines=True, very_thin=True)
pic.draw(line(coords), very_thin=True, color="gray", dashed=True)
for x1, x2 in up.couplage:
    draw(pic, x1, x2, thick=True)
pic.write_image(f"marche/up.pdf")
beamer += 1
print("\only<%s>{\includegraphics[width=\\textwidth]{marche/up.pdf}}" % (beamer))
for x1, x2 in down.couplage:
    # -180 pour en dessous
    draw(pic, x1, x2, angle=-180, thick=True)
pic.write_image(f"marche/up_down.pdf")
beamer += 1
print("\only<%s>{\includegraphics[width=\\textwidth]{marche/up_down.pdf}}" % (beamer))
