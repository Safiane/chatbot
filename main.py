from functions import *

# Test :
'''
#Affichage des noms des fichiers
print("Noms des fichiers dans le répertoire:")
for i in files_names:
    print(i)

# Affiche les noms des présidents sans doublons
print("Noms des présidents:", president_names)

# Exemple d'utilisation
for president_name in president_names:
    first_name = first_name(president_name)
    print("Le prénom du président",president_name," est ",first_name)

# Boucle pour associer le prénom à chaque président et afficher le résultat
for president_name in president_names:
    prenom = prenom_president(president_name)
    print("Le prénom du président",president_name,"est :",prenom)
#Appel de la fonction conversion en min
output_directory = "cleaned"
convert_min(directory, output_directory, files_names)
#Appel de la fonction conversion sans ponctuation des textes déjà dans cleaned
convert_ponct(directory_cleaned, output_directory, files_names)
#Appel de la fonction conversion en min et sans ponct
convert_min_ponct()
#TF
tf_results = tf(directory_cleaned, files_names)
print(tf_results)
#IDF
idf_scores = idf(directory_cleaned, files_names)
print(idf_scores)
'''
idf_scores = idf(directory_cleaned, files_names)
print(idf_scores)
