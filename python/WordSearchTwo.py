# Question No. 212
# Word Search Two
class TrieNode:
        def __init__(self, char):
            self.char = char
            self.isWord = False
            self.children = {}

        def addNode(self, char, node):
            self.children[char] = node

class Trie:

    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                child = TrieNode(c)
                cur.addNode(c, child)
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def eraseWord(self, ind, word, cur):
        if ind == len(word):
            cur.isWord = False
            if len(cur.children) == 0:
                return True
            return False
        
        canErase = self.eraseWord(ind+1, word, cur.children[word[ind]])
        if canErase:
            cur.children.pop(word[ind])
        
        return len(cur.children) == 0
            
        
    
class Solution:
    
    def getWords(self, x, y, cur, board, vis, word):
        
        if cur.isWord:
            w = "".join(word)
            self.wordsPresent.append(w)
            self.trieOb.eraseWord(0, word, self.trieOb.root)
            
        vis[x][y] = 1
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if nx >= 0 and nx < self.m and ny >= 0 and ny < self.n and vis[nx][ny] == 0:
                nxc = board[nx][ny]
                if nxc in cur.children:
                    word.append(nxc)
                    self.getWords(nx, ny, cur.children[nxc], board, vis, word)
                    word.pop()
        vis[x][y] = 0
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m, self.n = len(board), len(board[0])
        self.trieOb = Trie()
        for w in words:
            self.trieOb.insert(w)
        
        self.wordsPresent = []
        vis = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for x in range(self.m):
            for y in range(self.n):
                c = board[x][y]
                if c in self.trieOb.root.children:
                    self.getWords(x, y, self.trieOb.root.children[c], board, vis, [c])
        return self.wordsPresent