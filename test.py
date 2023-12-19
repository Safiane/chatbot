from functions import *
'''
#Affiche la liste des mots les moins importants
non_important_words=[]
for word, idf_score in idf_scores.items():
    if idf_score==0:
        non_important_words.append(word)
print("Mots non importants :", non_important_words)

#Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé
max_tfidf_words=[]
max_tfidf_value=None

for word, tfidf_value in idf_scores.items():
    if max_tfidf_value is None or tfidf_value > max_tfidf_value:
        max_tfidf_words=[word]
        max_tfidf_value=tfidf_value
    elif tfidf_value==max_tfidf_value:
        max_tfidf_words.append(word)

#Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac hormis les mots dits « non importants » :
chirac_words_count={}
for filename in files_names:
    if "Chirac" in filename:
        path_file=os.path.join(cleaned_directory, filename)
        with open(path_file, 'r') as file:
            content=file.read()
            words=content
            for word in words:
                if word not in non_important_words:
                    chirac_words_count[word]=chirac_words_count.get(word,0)+1
most_common_chirac_words=[]
most_common_chirac_count=None
for word,count in chirac_words_count.items():
    if most_common_chirac_count is None or count>most_common_chirac_count:
        most_common_chirac_words=[word]
        most_common_chirac_count=count
    elif count==most_common_chirac_count:
        most_common_chirac_words.append(word)
print("Mot le plus répété par Chirac (hors mots non importants) :",most_common_chirac_words,"Nombre d'occurrences : ",most_common_chirac_count)

#Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois :
nation_counts={}

for filename in files_names:
    with open(os.path.join(cleaned_directory, filename), 'r') as file:
        content=file.read()
        nation_occurrences=content.count("nation")
        if nation_occurrences > 0:
            president_name=extract_president_names([filename])[0]
            nation_counts[president_name]=nation_counts.get(president_name, 0) + nation_occurrences

president_most_mentions_nation=max(nation_counts, key=nation_counts.get)
most_mentions_nation_count=nation_counts[president_most_mentions_nation]

print(f"Président ayant le plus parlé de la Nation : ",president_most_mentions_nation,"Nombre de mentions : ",most_mentions_nation_count)

#Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé du climat et/ou de l’écologie :
climate_ecology_counts={}

for filename in files_names:
    with open(os.path.join(cleaned_directory, filename), 'r') as file:
        content=file.read().lower()
        if "climat" in content or "écologie" in content:
            president_name=extract_president_names([filename])[0]
            climate_ecology_counts[president_name]=climate_ecology_counts.get(president_name, 0) + 1

presidents_mentioned_climate_ecology=list(climate_ecology_counts.keys())

print("Président(s) ayant parlé du climat et/ou de l'écologie :", presidents_mentioned_climate_ecology)
'''

