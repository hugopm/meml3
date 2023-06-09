import random
from tikz import *
pic = Picture(scale=3, line_cap='round')

# background grid
DIM = 10
NB_POINTS = 20
random.seed(42*42)
pic.draw(line([(0, 0), (DIM - DIM/NB_POINTS, 0)]), thick=True, line_width='0.25mm')
def up(x1, x2):
    pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=180), thick=True)
def down(x1, x2):
    pic.draw((x2, 0), arc(radius=(x2-x1)/2, start_angle=0, end_angle=-180), thick=True)

def gen_word(draw_f):
    signs = [+1]*(NB_POINTS//2) + [-1]*(NB_POINTS//2)
    random.shuffle(signs)
    cumul = [0]
    for x in signs:
        cumul.append(cumul[-1] + x)
    # Symétriser la marche vers le haut (Catalan)
    cumul = [abs(x) for x in cumul]
    pile = []
    word = ""
    for i in range(len(cumul)-1):
        sign = cumul[i+1] - cumul[i]
        if sign == 1:
            pile.append(i)
            word += '('
        else:
            draw_f(pile.pop()*DIM/NB_POINTS, i*DIM/NB_POINTS)
            word += ')'
    print(word)
gen_word(up)
gen_word(down)

#print(pic.code())
pic.write_image(f"sys_{NB_POINTS//2}.pdf")
