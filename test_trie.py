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

def test_autocomplete(t, words):
	# how do we know the words that the algorithm finds are all the possible words
	for prefix in test_prefixes.keys():
		# we can check the equality of sets this way or ask if symmetric difference is 0
		start = time.time()
		completions = t.autocomplete(prefix)
		assert(completions == test_prefixes[prefix])
		print 'Autocomplete time for prefix "%s" with %d words was %f sec' % (prefix, len(completions), time.time() - start) 

'''
Pops arbitrary elements from dictionary and tries to delete them, afterwards exhaustively checking that thiss didn't screw up any other word
in trie. Adds words back to dictionary and trie for next round of testing. Does this 'trials' number of times
'''
def test_batch_delete(t, words, trials, toDelete):
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


'''
Read in a large text file from path using 'cat /usr/share/dict/words > words.txt' (235K words) 
'''
def dictionary():
	f = open('./words.txt')
	words = set([])
	ct = 0
	for line in f:
		words.add(line[:-1])
		ct += 1
		if ct > 10000:
			break
	return words

if __name__ == '__main__':
	words = dictionary()
	t = test_add_and_contains(words, 3)
	#test_autocomplete(t, words)
	test_batch_delete(t, words, 1000, 100)
