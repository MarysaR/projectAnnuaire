from print_color import print

print("Hello world", tag='success', tag_color='green', color='white')


nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

carrés = list(map(lambda x: x**2, nombres))

print("Liste des carrés :", carrés)

# Liste d'éléments
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrer les nombres pairs
nombres_pairs = filter(lambda x: x % 2 == 0, nombres)

# Utiliser map() avec une lambda pour calculer les carrés des nombres pairs
carrés_nombres_pairs = list(map(lambda x: x**2, nombres_pairs))

# Afficher la liste des carrés des nombres pairs
print("Liste des carrés des nombres pairs :", carrés_nombres_pairs)

# Liste d'éléments
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialiser une liste vide pour stocker les carrés des nombres pairs
carrés_nombres_pairs = []

# Utiliser une boucle for pour filtrer les nombres pairs et calculer les carrés
for nombre in elements:
    if nombre % 2 == 0:
        carrés_nombres_pairs.append(nombre**2)

# Afficher la liste des carrés des nombres pairs
print("Liste des carrés des nombres pairs :", carrés_nombres_pairs)