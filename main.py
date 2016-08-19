import os
import string
from word import SentenceTokenizer
print "Opening text data file"
f = open("1.txt","r")
print "Reading text..."
lines_text = f.readlines()
f.close()
full_text = ""
for s in lines_text:
    full_text = full_text + " " + s
print "Creating tokenizer..."
Tokenizer = SentenceTokenizer()

print "Segmenting text into words and sentences..."
sentences = Tokenizer.segment_text(full_text)

print "Segmented sentences:"
for sentence in sentences:
    print sentence
