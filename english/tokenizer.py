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
kip_symbols = [',','.',' ','!','?','#','-']
skip_symbols = []
analyser = HfstBasicTransducer()

for word in skip_symbols:
	tokenizer.add_skip_symbol(word)
for word in words:
	if word not in skip_symbols:
		tokenizer.add_multichar_symbol(word)
print("Preprocessing completed")

test = "shan't can't wouldn't This some randomized test data which is not so random. I'm okay with it! Aren't you? The question is, what does the fox say, or rather the foxes say? Corp. Mr. Dr. www.prannayk.com google.com players cricketers balls"

def ignore(tokens):
	i = 0
	for symbols in kip_symbols:
		if tokens.count(symbols):
			i+=tokens.count(symbols)
	if i is 1:
		return True
	return False

#rint(tokenize(test))
def analyze(token):
	return pos_tag(token)

def tokenize(text):
	text = text.split(" ")
	tokens = []
	for word in text:
		temptokens = tokenizer.tokenize_one_level(word)
		if len(temptokens) > 1:
			if not ignore(word):
				tokens += (word,)
			else:
				tokens += temptokens
		else:
			tokens += temptokens
	return tokens

tokenized = tokenize(test)

analysed = {}
for tokens in tokenized:
	analysed.update(analyze((tokens,)))

for token in tokenized:
	print(token + ":" + analysed[token])
