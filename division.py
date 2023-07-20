def division(nombre1, nombre2):
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        return resultat
    else:
        return "Erreur : Division par zéro impossible."


nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

resultat_final = division(nombre1, nombre2)
print("Le résultat de la division est :", resultat_final)
