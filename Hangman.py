import random
answerlist = ["python","benton","computer","class","javascript","JMU","ISAT",]
random.shuffle(answerlist)
answer = list(answerlist[0])
display = []
display.extend(answer)
for i in range(len(display)):
	display[i] = "_"
print("The topic is: 252\n")
print (' '.join(display))
print ()
count = 0
while count < len(answer):
	guess = input("Please guess a letter: ")
	guess = guess.lower()
	print (count)
	for i in range(len(answer)):
		if answer[i] == guess :
			display[i] = guess
			count = count + 1

	print (' '.join(display))
	print ()

print ("You Guessed the Word!")