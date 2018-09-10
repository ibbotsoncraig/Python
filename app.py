# libraries
import random
import time

# Declarations
dietop = [ '   ', 'O  ',  'O  ', 'O O', 'O O', 'O O']
diemid = [ ' O ', '   ',  ' O ', '   ', ' O ', 'O O']
diebot = [ '   ', '  O',  '  O', 'O O', 'O O', 'O O']
dashes_per_stage = ["________________________", "__________________", "____________", "__________", "________", "_______", "________", "__________", "____________", "__________________", "________________________"]
max_horses = 11
repeat = "Yes"
horse_victories = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#for i in range(1, 1000):
while repeat == "Yes":
	scratch1 = 0
	scratch2 = 0
	scratch3 = 0
	scratch4 = 0
	winner = "FALSE"
	finishline = [2, 4, 6, 7, 9, 10, 9, 7, 6, 4, 3]
	horse_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	prize=50*max_horses	
	print ("Drawing scratched horses....")
	scratch1 = random.randint(2,max_horses)
	while scratch2 == 0 or scratch2 == scratch1:
		scratch2 = random.randint(2,max_horses)
	while scratch3 == 0 or scratch3 == scratch1 or scratch3 == scratch2:
		scratch3 = random.randint(2,max_horses)
	while scratch4 == 0 or scratch4 == scratch1 or scratch4 == scratch2 or scratch4 == scratch3:
		scratch4 = random.randint(2,max_horses)
	time.sleep(3)
	print ("Scratched Horses:\t", scratch1, scratch2, scratch3, scratch4)

	# Roll the die
	while winner == "FALSE":
		time.sleep(1)
		print ("\n")	
		die1 = random.randint(0,5)
		die2 = random.randint(0,5)
		print ("+-----+\t\t+-----+")
		print ("|", dietop[die1], "|\t\t|", dietop[die2], "|")
		print ("|", diemid[die1], "|\t\t|", diemid[die2], "|")
		print ("|", diebot[die1], "|\t\t|", diebot[die2], "|")
		print ("+-----+\t\t+-----+")
		horse = die1 + die2
		if (horse+2) == scratch1 or (horse+2) == scratch2 or (horse+2) == scratch3 or (horse+2) == scratch4 :
			print ("SCRATCH DRAW!  Horse ", (horse+2), "owners put $50 in pot\t\t\t\t\tFINISH LINE!                 MINIMUM POT $", prize, "!")
#			print ("SCRATCH DRAW!  Horse ", (horse+2), "owners put $50 in pot")
			prize = prize+50
		else:
			horse_position[horse] += 1
			print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFINISH LINE!                 MINIMUM POT $", prize, "!")
		print ("                                                                      |")
		print ("                                                                      v")
		horse_number = 2
		for drawhorse in horse_position:
			dash_count = drawhorse
			print (horse_number, end="")
			if horse_number == scratch1 or (horse_number) == scratch2 or (horse_number) == scratch3 or (horse_number) == scratch4 :
				print (" SCRATCH")
			else:
				while dash_count > 0:
					print (dashes_per_stage[horse_number-2], end="")
					dash_count -= 1
				if horse_position[horse_number-2] == finishline[horse_number-2] and winner != "TRUE":
					winner = "TRUE"
					horse_victories[horse] += 1
					print ("**WINNER**", end="")
			horse_number += 1
			print ("\n")
#		if horse_position[horse] == finishline[horse]:
#			winner = "TRUE"

	
	print ("****** WE HAVE A WINNER*******")
	time.sleep(2)
	print ("Winning Horse:\t", horse+2, "Minimum Winnings: $", prize)
	print (horse_position, "\n\n")
	repeat = input("Play Again (Yes/No?)")

print (horse_victories)
