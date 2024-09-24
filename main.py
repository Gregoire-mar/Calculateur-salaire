def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

def main():
    salaire_annuel = float(input("Saisissez votre salaire annuel : "))
    heures_travaillees = float(input("Saisissez le nombre d'heures travaillées par semaine : "))

    salaire_mensuel_resultat = salaire_mensuel(salaire_annuel)
    salaire_hebdomadaire_resultat = salaire_hebdomadaire(salaire_mensuel_resultat)
    salaire_horaire_resultat = salaire_horaire(salaire_hebdomadaire_resultat, heures_travaillees)

    print("Votre salaire mensuel est de", salaire_mensuel_resultat, "euros.")
    print("Votre salaire hebdomadaire est de", salaire_hebdomadaire_resultat, "euros.")
    print("Votre salaire horaire est de", salaire_horaire_resultat, "euros par heure.")

if __name__ == "__main__":
    main()
