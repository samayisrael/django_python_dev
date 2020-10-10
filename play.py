class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr_node = self.root
        for i, val in enumerate(word):
            if val not in curr_node.children:
                curr_node.children[val] = TrieNode()
            curr_node = curr_node.children[val]
        curr_node.end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, i):
            if i == len(word): return node.end

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False

        return dfs(self.root, 0)


from var_dump import var_dump

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')


var_dump(obj)
# param_2 = obj.search(word)
