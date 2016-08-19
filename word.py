import string
import nltk
class ModifiedWPTokenizer( nltk.tokenize.RegexpTokenizer):
    def __init__(self):
        nltk.tokenize.RegexpTokenizer.__init__(self, r'\w+|[^\w\s]|\s+')
class SentenceTokenizer():
    # extracr punctuation features. features are: this word; previous word (lower case); next word capitalied? last word single char?features will be used to train while the features2 will be used to see data about whitespace
    def features(self, tokens, i):
        return {'next-capitalized': (i<len(tokens)-1) and tokens[i+1][0].isupper(),'prevword': tokens[i-1].lower(),'punct': tokens[i],'prev-one': len(tokens[i-1]) == 1}
    #to extract same feature from tuples also.(so as to include dat about whitespace)
    def features2(self,tokens, i):
        return {'next-capitalized': (i<len(tokens)-1) and tokens[i+1][0][0].isupper(),'prevword': tokens[i-1][0].lower(),'punct': tokens[i][0],'prev-one': len(tokens[i-1][0]) == 1}
        # naive bayes is used for training
    def __init__(self):
        self.tokenizer = ModifiedWPTokenizer()
        training_sents = nltk.corpus.treebank_raw.sents()
        tokens = []
        boundaries = set()
        offset = 0
        for sent in training_sents:
            tokens.extend(sent)
            offset += len(sent)
            boundaries.add(offset-1)
        featuresets = [(self. features(tokens,i), (i in boundaries)) for i in range(1, len(tokens)-1) if tokens[i] in '.?!']
        train_set = featuresets
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
    def classify_segment_sentences(self,words):
        start = 0
        sentence = []
        for i, word in enumerate(words):
            if word[0] in '.?!' and self.classifier.classify(self. features2(words,i)) == True:
                sentence.append(words[start:i+1])
                start = i+1
        if start <len(words):
            sentence.append(words[start:])
        return sentence
    def segment_text(self,full_text):
        text_words_sp = self.tokenizer.tokenize(full_text)
        word_tuples = []
        i =0
        while (i<len(text_words_sp)):
            word = text_words_sp[i]
            if (word.isspace()):
                word = " "    # convert all whitespace to a single space.
            if (i == len(text_words_sp)-1):
                word_tuples.append( (word,False) )
            else:
                word2 = text_words_sp[i+1]
                if (word2.isspace()):
                    i = i +1
                    word_tuples.append( (word,True) )
                else:
                    word_tuples.append( (word,False) )
            i = i +1

        sentences = []
        for sent in self.classify_segment_sentences(word_tuples):
            # sent holds the next sentence list of tokens
            sentence = []
            i = 0
            token = ""
            # to collapse abbreviations into single word tokens
            for i,tuple in enumerate(sent):
                if (tuple[0][0] in string.punctuation and not tuple[0][0] in '.?!'):
                    # punctuation that should be kept as a single token
                    if (len(token) > 0):
                        sentence.append(token)
                        token=""
                    sentence.append(tuple[0])
                elif (tuple[1]):
                    # space character
                    sentence.append( token+tuple[0] )
                    token = ""
                elif (i == len(sent)-2):
                    sentence.append( token+tuple[0] )
                    token = ""
                else:
                    token = token + tuple[0]
            # Add this token to the current sentence
            if len(token) > 0:
                sentence.append(tok)
            sentences.append(sentence)
        return sentences
