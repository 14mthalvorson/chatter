import wikipedia
import json
import re

# Selects the number of most common words to list
top_n_basic_words = 200

# Loads dictionary of most common words from basics_counts.txt
with open("basics_counts.txt", "r") as fileName:
    count_of_words = json.load(fileName)

for i in range(5000):
    try:
        # Uses Wikipedia API to get random article (object)
        title = wikipedia.random(1)

        # Prints article number and title
        print(str(i + 1) + ". " + title)

        # Creates string of lowercase text from Wikipedia article
        article_text = wikipedia.page(title).content.lower()

        # Iterates through words in article text
        for word in re.findall("[0-9A-z']+", article_text):
            count_of_words[word] = count_of_words.get(word, 0) + 1

    # Occasional errors retrieving file
    except:
        print("Error, skipping " + title)

    # Updates basics.txt file with most recent list every nth times (n = 5 below)
    if i % 10 == 0:

        # Creates list of words (v) and their count (k)
        basics = [(v, k) for v, k in count_of_words.items()]
        
        # Sorts list in descending order, truncates based on number of words wanted
        basics = sorted(basics, key=lambda x:x[1], reverse=True)[:top_n_basic_words]
        
        # Creates list of just words (removing count)
        basics = [x[0] for x in basics]

        # Dumps list in json format into basics.txt file
        with open('basics.txt', 'w') as file_name:
            json.dump(basics, file_name)

        # Updates basics_counts.txt to reflect updated dictionary (building over time instead of erasing after run)
        with open("basics_counts.txt", "w") as file_name:
            json.dump(count_of_words, file_name)
