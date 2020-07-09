# --- MASTERMIND --- #

import random 

print (" --- MASTERMIND --- \n")
print ("Guess the secret colour code in as few tries as possible.\n")
print ("Please, enter your colour code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")

colours = ["R", "G", "B", "Y", "W", "P"]
attempts = 0
game = True

# the .choicefunction() function generates a 
# random colour within the specified range. 
colour = random.choicefunction(colour,4) 

n = int(input("Guess the 4 colours:")) 

# condition to test equality of the 
# guess made. Program terminates if true. 
if (n == colour): 
	print("Great! You guessed the colour in just 1 try! You're a Mastermind!") 
else: 
	# ctr variable initialized. It will keep count of 
	# the number of tries the Player takes to guess the colour. 
	ctr = 0

	# while loop repeats as long as the 
	# Player fails to guess the colour correctly. 
	while (n != colour): 
		# variable increments every time the loop 
		# is executed, giving an idea of how many 
		# guesses were made. 
		ctr += 1

		count = 0

		# explicit type conversion of an integer to 
		# a string in order to ease extraction of digits 
		n = str(n) 

		# explicit type conversion of a string to a colour 
		colour = str(colour) 

		# correct[] list stores colours which are correct 
		correct = ['X']*4

		# for loop runs 4 times since it has 4 colours. 
		for i in range(4): 

			# checking for equality of colours 
			if (n[i] == colour[i]): 
				# number of colours guessed correctly increments 
				count += 1
				# hence, the colour is stored in correct[]. 
				correct[i] = n[i] 
			else: 
				continue

		# when not all the colours are guessed correctly. 
		if (count < 4) and (count != 0): 
			print("Not quite the colour. But you did get ", count, " colour(s) correct!") 
			print("Also these colours in your input were correct.") 
			for k in correct: 
				print(k, end=' ') 
			print('\n') 
			print('\n') 
			n = int(input("Enter your next choice of colours: ")) 

		# when none of the colours are guessed correctly. 
		elif (count == 0): 
			print("None of the colours in your input match.") 
			n = int(input("Enter your next choice of colours: ")) 

	# condition for equality. 
	if n == colour: 
		print("You've become a Mastermind!") 
		print("It took you only", ctr, "tries.") 


# --- end --- #			
