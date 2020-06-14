MIN = 3;
AY = 'ay';
AB = 'ab';
VOWELS = ['a', 'e', 'i', 'o', 'u']

# Input function

# This function requests a string from the user 
# and converts it to a list to be able to see how many words were entered.
def getString():
	word = input('Enter a string with 3 words minimum: ')

	# Validate minimum of three words
	while (len(word.split())<MIN):
		print('The string must have at least 3 words in it.')
		word = input('Enter a string with 3 words minimum: ')

	# Create Target List
	global targetList 
	targetList = word.split()
	
	# Return targetList to main
	return targetList 

# This function display a new string that has moved the first letter 
# to the end and added "ay" to each word in the targetList. 
def pigLatin(targetList):
	for word in targetList:
		w=word.lower()
		print (w[1:]+w[0]+AY)

# This function returns inputs in a new string that 
# has "ab" added before each vowel in each word.
def turkeyIrish(targetList):
	turkeyWord = '';
	global joinList
	joinList = "\n".join(targetList)
	
	for word in joinList:
		w=word.lower()
		for i in range(len(w)):
			if w[i] in VOWELS:
				turkeyWord+=AB+w[i]
			else:
				turkeyWord+=w[i]
	return turkeyWord
		

# This function counts the vowels in input        
def countVowels(joinList):
	count = 0
	for i in range(len(joinList)):
		if joinList[i] in VOWELS:
			count+=1
	return count

# Processing functions
def main():
	print('NEW WORD GENERATOR')
	getString()

	# Display Pig Latin
	print('\nWords made into Pig Latin:')
	pigLatin(targetList)
	print('\nWords made into Turkey Irish:')
	print(turkeyIrish(targetList))
	print('\n# of vowels in the words:', countVowels(joinList))

main()
