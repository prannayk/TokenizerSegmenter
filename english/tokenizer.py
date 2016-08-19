from libhfst import *
from nltk import pos_tag,word_tokenize
from nltk.corpus import treebank
from nltk.corpus import brown
print("Using the treebank lexicon")

words = treebank.words()
words += brown.words()
tagged_words = treebank.tagged_words()
tagged_words += brown.words()
tokenizer = HfstTokenizer()
skip_symbols = [',','.',' ','!','?','#','-']

analyser = HfstBasicTransducer()

for word in skip_symbols:
	tokenizer.add_skip_symbol(word)
for word in words:
	if word not in skip_symbols:
		tokenizer.add_multichar_symbol(word)
print("Preprocessing completed")

test = "shan't can't wouldn't This some randomized test data which is not so random. I'm okay with it! Aren't you? The question is, what does the fox say, or rather the foxes say? Corp. Mr. Dr. www.prannayk.com google.com"

def analyze(token):
	return pos_tag(token)

def tokenize(text):
	text = text.split(" ")
	tokens = []
	for word in text:
		temptokens = tokenizer.tokenize_one_level(word)
		if len(temptokens) > 1:
			tokens += (word,)
		else:
			tokens += temptokens
	return tokens

analysed = {}
for tokens in tokenize(test):
	analysed.update(analyze((tokens,)))
