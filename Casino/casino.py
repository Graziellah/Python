#-*-coding:utf-8-*

import os
from random import randrange
from math import ceil
def set_num():
	num = input("Sassissez un numéro entre 0 et 50: ")
	try:
		num = int(num)
		assert num < 50 and num >= 0
	except ValueError:
		print("la valeur saisi n'est pas correcte")
		set_num()
	except AssertionError:
		print('Le numero saisi n\' est pas compris entre 0 et 50')
		set_num()
	return(num)
def set_mise():
	mise = input("Quelle est votre mise ? ")
	try:
		mise = int(mise)
		assert mise >= 0
	except ValueError:
		print("la valeur saisi n'est pas correcte")
		set_mise()
	except AssertionError:
		print("Vous avez saisi une mise negative")
		set_mise()
	return (mise)
def game(win, num):
	if (win == num):
		return 0
	if win % 2 == 0 and num % 2 == 0:
		return 1
	if win % 2 != 0 and num % 2 != 0:
		return 1
	return(2)
def game(win, num):
	if win == num:
		return 0
	if win % 2 == 0 and num % 2 == 0:
		return 1
	if win % 2 != 0 and num % 2 != 0:
		return 1
	else:
		return 2

def play_again():
	rep = input("Souhaitez-vous continuer? Y or N: ")
	try:
		rep = str(rep)
		assert rep == "Y" or rep == "N"
	except AssertionError:
			play_again()
	if rep == "N":
		return 0
	return 1

if __name__ == "__main__":
	play = 1
	cagnotte = 100
	print("Bonjour bienvenu à la roulette, pour votre première participation nous vous offrons", cagnotte, "$")
	while play == 1:
		num = set_num()
		mise = set_mise()
		win = randrange(50)
		print ("valeur du numero gagnant: ", win)
		result = game(win, num)
		print (result)
		if result == 0:
			cagnotte = cagnotte + mise * 3
			print("Felication vous avez gagné", mise * 3, "votre cagnotte s\'élève à ", cagnotte, "$")
		elif result == 1:	
			cagnotte = cagnotte + mise / 2
			print("Bravo vous remportez la moitié de votre mise votre cagnotte s\'élève à ", cagnotte, "$")
		else:
			cagnotte = cagnotte - mise
			print("Dommage vous avez perdu votre cagnotte est maintenant de ", cagnotte, "$")
		play = play_again()
	print("Merci pour votre participation, Au revoir")

os.system("pause")