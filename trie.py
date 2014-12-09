class Trie():

	''' Naive trie implementation

		Complexity:
		Time: O(length of word)
		Space: O(M^n) where M = alphabet size (in our case, 26) and N = height of tree
		Every node is a dictionary, listing all the possible suffixes of this character so far in the trie
	'''

	def __init__(self, children={}, endOfWord=False):
		self.children = children
		self.endOfWord = endOfWord

	def add(self, word):
		next = self
		for char in word:
			if not char in next.children:
				next.children[char] = Trie({})
			next = next.children[char]
		next.endOfWord = True

	def delete(self, word):
		# Four cases:
		# 1. Word is not in trie: do nothing
		# 2. Word does not contain prefix of another word or is the prefix of any other word: delete all nodes in word
		# 3. Word is prefix of another word in trie: set node.endOfWord to False, and we are done
		# 4. Another word is prefix of this word in trie: delete leaf nodes bottom-up until the most recent endofword flag

		node = self
		# base case
		if node.endOfWord and not word:
			node.endOfWord = False
 			#CASE 3
			if node.children:
				return False
			return True

		char = word[0]

		# CASE 1
		if not char in node.children:
			return False

		node = node.children[char]

		#CASE 2 AND 4
		if node.delete(word[1:]):
			if node.endOfWord and word:
				return False
			del node
			return True



	def __contains__(self, word): 
		node = self
		for char in word:
			if not char in node.children:
				return False
			node = node.children[char]
		# only a word if we have found all characters in the word in correct order
		# and our stopping place happens to have 'endofword == True'
		return node.endOfWord
	
	''' 
	Find the node in the tree where we should begin our autocomplete.
	Then return all suffixes ending with this word
	'''
	def autocomplete(self, prefix):
		node = self
		for char in prefix:
			if not char in node.children:
				# we return empty list if at any point a character of the prefix is not found in trie traversal
				#print 'Prefix \'%s\' doesn\'t exist in trie' % (prefix)
				return []
			node = node.children[char]
		words = set([])
		node.allSuffixes(prefix, words)
		return words

	'''
	Generate all possible suffixes of a given prefix
	E.g. If given the empty string, will print all words in trie
	If given a prefix that is known to exist in tree, will give all words starting with that prefix (autocomplete feature)
	'''
	def allSuffixes(self, suffix, words):
		prefix = self.children
		if self.endOfWord:
			words.add(suffix)

		for char in prefix.keys():
			prefix[char].allSuffixes(suffix+char, words)