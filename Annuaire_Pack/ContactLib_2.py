#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
GESTION ANNUAIRE - 13/02/2024
----------------------------------------------------
3.4.1. DEFINITION D’UN OBJET PERSONNE
----------------------------------------------------

@Marysa RÉGENT
"""

class Personne:
    def __init__(self, nom, prenom, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Prenom : {self.prenom}, Nom : {self.nom}, \nTéléphone: {self.telephone}, \nEmail: {self.email}"

# Tester la classe dans l'interpréteur
if __name__ == "__main__":
    personne_test = Personne("Doe", "John", "123456789", "john.doe@example.com")
    print(personne_test)

# Ajouter un contact
def addContact(annuaire):
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    telephone = input("Téléphone : ")
    email = input("Email : ")
    cle_contact = nom.upper() + prenom.upper()

    annuaire[cle_contact] = Personne(nom, prenom, telephone, email)
    print("Nouveau contact ajouté avec succès !")

def displayContact(annuaire):
    if annuaire:
        print("\nListe des contacts :")
        print("-" * 60)
        print("|" + "|".join(["Nom".ljust(16), "Prénom".ljust(16), "Téléphone".rjust(12), "Email".rjust(11)]) + "|")
        print("-" * 60)
        for p in annuaire.values():
            print("|" + "|".join([p.nom.ljust(16), p.prenom.ljust(16), p.telephone.rjust(12), p.email.rjust(11)]) + "|")
        print("-" * 60)
    else:
        print("Il n'y a pas de contacts enregistrés ! ")

def verifCle(annuaire):
    cle = input("Entrer la clé du contact à supprimer : ")
    cle = cle.upper()
    contact = annuaire.get(cle, None)
    return cle, contact is not None

def modifyContact(annuaire):
    cle, trouve = verifCle(annuaire)
    if not trouve:
        print("Il n'y a aucun contact à modifier")
    else:
        nom, prenom, telephone, email = annuaire[cle]
        print("Entrer le champ à modifier 1: nom, 2: prénom, 3: téléphone, 4: email")
        choix = input("Entrer le numéro du champ à modifier : ")
        maj = input("Entrer la nouvelle valeur : ")

        match choix:
            case "1":
                nouvelle_cle = maj.upper() + prenom.upper()
                annuaire[nouvelle_cle] = Personne(maj, prenom, telephone, email)
                print(f"Ajout d'un nouveau nom pour le contact {prenom} {nom} ")
            case "2":
                nouvelle_cle = nom.upper() + maj.upper()
                annuaire[nouvelle_cle] = Personne(nom, maj, telephone, email)
                print("Ajout d'un nouveau contact ")
            case "3":
                annuaire[cle] = Personne(nom, prenom, maj, email)
                print(f"Modification du télephone pour {prenom} {nom}")
            case "4":
                annuaire[cle] = Personne(nom, prenom, telephone, maj)
                print(f"Modification de l'email pour {prenom} {nom}")
            case _:
                print("Choix invalide ! Veuillez réessayer.")

def deletedContact(annuaire):
    cle, trouve = verifCle(annuaire)
    if trouve:
        del annuaire[cle]
        print(f"Vous avez supprimé  {cle} de l'annuaire ! ")
    else:
        print(f"Aucune correspondance pour {cle}.")