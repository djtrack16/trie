class Trie():
	'''
	Naive trie implementation
	Complexity:
	Time: O(length of word)
	Space: O(M^n) where M = alphabet size (in our case, 26) and N = height of tree
	'''
	def __init__(self, children={}, endOfWord=False):
		self.children = children
		self.endOfWord = endOfWord

	def add(self, word):
		"""
		Adds a word to the trie.
		If word already in trie, changes nothing.
		If given empty string -> does nothing
		"""
		next = self
		for char in word:
			if not char in next.children:
				next.children[char] = Trie({})
			next = next.children[char]
		if word:
			next.endOfWord = True

	def delete(self, word):
		"""
		Delete word from trie.
		Four cases:
		1. Word is not in trie -> do nothing
		2. Word is in trie, but does not contain prefix or suffix of other words in tree,
		   -> delete entire word
		3. Word is prefix of another word in trie: set node.endOfWord to False, and we are done
		4. Another word is prefix of this word in trie: delete leaf nodes bottom-up until the
		   most recent endofword flag
		"""
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
		'''
		Returns true if words is in trie.
		Otherwise, returns false.
		Note: Only if endOfWord is marked on last letter in word, is the word in the trie.
		''' 
		node = self
		for char in word:
			if not char in node.children:
				return False
			node = node.children[char]
		return node.endOfWord
	
	def autocomplete(self, prefix):
		''' 
		Find the ending of the prefix in the tree where we should begin our autocomplete.
		Then returns a *generator* of all words beginning with this prefix
		'''
		node = self
		for char in prefix:
			if not char in node.children:
				# we return empty list if at any point a character of the prefix is not found in trie traversal
				#print 'Prefix \'%s\' doesn\'t exist in trie' % (prefix)
				return []
			node = node.children[char]
		return node.allSuffixes(prefix)

	def allSuffixes(self, prefix):
		'''
		Generate all possible words of a given prefix
		E.g. If given the empty string, will print all words in trie
		if given a prefix that is known to exist in tree, will give all words starting with that prefix (autocomplete feature)
		'''
		remaining_letters = self.children
		if self.endOfWord:
			yield prefix

		for char in remaining_letters.keys():
			prefix = ''.join([prefix, char])
			for word in remaining_letters[char].allSuffixes(prefix):
				yield word
