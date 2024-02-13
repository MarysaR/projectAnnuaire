#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 13/02/2024
----------------------------------------------------
3.2. ANNUAIRE_1 – FONCTIONS, MODULES, PACKAGES
----------------------------------------------------

@Marysa RÉGENT
"""

# Ajouter un contact
def addContact(annuaire):
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    cle = (nom + prenom).upper()
    annuaire[cle] = (nom, prenom)
    print("Nouveau contact ajouté avec succès!")

def displayContact(annuaire):
    if not annuaire:
        print("Il n'y a pas de contacts enregistrés !")
    else:
        for nom, prenom in annuaire.values():
            print(f"Nom : {nom}, Prenom : {prenom}")