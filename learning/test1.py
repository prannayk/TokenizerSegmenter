from libhfst import *

set_default_fst_type(FOMA_TYPE)

tok = HfstTokenizer()

tok.add_multichar_symbol('foo')
tok.add_multichar_symbol('bar')
tok.add_multichar_symbol('baz')

words = tokenized_fst(tok.tokenize('foobarfoo'))
t = tokenized_fst(tok.tokenize('foobarbaz'))
words.disjunct(t)

rule = regex('bar (->) baz || foo _ foo')
words.compose(rule).minimize()

results = 0
try :
	results = words.extract_paths(output='dict')
except exceptions.TransducerIsCyclicException as e:
	print("FAILED")
	exit(1)

for inputs,outputs in results.items():
	print("%s:" % inputs)
	for output in outputs:
		print('%s\t%f'%(output[0],output[1]))
