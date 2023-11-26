from functions import *
from menu import *

def afficher_menu():
    print("Menu:")
    print("1. Afficher les mots les moins importants")
    print("2. Afficher les mots ayant le score TD-IDF le plus élevé")
    print("3. Indiquer les mots les plus répétés par un président")
    print("4. Indiquer les noms des présidents qui ont parlé de d'un mot et celui qui l’a répété le plus de fois")
    print("5. Indiquer le premier président à parler d'un mot")
    print("6. Afficher les mots que tous les présidents ont évoqués hormis les mots dits « non importants »")
    print("0. Quitter")

mots_moins_importants = calculer_mots_moins_importants(tfidf_matrice)


if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = input("Entrez le numéro de votre choix (0 pour quitter) : ")

        if choix == "1":
            print("Les mots moins importants sont :", mots_moins_importants)
        elif choix == "2":
            result = mots_importants(tfidf_matrice)
            print("Les mots ayant le score TD-IDF le plus élevé sont :", result)
        elif choix == "3":
            print("Choisissez un président :"
                  "1) Chirac"
                  "2) Giscard d'Estaing"
                  "3) Hollande"
                  "4) Macron"
                  "5) Mitterrand"
                  "6) Sarkozy")
            presidents = {
                '1': 'Chirac',
                '2': 'Giscard dEstaing',
                '3': 'Hollande',
                '4': 'Macron',
                '5': 'Mitterrand',
                '6': 'Sarkozy'
            }

            choix2 = input("Entrez le numéro de votre choix : ")

            while choix2 not in presidents:
                choix2 = input("Entrez le numéro de votre choix : ")

            pres = presidents[choix2]

            result = mots_comm_pre(pres, tf_matrice)
            print("Le mot le plus répété par le président",pres," est :", result)
        elif choix == "4":
            word=str(input("Saisir un mot :"))
            presidents, most_mentions_president = word_president(word, tf_matrice)
            print("Les présidents qui ont parlé de",word," sont :", presidents)
            print("Le président qui l'a répété le plus de fois est :", most_mentions_president)
        elif choix == "5":
            word=str(input("Saisir un mot :"))
            result=first_president_to_mention(word, tf_matrice)
            print("Le premier président à avoir parlé de",word,"est : ",result)
        elif choix == "6":
            result = common_words(tf_matrice, mots_moins_importants)
            print("Les mots que tous les présidents ont évoqués hormis les mots dits « non importants » sont :", result)
        elif choix == "0":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")