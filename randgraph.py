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
#print(edges)

voisinages = [[0], [0,1,2,3,5], [0,1,2,3,5,6,7,4,10], [0,1,2,3,5,6,7,4,10,8,9,11]]
def tnod(k, node):
    a = ""
    if node == 0:
        a = "[red,fill=red]"
    elif node in voisinages[k]:
        a = "[red]"
    return str(node)+a
def tedg(k, edge):
    u, v = edge
    u, v = tnod(k, u), tnod(k, v)
    tactac = "--"
    if "red" in u and "red" in v:
        tactac += "[red,thick]"
    return f"{u} {tactac} {v}"

print("\\begin{figure}\n\\centering")
print("\\begin{tikzpicture}")
for k in range(1, 4):
    sedg = [tedg(k, x) for x in edges]
    print("\\only<%s>{" % k,end="")
    # for i, n in enumerate(liste, 1):
    #     dist = "1.5" if n <= 10 else "1"
    print("""\\graph [spring layout, node distance=1.5cm, nodes={circle,draw,as=}]
    { %s }""" % (";".join(sedg)) + "}%")
print("\\end{tikzpicture}")
    

print("\\caption{",end="")
    
for k in range(1, 4):
    print("\only<%s>{$%s$-voisinage}" % (k, k) + "%")

# print("\only<%s>{La chaîne infinie $P_\infty$}" % (len(liste)+1))

print("}\\end{figure}")
