from AnnuaireModele.AnnuaireLib import *

def addedContact(annuaire):
    nom = input("Nom : ").strip()
    prenom = input("Prenom : ").strip()
    telephone = input("Téléphone : ")
    email = input("Email : ")
    contact = Personne(nom, prenom, telephone, email)
    annuaire.addedContact(contact)
    print("Ce nouveau contact à été ajouté avec succès !")

def displayedContact(annuaire):
   liste = annuaire.displayedContact()
   if len(list(liste.keys())) > 0 :
       print("\nListe des contacts :")
       print("-" * 60)
       print("|" + "|".join(["Nom".ljust(16), "Prénom".ljust(16), "Téléphone".rjust(12), "Email".rjust(11)]) + "|")
       print("-" * 60)
       for p in liste.values():
           print("|" + "|".join([p.nom.ljust(16), p.prenom.ljust(16), p.telephone.rjust(12), p.email.rjust(11)]) + "|")
       print("-" * 60)
   else:
       print("Il n'y a pas de contacts enregistrés ! ")


def modifiedContact(annuaire):
    nom = input("Entrez le nom du contact à modifier :")
    prenom = input("Entrez le prenom du contact à modifier :")
    contact = annuaire.getContact(nom, prenom)
    if contact is None :
        print("Il n'y a aucun contact à modifier")
    else:
        nom, prenom, telephone, email = contact.nom, contact.prenom, contact.telephone, contact.email
        print("Entrer le champ à modifier 1: nom, 2: prénom, 3: téléphone, 4: email")
        choix = input("Entrer le numéro du champ à modifier : ")
        maj = input("Entrer la nouvelle valeur : ")
        match choix:
            case "1":
                nom = maj
            case "2":
                prenom = maj
            case "3":
                telephone = maj
            case "4":
                email = maj
            case _:
                print("Choix invalide ! Veuillez réessayer.")
        nouveau = Personne(nom, prenom, telephone, email)
        resultat = annuaire.modifiedContact(nouveau)
        if resultat:
            print("Ce contact a bien été modifié")
        else:
            annuaire.deletedContact(nouveau)
            print("L'ancien contact a bien été remplacé")
def deleteContact(annuaire):
    lcle = input("Entrer la cle du contact à supprimer : ")
    lcle = lcle.upper()
    resultat = annuaire.deletedContact(lcle)
    if resultat:
        print(f"Vous avez supprimé {lcle} de l'annuaire ! ")
    else:
        print(f"Aucune correspondance pour ce contact {lcle}.")