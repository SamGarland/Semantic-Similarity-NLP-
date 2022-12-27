# This programme defines a function that compares the string assigned to 'planet_hulk', to different movie descriptions
# in "movies.txt" using the inbuilt similarity method in spacy. A semantic similarity value is assigned to each movie 
# in the file and the movie with the highest semantic similarity is recommended to the user and returned by the function. 

import spacy

def movie_compare(input_description):
    
    with open("movies.txt", "r") as file:
       
        nlp = spacy.load('en_core_web_md')
        in_descrp = nlp(input_description)
        
        lines = file.readlines()
        movies = {}
        
        for line in lines:
            (key, value) = line.split(":")
            movies[key] = value
        
        for key, value in movies.items():
            value = nlp(value).similarity(in_descrp)
            movies[key] = value
        
        count = 0.00
        most_similar = ""
        
        for key, value in movies.items():
            if value >= count:
                most_similar = key
                count = value
            else:
                continue
        
        most_similar = most_similar.rstrip()
        
        print(f"If you liked 'Planet Hulk'', you'll like {most_similar}.")    
        return most_similar

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunatley, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

movie_compare(planet_hulk)