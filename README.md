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

root.add(string)

*Delete a word*

root.delete(word)

*Check if string is in trie*

root.add('apple')
'apple in trie' returns True

*Generates all suffixes starting with this prefix (e.g. will print all words in trie if passed empty string)*

root.autocomplete(prefix)

**TODO:**
- Add support for other alphabets besides "normal" characters (e.g. bitwise tries, etc)
- Lexicographic sorting by character

Maybe, I will re-implement this as a compact prefix tree, or I will have it alongside it.
I will soon upload a less naive implementation, similar to a ternary search tree.

**Perf details**
Data: 250K words found in /usr/share/dict/words - try it on your machine

Inserted all words at once, and checked for membership at once, and ran performance tests while doing it.

?:trie dliddell$ python test_trie.py 
* Max time to add word was 1.145418 sec, Max time to check if word in trie was 0.002709 sec
* Autocomplete time for prefix "pul" with 174 words was 0.000950 sec
* Autocomplete time for prefix "coc" with 218 words was 0.001251 sec
* Autocomplete time for prefix "kra" with 23 words was 0.000128 sec
* Autocomplete time for prefix "que" with 144 words was 0.000669 sec
* Autocomplete time for prefix "mon" with 817 words was 0.004332 sec
* Autocomplete time for prefix "fel" with 90 words was 0.000492 sec
* Autocomplete time for prefix "klo" with 6 words was 0.000045 sec
* Autocomplete time for prefix "lio" with 23 words was 0.000133 sec
* Autocomplete time for prefix "gir" with 49 words was 0.000212 sec
* Autocomplete time for prefix "abo" with 62 words was 0.000277 sec

On average, search times seems worse than ternary search tree. Maybe worst case is better than average case for one, but not the other.

