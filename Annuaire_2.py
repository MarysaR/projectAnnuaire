#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 13/02/2024
----------------------------------------------------
3.3. ANNUAIRE_2 – FICHIER, SERIALISATION
----------------------------------------------------

@Marysa RÉGENT
"""

from Annuaire_Pack import ContactLib_1
import shelve

annuaire = shelve.open("Annuaire.dat")
LARGEUR = 60

while True:
    print("=" * LARGEUR)
    print("Menu:".center(LARGEUR))
    print("=" * LARGEUR)
    print("1. Ajouter un nouveau contact")
    print("2. Afficher les contacts")
    print("3. Quitter l'application")
    print("=" * LARGEUR)

    choix = input("Choisissez une option parmi les choix 1, 2 ou 3) : ")

    if choix == '1':
        ContactLib_1.addContact(annuaire)
    elif choix == '2':
       ContactLib_1.displayContact(annuaire)
    elif choix == '3':
        ContactLib_1.modifyContact(annuaire)
    elif choix == '4':
        ContactLib_1.deletedContact(annuaire)
    elif choix == '5':
        annuaire.close()
        print("Application quittée ")
        break
    else:
        print("Option non valide. Veuillez choisir 1, 2, ou 3.")