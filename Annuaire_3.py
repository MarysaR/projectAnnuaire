#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 13/02/2024
----------------------------------------------------
3.3. ANNUAIRE_2 – FICHIER, SERIALISATION
----------------------------------------------------

@Marysa RÉGENT
"""
import shelve

from Annuaire_Pack.ContactLib_2 import *

annuaire = shelve.open("AnnuaireSV.dat")
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
        addContact(annuaire)
    elif choix == '2':
       displayContact(annuaire)
    elif choix == '3':
        modifyContact(annuaire)
    elif choix == '4':
        deletedContact(annuaire)
    elif choix == '5':
        print("Application quittée ")
        break
    else:
        print("Option non valide. Veuillez choisir 1, 2, ou 3.")