# Question No. 208
# Implement Trie
 
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
 
class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        return ord(ch)-ord('a')
 
 
    def insert(self,word):
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
    def search(self, word):
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl.isEndOfWord

    def startsWith(self, prefix):
         
        pCrawl = self.root
        length = len(prefix)
        for level in range(length):
            index = self._charToIndex(prefix[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return True
 
# driver function
def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
if __name__ == '__main__':
    main()