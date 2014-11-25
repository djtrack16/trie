trie
====

Herein lies a naive, simple trie implementation.

**Complexity:**

Space complexity is O(alphabet_size^k) where K is height of tree
*Fast search time, but horrible memory usage*

Time complexity is done by method:

**n** is length of word

* Membership: O(n)
* Insert: O(n)
* Delete: O(n) (Estimated, have not implemented yet)
* Size: O(1) 


Usage:

root = Trie()

*Add a word, using:*

root.addWord(string)

*Generates all suffixes starting with this prefix (e.g. will print all words in trie if passed empty string)*

root.autocomplete(prefix)

*Can use 'in' operator to check if a word is in trie*

root.addWord('apple')
'apple in trie' returns True

**TODO:**
- Add support for deleting words.
- Run timed tests.
- Add support for other alphabets besides "normal" characters (e.g. bitwise tries, etc)
- Lexicographic sorting by character

Maybe, I will re-implement this as a compact prefix tree, or I will have it alongside it.
I will soon upload a less naive implementation, similar to a ternary search tree.




