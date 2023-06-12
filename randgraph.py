edges = """0 1
0 2
0 3
2 3
3 4
0 5
5 6
5 7
6 8
7 8
7 9
4 10
10 1
10 11""".split('\n')
edges = [tuple(map(int, x.split())) for x in edges]
print(edges)

bad = [8, 9, 11]
def tnod(node):
    a = ""
    if node == 0:
        a = "[red,fill=red]"
    elif not (node in bad):
        a = "[red]"
    return str(node)+a
def tedg(edge):
    u, v = edge
    u, v = tnod(u), tnod(v)
    tactac = "--"
    if "red" in u and "red" in v:
        tactac += "[red]"
    return f"{u} {tactac} {v}"

edges = [tedg(x) for x in edges]

print("\\begin{tikzpicture}")
# for i, n in enumerate(liste, 1):
#     dist = "1.5" if n <= 10 else "1"
print("""\\graph [spring layout, nodes={circle,draw,as=.}]
{ %s }""" % (";".join(edges)))
    
# print("""\\only<%s>{\\graph []
# { %s }}""" % (len(liste)+1, g(4)))

print("\\end{tikzpicture}")
# print("\\caption{")
    
# for i, n in enumerate(liste, 1):
#     typ = "$C_{%s}$ lui-même"%n if n <= 7 else "une chaîne de taille 6"
#     print("\only<%s>{Le $3$-voisinage de $C_{%s}$ est %s}" % (i, n, typ))

# print("\only<%s>{La chaîne infinie $P_\infty$}" % (len(liste)+1))

# print("}\n\\end{figure}")
