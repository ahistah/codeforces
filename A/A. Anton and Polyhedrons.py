n=int(input())
faces=0

for _ in range(n):
    polyhedron= str(input())
    if polyhedron == "Tetrahedron":
        faces += 4
    elif polyhedron == "Cube":
        faces += 6
    elif polyhedron == "Octahedron":
        faces += 8
    elif polyhedron == "Dodecahedron":
        faces += 12
    else:
        faces += 20

print(faces)