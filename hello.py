pyg = 'ay'
original = raw_input('enter a word: ')
word = original.lower()
newWord = word[1:len(word)]
first = word[0]
pygLatin = newWord+first+pyg
print str(pygLatin)
