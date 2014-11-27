from trie import Trie
import random
import time

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
	maxInsert = 0
	maxContains = 0
	for w in words:

		add_start = time.time()
		t.addWord(w)
		add_end = time.time() - add_start
		maxInsert = max(maxInsert, add_end)

		if len(w) >= prefixLen:
			if w[:prefixLen] in test_prefixes:
				test_prefixes[w[:prefixLen]].add(w)

		contains_start = time.time()
		assert(w in t)
		contains_end = time.time() - contains_start
		maxContains = max(maxContains, contains_end)

	print 'Max time to add word was %f sec, Max time to check if word in trie was %f sec' % (maxInsert, maxContains)

	return t

def test_autocomplete(t, words):
	# how do we know the words that the algorithm finds are all the possible words
	for prefix in test_prefixes.keys():
		# we can check the equality of sets this way or ask if symmetric difference is 0
		start = time.time()
		completions = t.autocomplete(prefix)
		assert(completions == test_prefixes[prefix])
		print 'Autocomplete time for prefix "%s" with %d words was %f sec' % (prefix, len(completions), time.time() - start) 



''' Generate an arbitrary prefix of length prefixLen and add it to dictionary '''
def getPrefixes(prefixLen):
	pass

if __name__ == '__main__':
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
