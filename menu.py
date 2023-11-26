from functions import *
from menu import *

directory = "C:\\Users\\safia\\PycharmProjects\\chatbot\\speeches"
extension = ".txt"
output_directory = "cleaned"
directory_cleaned = "C:\\Users\\safia\\PycharmProjects\\chatbot\\cleaned"
files_names = list_of_files(directory, extension)
names = extract_president_names(files_names)
president_names = remove_duplicates(names)
tf_matrice = tf(directory_cleaned, files_names)
tfidf_matrice = tfidf_matrice(directory_cleaned, files_names)

# 1 Afficher liste des mots les - importants dans les doc
def calculer_mots_moins_importants(tfidf_matrice):
    mots_moins_importants = []
    for filename, dic in tfidf_matrice.items():
        for word, tfidf_score in dic.items():
            if tfidf_score == 0 and word not in mots_moins_importants:
                mots_moins_importants.append(word)
    return mots_moins_importants

mots_moins_importants = calculer_mots_moins_importants(tfidf_matrice)


# 2 Afficher les mots ayant le score TD-IDF le + élevé
def mots_importants(tfidf_matrice):
    mots_importants = {}
    for filename, dic in tfidf_matrice.items():
        max_tfidf_word = 0
        max_tfidf_score = 0
        for word, tfidf_score in dic.items():
            if tfidf_score > max_tfidf_score :
                max_tfidf_word = word
                max_tfidf_score = tfidf_score
        mots_importants[filename] = (max_tfidf_word, max_tfidf_score)
    return mots_importants

# 3 Mots les plus répétés par un président
def mots_comm_pre(president_name, tf_matrice):
    president_words = tf_matrice.get(president_name, {})
    comm_word = None
    comm_count = None
    for word, count in president_words.items():
        if comm_count is None or count > comm_count:
            comm_word = word
            comm_count = count
    return comm_word


#  4 Présidents qui ont mentionnés un mot et celui qui l’a répété le +
def word_president(word, tf_matrice):
    presidents_mention_word = []
    for president_name, words in tf_matrice.items():
        if word in words:
            presidents_mention_word.append(president_name)

    mentions_president = 0
    mentions_count = 0
    for president_name in presidents_mention_word:
        count = tf_matrice[president_name].get(word, 0)
        if count > mentions_count:
            mentions_president = president_name
            mentions_count = count

    return presidents_mention_word, mentions_president

# 5 Président mentionnant en premier un mot

def first_president_to_mention(word, tf_matrice):
    for president_name, words in tf_matrice.items():
        if word in words:
            return president_name

# 6 Mots comm des présidents
def common_words(tf_matrice, mots_moins_importants):
    #Ici j'ai pris les mots du premiers présidents comme base et j'ai enlevé tt les mots - important (tf=0)
    common_words = set(tf_matrice[list(tf_matrice.keys())[0]].keys())
    common_words = common_words - set(mots_moins_importants)

    for president_name, words in tf_matrice.items():
        common_words_temp = set()
        for word in common_words:
            if word in words:
                common_words_temp.add(word)
        common_words = common_words_temp

    return list(common_words)