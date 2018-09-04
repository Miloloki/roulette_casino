# -*-coding:UTF-8 -*

import os
from random import randrange
from math import ceil 

monnaie = 1000
continuer=True

print("Vous commencer la partie avec", monnaie,"€")


while continuer:

#Partie sur le nombre de la roulette
	nbr=-1
	while nbr<1 or nbr>50:
		nbr=input("Entrez un nombre de la roulette entre 1 et 50 :  ")
		try:
			nbr=int(nbr)
		except ValueError:
			print("Ceci n'est pas un nombre de la roulette")
			nbr= -1
			continue
		if nbr < 1:
			print("Votre nombre est négatif")
		if nbr > 50:
			print("Votre nombre est supérieur à 50")


#Partie sur la mise du nombre
	mise=0
	while mise<=0 or mise>monnaie:
		mise=input("Entrez votre mise :  ")
		try:
			mise=float(mise)
		except ValueError:
			print("Vous avez rentré un nombre invalide")
			mise = -1
			continue
		if mise<=0:
			print("Votre montant est négatif")
		if mise > monnaie:
			print("Vous n'avez pas assez d'argent")

#Nombre aléatoire
	alt=randrange(50)
	print("La roulette a sorti ce numéro :  ")


#Gain ou non
	if alt==nbr:
		print("Vous avez gagner, votre mise est de :  ", mise*3, "€")
		monnaie += mise*3

	elif alt%2 == nbr%2:
		mise=mise*0.5
		print("Vous obtenez 50pour cent votre mise soit :  ", mise,"€")
		monnaie += mise

	else:
		print("Vous avez perdu")
		monnaie -= mise


#Si plus d'argent
	if mise<=0:
		print("Vous ne pouvez plus jouer")
		continuer=False
	else:
		print("Il vous reste", monnaie ,"€")
		quitter = input("Souhaitez-vous quitter le casino (o/n)")
		if quitter == "o":
			print ("Vous avez quitter le casino avec", monnaie,"€")
			continuer = False
		


os.system("pause")
