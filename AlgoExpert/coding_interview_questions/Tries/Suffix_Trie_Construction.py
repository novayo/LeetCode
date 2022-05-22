'''
main idea: trie
time comp: O(n^2)
space comp: O(n^2)
- where n is the length of the input string
'''

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
			root = self.root
			for s in string[i:]:
				if s not in root:
					root[s] = {}
				root = root[s]
			root[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        root = self.root
		for s in string:
			if s not in root:
				return False
			root = root[s]
		return self.endSymbol in root
