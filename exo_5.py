from print_color import print
print("Hello world", tag='success', tag_color='green', color='white')

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

carrés = list(map(lambda x: x**2, nombres))
print("Liste des carrés :", carrés)

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nombres_pairs = filter(lambda x: x % 2 == 0, nombres)

carrés_nombres_pairs = list(map(lambda x: x**2, nombres_pairs))
print("Liste des carrés des nombres pairs :", carrés_nombres_pairs)

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
carrés_nombres_pairs = []

for nombre in elements:
    if nombre % 2 == 0:
        carrés_nombres_pairs.append(nombre**2)
print("Liste des carrés des nombres pairs :", carrés_nombres_pairs)