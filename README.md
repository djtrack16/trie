trie
====

Herein lies a naive, simple trie implementation.

*Advantages*

* Fast lookup time: O(length of word)
* Great for use when there are a large number of short keys; even better, if they have common prefixes.
* We can provide alphabetical ordering of entries by key (although I don't implement that here, perhaps by pre-order traversal)
* 

*Disadvantages*

* Depending on one's implementation, tries don't have to rebuild or resize when they are full (which can be quite expensive) -- unless you are using hash tables to store the children of each node -- which I am. Hey, I said this was the naive impl.
* Highly space inefficient: O(alphabet_size^k) where k is height of tree. So assume tree is of height 4 and every node has the maximum no. of children and using English alphabet, we have 26^0+26^1+26^2+26^3 nodes -- and here, max length of string is merely 4 characters!
* 

**Complexity:**

**n** is length of word

* Membership: O(n)
* Insert: O(n)
* Delete: O(n) (Estimated, have not implemented yet)
* Size: O(1) 


Usage:

root = Trie()

*Add a word, using:*

root.addWord(string)

*Check if string is in trie*

root.addWord('apple')
'apple in trie' returns True

*Generates all suffixes starting with this prefix (e.g. will print all words in trie if passed empty string)*

root.autocomplete(prefix)

**TODO:**
- Add support for deleting words.
- Run timed tests.
- Add support for other alphabets besides "normal" characters (e.g. bitwise tries, etc)
- Lexicographic sorting by character

Maybe, I will re-implement this as a compact prefix tree, or I will have it alongside it.
I will soon upload a less naive implementation, similar to a ternary search tree.




