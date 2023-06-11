import random
from tikz import *
from uf import Uf
pic = Picture(scale=3, line_cap='round')

# background grid
DIM = 10
NB_POINTS = 20
random.seed(42*42)
pic.draw(line([(0, 0), (DIM - DIM/NB_POINTS, 0)]), thick=True, line_width='0.25mm')

#pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=-180), thin=True, color="gray", dashed=True)
def draw(x1, x2, angle=180, **kwargs):
    pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=angle), **kwargs)

def gen_word():
    signs = [+1]*(NB_POINTS//2) + [-1]*(NB_POINTS//2)
    random.shuffle(signs)
    cumul = [0]
    for x in signs:
        cumul.append(cumul[-1] + x)
    # Symétriser la marche vers le haut (Catalan)
    cumul = [abs(x) for x in cumul]
    pile = []
    edges = []
    word = ""
    for i in range(len(cumul)-1):
        sign = cumul[i+1] - cumul[i]
        if sign == 1:
            pile.append(i)
            word += '('
        else:
            edges.append((pile.pop(), i))
            word += ')'
    print(word)
    return edges
up = gen_word()
down = gen_word()
comp = Uf(NB_POINTS)
for edges in [up, down]:
    for x1, x2 in edges:
        comp.union(x1, x2)
_colors, avail = {}, ['red', 'blue', 'black!60!green']
def get_color(x):
    x = comp.find(x)
    if not (x in _colors):
        if avail:
            _colors[x] = avail.pop()
        else:
            _colors[x] = 'black'
    return _colors[x]

for edges, angle in [(up, 180), (down, -180)]:
    for x1, x2 in edges:
        draw(x1*DIM/NB_POINTS, x2*DIM/NB_POINTS, angle=angle, color=get_color(x1), thick=True)

#print(pic.code())
pic.write_image(f"colored_{NB_POINTS//2}.pdf")
