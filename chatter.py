import json

# Initializes scores dictionary
with open("scores.txt", "r") as file_name:
    scores = json.load(file_name)

# Initializes links dictionary
with open("links.txt", "r") as file_name:
    links = json.load(file_name)

# Returns list of words most related to a keyword
def get_top_scores(keyword):
    # Get keyword's dictionary from within scores dictionary
    connections = scores.get(keyword, {})

    # Creates list of tuples with connections and their respective scores
    connections_list = [(k, connections[k]) for k in connections.keys()]

    # Sort list by descending score value
    connections_list = sorted(connections_list, key=lambda x: x[1], reverse=True)

    print(connections_list)

# Returns list of most common words succeeding keyword
def get_top_links(keyword):
    # Get keyword's dictionary from within links dictionary
    connections = links.get(keyword, {})

    # Creates list of tuples with connections and their respective link scores
    connections_list = [(k, connections[k]) for k in connections.keys()]

    # Sort list by descending score value
    connections_list = sorted(connections_list, key=lambda x: x[1], reverse=True)

    print(connections_list)

get_top_scores("revolution")
get_top_links("revolution")

