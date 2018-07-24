#import spacy for nlp
import spacy
#importing textacy which is based on spacy
import textacy.extract
from data import *
#load english model
nlp = spacy.load('en')

#inpute favourite text
title=input("Title :")
text=input("ENTER YOUR FAVOURITE PARAGRAPH HERE :")

# Parse the document with spaCy
paragraph = nlp(name)

# Extract semi-structured statements
sents = list(textacy.extract.semistructured_statements(paragraph,title))

# Print the results
print(sents)

for sent in sents:
    subject, verb, fact = sent
    print("subject :",subject)
    print("verb :",verb);
    print("fact :",fact)
