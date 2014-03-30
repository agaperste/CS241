# Trie
# comes from the root ReTRIEval

class Node ():
    
    def __init__ (self, letter):
        self.count = 0
        self.letter = letter
        self.children = [None] * 26
        self.isWord = False 

class AutoComplete (object):
    def __init__ (self):
        self.head = Node (" ")
        
    def insert (self, word):
        if not word.isalpha:
            return 
        curnode = self.head
        for letter in word:  #convert the letter into an index in the node
            index = ord (letter.lower()) - 97  #ord("a") = 97, it serves as the offset
            c = curnode.children [index]
            if c == None:
                n = None (letter)
                curnode.children[index, n]
            curnode.count += 1
            curnode = c 
            # at the end of the prefix chain
        curnode.isWord = True
    
    def find (self, prefix):
        curnode = self.head
        for letter in prefix:
            index = ord(letter.lower()) - 97
            c = curnode.children[index]
            if not c:
                return None
            curnode = c
                
        '''for dictword in dictionary:
            if len (word) <= len (dictowrd):
                for letter in dictword:
                    for  '''
                    
if __name__ == "main":    
    a = AutoComplete ()
    words = open ("wordEn.txt", "r")
    for word in words:
        a.insert(word)
    posswords = a.find("abandon")
    print "Possible completions are: "
    for word in possword:
        print word 
        
        

                