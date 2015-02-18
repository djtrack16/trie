from trie import Trie
import random
import time

prefixes = [
	'abo',
	'klo',
	'kra',
	'mon',
	'fel',
	'gir',
	'pul',
	'lio',
	'que',
	'coc'
]

def test_add_and_contains(words, prefixLen, test_prefixes):
	'''
	Adds words to trie, and verifies word is in trie with __contains__ method
	'''
	t = Trie()
	maxInsert = 0
	maxContains = 0
	for w in words:

		add_start = time.time()
		t.add(w)
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

def test_autocomplete(t, words, test_prefixes):
	'''
	Testing to make sure autocomplete finds all possible words that complete the prefix
	We use the prefixes from test_prefixes dictionary above as a global.
	'''
	for prefix in test_prefixes.keys():
		# we can check the equality of sets this way or ask if symmetric difference is 0
		start = time.time()
		completions = {elem for elem in t.autocomplete(prefix)}
		assert(completions == test_prefixes[prefix])
		print 'Autocomplete time for prefix "%s" with %d words was %f sec' % (prefix, len(completions), time.time() - start) 


def test_batch_delete(t, words, trials, toDelete):
	'''
	Pops arbitrary elements from dictionary and tries to delete them,
	afterwards exhaustively checking that thiss didn't screw up any other word
	in trie. Adds words back to dictionary and trie for next round of testing.
	Does this 'trials' number of times
	'''
	for trial in xrange(trials):
		prefixes = set([])
		for x in xrange(toDelete):
			elem = words.pop()
			prefixes.add(elem)
			t.delete(elem)
		for w in words:
			# the only elements not in trie are the ones we deleted
			if not w in t:
				assert(w in prefixes)
		for pre in prefixes:
			words.add(pre)
			t.add(pre)


def dictionary():
	'''
	Read in a large text file from path using 'cat /usr/share/dict/words > words.txt' (235K words) 
	'''
	f = open('./words.txt')
	words = set([])
	for line in f:
		words.add(line[:-1])
	return words

if __name__ == '__main__':
	words = dictionary()
	test_prefixes = {prefix: set([]) for prefix in prefixes}
	t = test_add_and_contains(words, 3, test_prefixes)
	test_autocomplete(t, words, test_prefixes)
	test_batch_delete(t, words, 1000, 100)
