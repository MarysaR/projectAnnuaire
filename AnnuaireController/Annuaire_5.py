#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 15/02/2024
----------------------------------------------------
3.6.2. CREATION D’EXCEPTION DANS NOTRE GESTION D’ANNUAIRE
----------------------------------------------------

@Marysa RÉGENT
"""
from AnnuaireView.Annuaire_5clt import *

annuaire = Annuaire("Annuaire")
LARGEUR = 60

while True:
    print("=" * LARGEUR)
    print("Menu:".center(LARGEUR))
    print("=" * LARGEUR)
    print("1. Ajouter un nouveau contact")
    print("2. Afficher les contacts")
    print("3. Modifier un contact")
    print("4. Supprimer un contact")
    print("5. Quitter l'application")
    print("=" * LARGEUR)

    choix = input("Choisissez une option parmi les choix 1, 2, 3, 4 ou 5 (pour quitter l'application) : ")

    if choix == '1':
        addedContact(annuaire)
    elif choix == '2':
       displayedContact(annuaire)
    elif choix == '3':
        modifiedContact(annuaire)
    elif choix == '4':
        deletedContact(annuaire)
    elif choix == '5':
        annuaire.close()
        print("Merci d'avoir utilisé l'application, au revoir !")
        break
    else:
        print("Option non valide. Veuillez choisir 1, 2, ou 3.")