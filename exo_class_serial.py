class Francais:
    nationalite = "Français"

    @staticmethod
    def displayNationality():
        print(f"Cette personne est de nationalité {Francais.nationalite}")

#Francais.displayNationality()

natFrancais = Francais()
natFrancais.displayNationality()

class Toulouse(Francais):
    nationalite = "Toulouse"

    @staticmethod
    def displayNationality():
        print(f"Cette personne est de nationalité {Francais.nationalite} et réside à {Toulouse.nationalite}")

#Toulouse.displayNationality()
natToulousain = Toulouse()
natToulousain.displayNationality()