fruit = 'apple'

def backwards(word):
	index = 1
	while index <= len(word):
		letter = word[-index]
		print letter
		index = index + 1
	
# backwards(fruit)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

def ex2(pre,suf):
	for letter in pre:
		if letter in ('O', 'Q'):
			print letter + 'u' + suf
		else:
			print letter + suf
		
# ex2(prefixes, suffix)

fruit = 'banana'
# print fruit[:]

word = 'banana  '
new_word = word.strip()
#print new_word


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter
            
in_both('michael', 'sarah')