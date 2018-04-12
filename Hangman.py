import random
possibleAnswers = [ "python", "benton", "computer", "class", "javascript", "JMU", "ISAT", ]
random.suffle(possibleAnswers)
answer = list(possibleAnswers[1])
display = []
display.extend(answer)
for i in range(len(display)):
	display[i] = "_"
print("The topic is: 252\n")
print ' '.join(display)
print "\n\n\n\n"

count = 0
while count < len(answer):
		guess = raw_input("Please guess a letter: ")
		
		guess = guess.upper()

		for i in range(len(answer)):
			if answer[i] == guess:
				display[i] = guess
				count += 1

		print ' '.join(display)
		print "\n\n\n"

print "You Guessed It!!"