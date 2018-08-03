#!/usr/bin/python3.4
# this is used in working out who won a match
import random
import os
import mylog



#######################variables

#randomnumber=random.randint (1,10)
#randomnumber50=random.randint (1,10)
#randomnumber501=random.randint (1,10)

#randomnumber1=random.randint (1,10)
bigdiff=70
smalldif=20

#######################logic
## pass me the team value and i will do something clever
## lots of debugging to help catch crazy score lines and tweak logic
## Diffence  % Win Draw Lose
## 100         80  10   10
## 50          70  20   10
## 30          50  30   20
## else        30  40   30
## if result is draw use char+exp to see if we can force a result

######################Clever stuff


def bat(ourgk,oppgk,ourdef,oppdef,ourmid,oppmid,ourata,oppata,ourchar,oppchar,ourexp,oppexp):

# create scores
	ourdefscore=0	
	ourattackscore=0	
	oppdefscore=0	
	ourattackscore=0	
	oppattackscore=0	

	randomnumber=random.randint (1,10)
	randomnumber50=random.randint (1,10)
	randomnumber501=random.randint (1,10)
	randomnumber1=random.randint (1,10)
	
	
#	print ("rn=",randomnumber)
#	print ("rn50=",randomnumber50)
#	print ("rn501=",randomnumber501)


	ourattackscore=int(((ourdef*4)+(ourmid*8)+(ourata*6)+(ourexp/7)+(ourchar/4))/4.5)
	oppattackscore=int(((oppdef*4)+(oppmid*8)+(oppata*6)+(oppexp/7)+(oppchar/4))/4.5)
	ourdefscore=int(((ourgk*4)+(ourdef*8)+(ourmid*4)+(ourata*2)+(ourexp/7)+(ourchar/4))/4.5)
	oppdefscore=int(((oppgk*4)+(oppdef*8)+(oppmid*4)+(oppata*2)+(oppexp/7)+(oppchar/4))/4.5)
 
	print ("Our Def Team score",ourdefscore)
	print ("Our Ata Team score",ourattackscore)
	print ("The Def Opposition Team score",oppdefscore)
	print ("The Ata Opposition Team score",oppattackscore)
	print ("Lets go play a game")

# our goals tally
	ourcomaprescore=0
	ourgoals=0
	ourcomparescore=int(ourattackscore-oppdefscore)
	if ourcomparescore > 50:
		if randomnumber1 < 2:
			ourgoals=("5")
		elif randomnumber1 < 4:
			ourgoals=("4")
		elif randomnumber1 <= 6:
			ourgoals=("3")
		elif randomnumber1 <= 8:
			ourgoals=("2")
		else:
			if randomnumber >5:
				ourgoals=("1")
			else:
				ourgoals=("0")



	elif ourcomparescore > 25:

		if randomnumber1 <= 7:
			ourgoals=("3")
		elif randomnumber1 < 10:
			ourgoals=("2")
		else:
			if randomnumber >5:
				ourgoals=("1")
			else:
				ourgoals=("0")


	elif ourcomparescore > 10:

		if randomnumber1 <= 4:
			ourgoals=("3")
		elif randomnumber1 < 8:
			ourgoals=("2")
		else:
			if randomnumber >5:
				ourgoals=("1")
			else:
				ourgoals=("0")

	else:

		if randomnumber50 <= 1:
			ourgoals=("3")
		elif randomnumber50 <= 4:
			ourgoals=("2")
		elif randomnumber50 <= 7:
			ourgoals=("1")
		else:
			ourgoals=("0")


	

# opposition goals tally
	oppcomaprescore=0
	oppgoals=0
	oppcomparescore=int(oppattackscore-ourdefscore)
	if oppcomparescore > 50:
		if randomnumber < 2:
			oppgoals=("5")
		elif randomnumber < 4:
			oppgoals=("4")
		elif randomnumber <= 6:
			oppgoals=("3")
		elif randomnumber <= 8:
			oppgoals=("2")
		else:
			if randomnumber50 > 5:
				ourgoals=("1")
			else:
				ourgoals=("0")

	elif oppcomparescore > 25:
		if randomnumber <= 7:
			oppgoals=("3")
		elif randomnumber < 10:
			oppgoals=("2")
		else:
			if randomnumber50 > 5:
				ourgoals=("1")
			else:
				ourgoals=("0")

	elif oppcomparescore > 10:
		if randomnumber <= 4:
			oppgoals=("3")
		elif randomnumber < 8:
			oppgoals=("2")
		else:
			if randomnumber50 > 5:
				ourgoals=("1")
			else:
				ourgoals=("0")

	else:
		if randomnumber501 <= 1:
			oppgoals=("3")
		elif randomnumber501 <= 4:
			oppgoals=("2")
		elif randomnumber501 <= 7:
			oppgoals=("1")
		else:
			oppgoals=("0")
	return ourgoals,oppgoals


