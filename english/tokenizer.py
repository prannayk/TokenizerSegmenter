from libhfst import *
from nltk.corpus import treebank
print("Using the treebank lexicon")
# print(len(treebank.tagged_words()))

words = treebank.words()
tagged_words = treebank.tagged_words()
tokenizer = HfstTokenizer()
skip_symbols = [',','.',' ','!','?','#','-']

for word in skip_symbols:
	tokenizer.add_skip_symbol(word)
for word in words:
	if word not in skip_symbols:
		tokenizer.add_multichar_symbol(word)


# stemming for tokenization
test = "shan't can't wouldn't This some randomized test data which is not so random. I'm okay with it! Aren't you? The question is, what does the fox say, or rather the foxes say? Corp. Mr. Dr. www.prannayk.com google.com"

stringlist = test.split(" ")
tokens = []
for string in stringlist:
	temptoken =  tokenizer.tokenize_one_level(string)
	if len(temptoken) > 1:
		tokens += string
	else:
		tokens += temptoken