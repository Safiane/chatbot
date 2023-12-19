from functions import *
from test import *

directory = "C:/Users/safia/PycharmProjects/chatbot/speeches"
cleaned_directory = "cleaned"
directory_cleaned = "C:/Users/safia/PycharmProjects/chatbot/cleaned"
question_starters = {
    "Comment": "Après analyse, ",
    "Pourquoi": "Car, ",
    "Peux-tu": "Oui, bien sûr!"
}

def print_menu():
    print("\nMenu:")
    print("1. Mode Chatbot")
    print("2. Quitter")

def chatbot_mode():
    while True:
        question = input("Posez une question (ou tapez '2' pour quitter): ")

        if question.lower() == '2':
            break
        question_tokens = tokenize_question(question)
        comm_terms = find_common_terms(question, cleaned_directory, files_names)
        tf_idf_question = calculate_tfidf_vector(question_tokens, tf_scores, idf_scores)
        most_pertinent_doc = document_pertinent(tf_idf_matrix, tf_idf_question, files_names)
        most_relevant_word = find_most_relevant_word(question, tf_scores, idf_scores)
        generated_response = response(most_pertinent_doc, most_relevant_word, question)
        print("Réponse:", generated_response)

while True:
    print_menu()
    choice = input("Choisissez une option (1 ou 2): ")

    if choice == '1':
        chatbot_mode()
    elif choice == '2':
        print("Programme terminé.")
        break
    else:
        print("Veuillez choisir une option valide.")






