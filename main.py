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
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()