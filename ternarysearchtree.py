class TernarySearchTree():

	# ternary search trees can be used any time a hashtable would be used to store strings
	# tries are suitable when there is a proper distribution of words over the alphabet(s).
	# ternary trees are more space-efficient when the strings to be stored share a common prefix
	# for "given a word, find the next word in dictionary" or
	# "find all telephone numbers with 9342" or "typing few starting character in a web browser
	# " .... displays all website names with this prefix (i.e. auto complete feature)"
	# 

	#Design: left < node, right > node, down >= node
	# each node is a prefix of stored strings. all strings in the middle subtree of a node
	# start with that prefix.
	def __init__(self, value=None, left=None, right=None, equal=None, endOfWord=False):
		self.value = value
		self.left = left
		self.right = right
		self.equal = equal ## this is the only way we build actual words, left and right paths do not build words
		self.endOfWord = False


	def __contains__(self, word):
		node = self
		while node != None:
			
			c = word[0]
			if c == node.value:
				word = word[1:]
				if word == '':
					return node.endOfWord
				node = node.equal

			elif c > node.value:
				node = node.right

			elif c < node.value:
				node = node.left

		return False


	def insert(self, word):

		c = word[0]
		if not self.value:
			self.value = c

		if c < self.value:

			if not self.left: self.left = TernarySearchTree()
			self.left.insert(word)

		elif c > self.value:

			if not self.right: self.right = TernarySearchTree()
			self.right.insert(word)

		else:
			if len(word) == 1:
				self.endOfWord = True
				return

			if not self.equal: self.equal = TernarySearchTree()
			self.equal.insert(word[1:])

	def delete(self, word):
		pass

	def traverse(self):
		# if we want to see how our tree is constructed
		if self.left:
			self.left.traverse()
		if self.equal:
			self.equal.traverse()
		if self.right:
			self.right.traverse()
		print self.value

	def allSuffixes(self, prefix):
		if self.endOfWord:
			print prefix+self.value

		if self.left:
			self.left.allSuffixes(prefix)
		if self.right:
			self.right.allSuffixes(prefix)
		if self.equal:
			self.equal.allSuffixes(prefix+self.value)


	def autocomplete(self, prefix):
		node = self
		#pre = prefix
		k = 0
		while node != None:
			
			c = prefix[k]
			if c == node.value:
				k += 1
				node = node.equal
				if k == len(prefix):
					break

			elif c > node.value:
				node = node.right

			elif c < node.value:
				node = node.left

		if k < len(prefix):
			print 'Prefix "%s" doesn\'t exist in tree' % (prefix)
			return

		node.allSuffixes(prefix)

	def destroy(self):
		# what if we want to destroy the tree,
		# we have to do so in bottom up fashion (post order traversal)
		# deleting all leaves first and then deleting their parents
		if self.left: self.left.destroy()
		if self.right: self.right.destroy()
		if self.equal: self.equal.destroy()
		# we can use variable=None or del variable.
		# we release the attributes first, and then delete the tree itself
		# the use of del vs None is somewhat debated within the python community
		# i won't debate here
		self.value = None
		self.endOfWord = None
		del self



if __name__ == '__main__':
	words = ['baby','food', 'fool','folly', 'bat', 'back', 'fish', 'fruit', 'pie', 'pies']
	#words = ['lukasz', 'luke', 'ruby', 'run']
	#words = ['fox', 'foe', 'folly', 'foolishness', 'fop', 'fooled', 'fondle']
	t = TernarySearchTree()
	for w in words:
		t.insert(w)
	t.autocomplete('ba')
	t.autocomplete('baa')
	t.autocomplete('fo')
	t.autocomplete('po')