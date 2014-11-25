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

	def addWord(self, word):
		next = self
		for char in word:
			if not char in next.children:
				next.children[char] = Trie({})
			next = next.children[char]
		next.endOfWord = True

	def deleteWord(self, word):
		# we cannot only delete the last character
		# we have to delete up to the latest previous end of word.
		pass

	# what happens when we call 'in' operator
	def __contains__(self, word): 
		node = self
		for char in word:
			if not char in node.children:
				return False
			node = node.children[char]
		# only a word if we have found all characters in the word in correct order
		# and our stopping place happens to have 'endofword == True'
		return node.endOfWord
	
	''' find the node in the tree where we should begin our autocomplete '''
	def autocomplete(self, prefix):
		node = self
		for char in prefix:
			if not char in node.children:
				# we return empty list if at any point a character of the prefix is not found in trie traversal
				print 'Prefix \'%s\' doesn\'t exist in trie' % (prefix)
				return
			node = node.children[char]
		node.allSuffixes(prefix)

	''' Generate all possible suffixes of a given prefix
		E.g. If given the empty string, will print all words in trie
		If given a prefix that is known to exist in tree, will give all words starting with that prefix (autocomplete feature)
	'''
	def allSuffixes(self, suffix):
		prefix = self.children
		if self.endOfWord:
			print suffix

		for char in prefix.keys():
			prefix[char].allSuffixes(suffix+char)
			

