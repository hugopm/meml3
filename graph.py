def f(n):
    res = ""
    for i in range(n):
        res += str(i)
        if i == 0:
            res += "[red,fill=red]"
        elif min(i, n-i) <= 3:
            res += "[red]"
        res += "--"
        if max(min(i, n-i), min(i+1, n-i-1)) <= 3:
            res += "[red]"
    res += "0"
    return res

def g(n):
    res = ""
    for i in range(2*n+1):
        res += str(i)
        opts = ["circle", "draw", f"as={i-n}"]
        if i == n:
            opts.append("fill=red")
        if abs(i-n) <= 3:
            opts.append("red")
        res += "[%s]" % ",".join(opts)
        if i < 2*n:
            res += "--"
            if max(abs(i-n), abs(i+1-n)) <= 3:
                res += "[red]"
    res = "a[as=] --[dotted,thick] " + res + " --[dotted,thick] b[as=]"
    return res

liste = [4, 7, 8, 14]

print("""\\begin{figure}
\\centering
\\begin{tikzpicture}""")
for i, n in enumerate(liste, 1):
    dist = "1.5" if n <= 10 else "1"
    print("""\\only<%s>{\\graph [simple necklace layout, node distance=%scm, nodes={circle,draw,as=.}]
{ %s }}""" % (i, dist, f(n)))
    
print("""\\only<%s>{\\graph []
{ %s }}""" % (len(liste)+1, g(4)))

print("\\end{tikzpicture}")
print("\\caption{")
    
for i, n in enumerate(liste, 1):
    typ = "$C_{%s}$ lui-même"%n if n <= 7 else "une chaîne de taille 6"
    print("\only<%s>{Le $3$-voisinage de $C_{%s}$ est %s}" % (i, n, typ))

print("\only<%s>{La chaîne infinie $P_\infty$}" % (len(liste)+1))

print("}\n\\end{figure}")
