def affiche(ls) :
    print(ls)
    [print(f"Élément : {el:3d} ; id : {id(el)}") for el in ls]

ls = []
for k in range(10) :
    ls.append(k**2-3*k)

affiche(ls)
del ls[4]
affiche(ls)
ls.insert(4, 12)
affiche(ls)
