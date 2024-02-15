#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 15/02/2024
----------------------------------------------------
3.5. ANNUAIRE_4 – CONCEPTION OBJET, QUALITE DE CODE
----------------------------------------------------

@Marysa RÉGENT
"""
import shelve

#Gestion des erreurs @classe AnnuaireException
class AnnuaireException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# @class Personne
class Personne:
    def __init__(self, nom="x", prenom="x", telephone="", email=""):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
    def __str__(self):
        return f"Prenom : {self.prenom}, Nom : {self.nom}, \nTéléphone: {self.telephone}, \nEmail: {self.email}"

# @class Annuaire
class Annuaire:
    def __init__(self, nom="Répertoire"):
        self.nom = nom
        self.save_annuaire = shelve.open(self.nom)

    # @def validecle
    def validecle(self, *args):
        if len(args) == 1 and args[0] == "":
            raise AnnuaireException("Le nom ne peut pas être vide.")
        elif len(args) == 2 and (args[0] == "" or args[1] == ""):
            raise AnnuaireException("Le nom et le prénom ne peuvent pas être vides.")

    def __str__(self):
        return f"Annuaire : {self.nom}"

    # Créer un contact @class Personne
    def addedContact(self, pers):
        try:
            self.validecle(pers.nom, pers.prenom)
            cle_contact = pers.nom.upper() + pers.prenom.upper()
            self.save_annuaire[cle_contact] = pers
        except AnnuaireException as e:
            print(f"Erreur lors de l'ajout du contact: {e.message}")

    # Liste des contacts
    def displayedContact(self):
        if self.save_annuaire:
            liste_contacts = dict()
            for cle, personne in self.save_annuaire.items():
                liste_contacts[cle] = personne
            return liste_contacts

    def verifCle(self, cle):
        contact = self.save_annuaire.get(cle, None)
        return cle, contact is not None

    def modifiedContact(self, contact):
        try:
            self.validecle(contact.nom, contact.prenom)
            cle, trouve = self.verifCle(contact.nom.upper() + contact.prenom.upper())
            if not trouve:
                return False
            else:
                self.save_annuaire[cle] = contact
                return True
        except AnnuaireException as e:
            print(f"Erreur lors de la modification du contact: {e.message}")
            return False

    def close(self):
        self.save_annuaire.close()

    def deletedContact(self, Lcle):
        cle, trouve = self.verifCle(Lcle)
        if trouve:
            del self.save_annuaire[cle]
            return True
        else:
            return False

    def getContact(self, nom, prenom):
        cle = nom.upper() + prenom.upper()
        return self.save_annuaire.get(cle, None)