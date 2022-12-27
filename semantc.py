import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

#==== Note ====#

# The semantic similarity between cat and monkey is not surprising. 
# Similarity between monkey and banana is very interesting because I would have considered this 
# a pragmatic similarity i.e. a similarity in 'use' rather than in inherent 'meaning'.
# Furthermore, it's interesting to consider that there is some semantic similarity between banana and cat - 
# is this because they are both nouns i.e. 'syntactic similarity' rather than because there similarity in meaning?

#==== My own example ====#:

word1 = nlp("swede")
word2 = nlp("leaf")
word3 = nlp("root")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

# Interesting that spacy can't deal well with words with multiple meanings.

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
   for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("\n")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
