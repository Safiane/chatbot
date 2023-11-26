import os
import math


#Lister les fichiers de speeches
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Appel de la fonction
directory = "C:\\Users\\safia\\PycharmProjects\\chatbot\\speeches"
extension = ".txt"
files_names = list_of_files(directory, extension)

#Supprimer les doublons des noms des présidents
def remove_duplicates(names):
    president_names = []
    for i in range(len(names)):
        a = (names[i][-1])
        if (chr(48) <= a <= chr(57)) :
            names[i] = names[i][:-1]
    for i in names:
        if not (i in president_names):
            president_names.append(i)
    return president_names

#Extraire les noms des présidents des noms de fichiers
def extract_president_names(files_names):
    names = []

    for filename in files_names:
        #les slices pour extraire le nom
        president_name = filename[11:-4]
        names.append(president_name)

    return names

# Appel de la fonction extract_president_names
names = extract_president_names(files_names)

# Appel de la fonction remove_duplicates pour supprimer les doublons
president_names = remove_duplicates(names)

#Associer un prénom à chaque président
def prenom_president(president_name):
    dict_presidents = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
    }

    #prendre le prénom à partir du dictionnaire
    prenom_president = dict_presidents.get(president_name)

    return prenom_president

#Convertir les textes en minuscules
def convert_min(directory, output_directory, files_names):
    for filename in files_names:
        chemin_fichier = os.path.join(directory, filename)
        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r') as file:
                content = file.read()
            #convertir en min
            content_min = ''
            for char in content:
                content_min += chr(ord(char) + 32) if 'A' <= char <= 'Z' else char
            #définir le chemin du fichier de sortie dans le répertoire "cleaned"
            fichier_destination = os.path.join(output_directory, filename)

            #écrire le contenu converti dans le nouveau fichier
            with open(fichier_destination, 'w') as file:
                file.write(content_min)
    #print("Conversion effectué en min")
#Appel de la fonction conversion
output_directory = "cleaned"
#convert_min(directory, output_directory, files_names)

#Supprimer ponctuation

def remove_ponctuation(content):
    ponctuations = "'.-!,;?"
    content_no_ponct = ''
    for char in content:
        content_no_ponct += char if char not in ponctuations else ' '

    return content_no_ponct

def convert_ponct(directory_cleaned, output_directory, files_names):
    # Parcourir les fichiers dans le répertoire "cleaned"
    for filename in files_names:
        chemin_fichier = os.path.join(directory_cleaned, filename)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r') as file:
                content = file.read()
            #suppr les ponct à l'aide de remove_ponctuation
            content_no_ponct = remove_ponctuation(content)

            #définir le chemin du fichier de sortie dans le répertoire "cleaned"
            fichier_destination = os.path.join(output_directory, filename)

            #écrire le contenu converti dans le nouveau fichier
            with open(fichier_destination, 'w') as file:
                file.write(content_no_ponct)
    #print("Conversion sans ponctuation effectué")
#convert_ponct(directory_cleaned, output_directory, files_names)

directory_cleaned = "C:\\Users\\safia\\PycharmProjects\\chatbot\\cleaned"

def convert_min_ponct():
    convert_min(directory, output_directory, files_names)
    convert_ponct(directory_cleaned, output_directory, files_names)
    print("Conversion des fichiers en min et sans ponctuations effectué")

#TF (Term Frequency - Fréquence du terme)
def count_occ(text):
    #Divisier le texte en mots
    words = text.split()

    #Dict pour stocker les occ de chaque mot
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def tf(directory_cleaned, files_names):
    tf_results = {}  #Dict pour stocker les résultats TF de chaque fichier
    for filename in files_names:
        chemin_fichier = os.path.join(directory_cleaned, filename)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r') as file:
                content = file.read()
                tf_results[filename] = count_occ(content)
    return tf_results
#tf_results = tf(directory_cleaned, files_names)

#IDF (Inverse Document Frequency - Fréquence Inverse du Document)

def calculate_idf(total_documents, doc_frequence):
    idf_scores = {}
    for word, frequence in doc_frequence.items():
        idf_scores[word] = math.log10(total_documents / frequence)
    return idf_scores


def idf(directory_cleaned, files_names):
    total_documents = len(files_names)

    # Dict pour stocker le nombre de documents contenant chaque mot
    doc_frequence = {}

    for filename in files_names:
        chemin_fichier = os.path.join(directory_cleaned, filename)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'r') as file:
                content = file.read()
            words = content.split()

            # Liste pour mots uniques
            mots_unique = []
            for word in words:
                if word not in mots_unique:
                    mots_unique.append(word)

            # Mettre à jour le dictionnaire doc_frequence pour chaque mot unique
            for word in mots_unique:
                doc_frequence[word] = doc_frequence.get(word, 0) + 1

    idf_scores = calculate_idf(total_documents, doc_frequence)
    return idf_scores

#idf_scores = idf(directory_cleaned, files_names)

