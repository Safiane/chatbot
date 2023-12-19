import os
import math


#Partie 1:
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "C:/Users/safia/PycharmProjects/chatbot/speeches"
files_names = list_of_files(directory, "txt")

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

def extract_president_names(files_names):
    names = []
    for filename in files_names:
        president_name=filename[11:-4]
        names.append(president_name)
    return names

president_names_with_duplicates = extract_president_names(files_names)
president_names = remove_duplicates(president_names_with_duplicates)

def associate_first_name_president(president_name):
    presidents_name= {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
    }
    first_name=presidents_name.get(president_name)

    return first_name

def convert_min(directory,cleaned_directory,files_names):
    for filename in files_names:
        path_file=os.path.join(directory,filename)
        with open(path_file, 'r') as file:
            content=file.read()
        content_min = ''
        for char in content:
            if 'A' <= char <= 'Z':
                content_min += chr(ord(char) + 32)
            else:
                content_min += char
        cleaned_file=os.path.join(cleaned_directory,filename)
        with open(cleaned_file,'w') as file:
            file.write(content_min)
    print("Conversion effectué en min")

cleaned_directory = "cleaned"
directory_cleaned = "C:/Users/safia/PycharmProjects/chatbot/cleaned"

def remove_ponctuation(content):
    ponctuations="'.-!,;?()"
    content_no_ponct=''
    for char in content:
        if char not in ponctuations:
            content_no_ponct+=char
        else:
            content_no_ponct+=' '
    return content_no_ponct

def convert_ponct(directory_cleaned,cleaned_directory,files_names):
    for filename in files_names:
        path_file = os.path.join(directory_cleaned,filename)
        with open(path_file,'r') as file:
            content=file.read()
        content_no_ponct=remove_ponctuation(content)
        cleaned_file=os.path.join(cleaned_directory,filename)
        with open(cleaned_file,'w') as file:
            file.write(content_no_ponct)
    print("Conversion sans ponctuation effectué")

def word_frequency(text):
    word_count={}
    for word in text.split():
        if word:
            word_count[word]=word_count.get(word,0) + 1
    return word_count

def tf(directory_cleaned,files_names):
    tf_results={}
    for filename in files_names:
        path_file = os.path.join(directory_cleaned,filename)
        with open(path_file,'r') as file:
            content=file.read()
            tf_results[filename] = word_frequency(content)
    return tf_results

tf_scores = tf(cleaned_directory, files_names)

def idf(cleaned_directory,files_names):
    num_documents=len(files_names)
    word_document_count={}
    for filename in files_names:
        path_file = os.path.join(cleaned_directory,filename)
        with open(path_file, 'r') as file:
            content=file.read()
            unique_words=set(content.split())
            for word in unique_words:
                if word:
                    word_document_count[word]=word_document_count.get(word,0) + 1
    word_idf={}
    for word,document_count in word_document_count.items():
        word_idf[word] = math.log(num_documents / (1 + document_count))

    return word_idf

idf_scores = idf(cleaned_directory, files_names)

def calculate_tf_idf_matrix(cleaned_directory, files_names, tf_scores, idf_scores):
    unique_words = set()
    tf_idf_matrix = []

    for filename in files_names:
        chemin_fichier = os.path.join(cleaned_directory, filename)
        with open(chemin_fichier, 'r') as file:
            content = file.read()
            unique_words.update(set(content.split()))

    for filename in files_names:
        tf_idf_vector = []
        path_file = os.path.join(cleaned_directory, filename)
        with open(path_file, 'r') as file:
            content = file.read()
            for word in unique_words:
                tf_score = tf_scores[filename].get(word, 0)
                idf_score = idf_scores.get(word, 0)
                tf_idf_value = tf_score * idf_score
                tf_idf_vector.append(tf_idf_value)

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix

tf_idf_matrix = calculate_tf_idf_matrix(cleaned_directory, files_names, tf_scores, idf_scores)
#Nombre de lignes=nombre de mots dans le corpus Nombre de colonnes=nombre de document
def transpose_matrix(matrix):
    num_rows=len(matrix)
    num_cols=len(matrix[0])

    transposed_matrix = []

    for j in range(num_cols):
        transposed_row = []
        for i in range(num_rows):
            transposed_row.append(matrix[i][j])
        transposed_matrix.append(transposed_row)
    return transposed_matrix

tf_idf_transposed = transpose_matrix(tf_idf_matrix)
#Nombre de lignes=nombre de document Nombre de colonnes=nombre de mots dans le corpus

#Partie 2:
def tokenize_question(question):
    punctuation="'.-!,;?()"
    question_no_punc_min = ''
    for char in question:
        if 'A' <= char <= 'Z':
            question_no_punc_min += chr(ord(char) + 32)
        elif char not in punctuation:
            question_no_punc_min+= char
        else:
            question_no_punc_min += ' '
    question_tokens = question_no_punc_min.split()
    return question_tokens

def find_common_terms(question, cleaned_directory, files_names):
    question_tokens = tokenize_question(question)
    corpus_words = set()
    for filename in files_names:
        path_file = os.path.join(cleaned_directory, filename)
        with open(path_file, 'r') as file:
            content = file.read()
            corpus_words.update(set(content.split()))
    common_terms = set(question_tokens) & corpus_words

    return common_terms

def calculate_tfidf_vector(question_tokens, tf_scores, idf_scores):
    tfidf_vector = []
    for word in question_tokens:
        tf_score = question_tokens.count(word)
        tfidf_vector.append(tf_score * idf_scores.get(word, 0))

    return tfidf_vector

def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))


def vector_norm(vector):
    return math.sqrt(sum(x ** 2 for x in vector))


def cosine_similarity(vector_a, vector_b):
    dot_product_value = dot_product(vector_a, vector_b)
    norm_a = vector_norm(vector_a)
    norm_b = vector_norm(vector_b)

    if norm_a == 0 or norm_b == 0:
        return 0  # Pour éviter la division par zéro

    similarity = dot_product_value / (norm_a * norm_b)
    return similarity


def document_pertinent(tf_idf_matrix, question_tfidf_vector, files_names):
    max_similarity = 0
    most_pertinent_document = None

    for i, document_vector in enumerate(tf_idf_matrix):
        similarity = cosine_similarity(question_tfidf_vector, document_vector)
        if similarity > max_similarity:
            max_similarity = similarity
            most_pertinent_document = files_names[i]

    return most_pertinent_document

def find_most_relevant_word(question, tf_scores, idf_scores):
    question_tokens = tokenize_question(question)
    tfidf_vector = calculate_tfidf_vector(question_tokens, tf_scores, idf_scores)
    max_tfidf_word = max(zip(question_tokens, tfidf_vector), key=lambda x: x[1])[0]

    return max_tfidf_word

def response(most_pertinent_doc, most_relevant_word, question):
    with open("C:/Users/safia/PycharmProjects/chatbot/speeches/"+most_pertinent_doc, 'r') as file:
        content = file.read()
        sentences = content.split('.')
        for sentence in sentences:
            if most_relevant_word in sentence:
                refined_response = sentence.strip().capitalize()
                if not refined_response.endswith('.'):
                    refined_response += '.'
                question_starters = {
                    "Comment": "Après analyse, ",
                    "Pourquoi": "Car, ",
                    "Peux-tu": "Oui, bien sûr!"
                }
                for starter, reply in question_starters.items():
                    if question.startswith(starter):
                        refined_response = reply + refined_response
                        break
                return refined_response
    return "Aucune phrase trouvée."
