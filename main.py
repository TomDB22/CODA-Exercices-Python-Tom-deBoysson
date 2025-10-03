def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom=input("Quelle est votre prénom ?")
    print("Votre prénom est ", prenom)

def exercice3():
    print("1er ligne \n 2eme ligne \n 3eme ligne")

def exercice4():
    age=int(input("De quelle année êtes vous ?"))
    print("Vous avez", 2025-age, "ans")

def exercice5():
    addition1=int(input("Saisir 1er nombre : "))
    addition2=int(input("Saisir 2eme nombre : "))
    print("L'addition des 2 nombres est", addition1+addition2)

def exercice6():
    soustraction1=int(input("Saisir 1er nombre : "))
    soustraction2=int(input("Saisir 2eme nombre : "))
    print("La soustraction des 2 nombres est", soustraction1-soustraction2)

def exercice7():
    multi1=int(input("Saisir 1er nombre : "))
    multi2=int(input("Saisir 2eme nombre : "))
    print("La multiplication des 2 nombres est", multi1*multi2)

def exercice8():
    divi1=int(input("Saisir 1er nombre : "))
    divi2=int(input("Saisir 2eme nombre : "))
    if divi2==0:
        print("Error")
        return
    print("La division des 2 nombres est", int(divi1/divi2))

def exercice9():
    carre=int(input("Saisir un nombre : "))
    print("Ce nombre au carré est : ", carre*carre)

def exercice10():
    double=int(input("Saisir un nombre : "))
    print("Le double de ce nombre est de : ", double+double )

def exercice11():
    moitié=int(input("Saisir un nombre : "))
    print("La moitié de ce nombre est de : ", moitié/2 )

def exercice12():
    for i in range (1,6):
        print ("Je suis élève de CODA")

def exercice13():
    for i in range (1,6):
        print (i)

def exercice14():
    for i in range (1,6):
        print ("2 *", i, "= ",i*2)

def exercice15():
    peri=int(input("Saisir longeur du coté : "))
    print("Le périmètre de ton carré est : ", peri*4)

def exercice16():
    aire=int(input("Saisir longeur du coté : "))
    print("L'aire de ton carré est : ", aire*4)

def exercice17():
    montant=int(input("Montant en euro : "))
    print("Le montant en dollars est de : ", montant*1.1)

def exercice18():
    conversion=int(input("Nombre de minutes ? : "))
    print("Cela fait", conversion*60, "secondes. ")

def exercice19():
    ttc=int(input("Montant HT ? : "))
    print("Le montant TTC est de : ", ttc*1.2, "€")

def exercice20():
    nom=str(input("Votre prénom ? : "))
    age=int(input("Votre age ? : "))
    print("Vous êtes",nom, "et vous avez", age, "ans.")

def exercice21():
    pon=int(input("Saisir un nombre : "))
    if pon<0 :
        print("Votre nombre est négatif ")
    elif pon>0 :
        print("Votre nombre est positif ")
    else :
        print("Votre nombre est nul ")

def exercice22():
    mom=int(input("Saisir votre âge : "))
    if mom<18 :
        print("Vous êtes mineur")
    else :
        print("Vous êtes majeur ")

def exercice23():
    valid=int(input("Saisir votre note : "))
    if 0<=valid<10 :
        print("Non validé ")
    elif 10<=valid<=20 :
        print("Validé ")
    else :
        print("Saisie invalide ")

def exercice24():
    grand=0
    nombre1=int(input("Saisir le  nombre 1 : "))
    nombre2=int(input("Saisir le  nombre 2 : "))
    if nombre1>nombre2:
        grand=nombre1
        print("Le nombre le plus grand est", grand)
    elif nombre2>nombre1:
        grand=nombre2
        print("Le nombre le plus grand est", grand)
    else :
        print("Les 2 nombres sont égaux")
    
def exercice25(): 
    nombre1=int(input("Saisir le  nombre 1 : "))
    nombre2=int(input("Saisir le  nombre 2 : "))
    if nombre1<nombre2:   
        print("CROISSANT")
    elif nombre2<nombre1:
        print("PAS CROISSANT")
    else :
        print("EGAUX")

def exercice26():
    div5=int(input("Saisir un nombre : "))
    if div5%5==0:
        print("Ce nombre est divisible par 5 ")
    else: 
        print("Ce nombre n'est pas divisive par 5 ")
    
def exercice27():
    cage=int(input("Saisir un âge : "))
    if 0<=cage<12 :
        print("Enfant ")
    elif 12<=cage<=17 :
        print("Adolesant ")
    elif 17<cage :
        print("Adulte ")
    else :
        print("Saisie invalide ")

def exercice29():
    temp=int(input("Saisir une température : "))
    if 0>temp :
        print("Glace ")
    elif 0<=temp<=100 :
        print("Eau liquide ")
    elif 100<temp :
        print("Gaz ")
    else :
        print("Saisie invalide ")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix=="2":
        exercice2()
    elif choix=="3":
        exercice3()
    elif choix=="4":
        exercice4()
    elif choix=="5":
        exercice5()
    elif choix=="6":
        exercice6()
    elif choix=="7":
        exercice7()
    elif choix=="8":
        exercice8()
    elif choix=="9":
        exercice9()
    elif choix=="10":
        exercice10()
    elif choix=="11":
        exercice11()
    elif choix=="12":
        exercice12()
    elif choix=="13":
        exercice13()
    elif choix=="14":
        exercice14()
    elif choix=="15":
        exercice15()
    elif choix=="16":
        exercice16()
    elif choix=="17":
        exercice17()
    elif choix=="18":
        exercice18()
    elif choix=="19":
        exercice19()
    elif choix=="20":
        exercice20()
    elif choix=="21":
        exercice21()
    elif choix=="22":
        exercice22()
    elif choix=="23":
        exercice23()
    elif choix=="24":
        exercice24()
    elif choix=="25":
        exercice25()
    elif choix=="26":
        exercice26()
    elif choix=="27":
        exercice27()
    elif choix=="28":
        exercice28()
    elif choix=="29":
        exercice29()
    elif choix=="30":
        exercice30()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()