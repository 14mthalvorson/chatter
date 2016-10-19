import json
import wikipedia


# scores is a dictionary of dictionaries linking a base word with other words it is most closely associated with (excluding basics)
with open("scores.txt", 'a') as fileName:
    scores = json.load(fileName)

# links is a dictionary of dictionaries linking a base word
with open("scores.txt", 'a') as fileName:
    links = json.load(fileName)
with open("basics.txt", 'a') as fileName:
    basics = json.load(fileName)


def add_topic(title):
    #try:
    page = wikipedia.page(title)
    text = page.content
    text = word_list(text)
    #except Exception:
    #    pass


def word_list(text):
    chars = ".,<>/?;:!@#$%^&*()-_=+[]{}|\n\t"
    for char in chars:
        if char in text:
            text = text.replace(char, " ")
    while "  " in text:
        text.replace("  ", " ")
    list_of_words = text.split(" ")
    for word in list_of_words:
        word = word.lower()
    print(list_of_words)
    return list_of_words


title_list = wikipedia.random(10)
for title in title_list:
    print(title)
    add_topic(title)







