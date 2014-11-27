from trie import Trie
import random

test_prefixes = {
	'abo': set([]),
	'klo': set([]),
	'kra': set([]),
	'mon': set([]),
	'fel': set([]),
	'gir': set([]),
	'pul': set([]),
	'lio': set([]),
	'que': set([]),
	'coc': set([]),
}
def test_add_and_contains(words, prefixLen):
	t = Trie()
	#test_prefixes = {} # as we build the tree, we get all the words starting with the prefixes we want to test
	for w in words:
		t.addWord(w)
		if len(w) >= prefixLen:
			if w[:prefixLen] in test_prefixes:
				test_prefixes[w[:prefixLen]].add(w)
		assert(w in t)
	return t

def test_autocomplete(t, words):
	# how do we know the words that the algorithm finds are all the possible words
	for prefix in test_prefixes.keys():
		#print t.autocomplete(prefix).symmetric_difference(test_prefixes[prefix])
		assert(t.autocomplete(prefix) == test_prefixes[prefix])

''' Generate an arbitrary prefix of length prefixLen and add it to dictionary '''
def getPrefixes(prefixLen):
	pass

if __name__ == '__main__':
	#words = ['baby', 'food', 'peach', 'peaches', 'pie', 'doll', 'wisdom', 'rosemary', 'dolt', 'sun', 'sundry']
	t = Trie()
	'''
	Read in a large text file from path using 'cat /usr/share/dict/words > words.txt' (235K words) 
	'''
	f = open('./words.txt')
	words = set([])
	for line in f:
		words.add(line[:-1])

	test_add_and_contains(words, 3)
	test_autocomplete(t, words)
