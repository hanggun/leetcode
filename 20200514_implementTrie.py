# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, s):
        self.endsHere = False
        self.val = s
        self.child = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TreeNode(None)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        parent = self.root
        for char in word:
            if char not in parent.child:
                parent.child[char] = TreeNode(char)
            parent = parent.child[char]

        parent.endsHere = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent = self.root
        for i in word:
            if i not in parent.child:
                return False
            parent = parent.child[i]
            
        return parent.endsHere

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent = self.root
        for i in prefix:
            if i not in parent.child:
                return False
            parent = parent.child[i]
            
        return True
        
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))