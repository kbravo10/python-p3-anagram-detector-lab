# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        anagram_list = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                anagram_list.append(word)
        
        return anagram_list