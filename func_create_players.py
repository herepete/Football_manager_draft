#!/usr/bin/python3.4
# this script will create a random name combining first and last names when called
# this is used in inital team creation and draft
import random
import os
#import numpy

#os.system('rm create_players.log')

#num # removed
#gk = num of gk to create
#def = num of def to create
#mid = number of midfielders to create
#ata = number of attackers to create
#exp = max experience (in draft/free agency we might allow more experience players)
#maxskill = max skill
#skill = current skill
#skillpeak = max skill peak in age (not sure what to do with this yet)
#char = max Characteur of player
#maxage= player can at most be this old
#weighted=1 yes 0 no

#######################variables
#minskill=1
#maxrskill=15
minrchar=0
#minage=17
minexp=0
choices = []

#######################logic
## pass me your variables and i will create you some players
## so create 2 gk with maxskill =20 skill =18 skillpeak=17,maxage=18 you would pass 
## func_create_players.rn3(gk =2, defe =0, mid =0, ata =0, exp =0, maxskill =20, skill =18, skillpeak =17, char =0, maxage=18)
## anything with a value of 0 will create an output value of 0
## designed to hopefully allow for inital start up players, draft players and Free agency
## the format command below just adds some nice extra space to each line to make the output nicer


######################Clever stuff

def betterexp (rage):
	
	rexp=int(rage)-17
	if rexp <= 2:
		rexp=random.randint (0,rexp)
	elif rexp >14:
		mirexp=10
		rexp=15
		rexp=random.randint (mirexp,rexp)	
	else:
#		mirexp=int(rexp)-3
		mirexp=3
#		marexp=int(rexp)
		marexp=int(rexp)

		rexp=random.randint (mirexp,marexp)

	return rexp

def rn3(gk,defe,mid,ata,exp,maxskill,skill,skillpeak,char,maxage,minskill,weighted,minage,minrchar):

	first_names=('Wayne','Alan','David','Stuart','Luke ','Choper','Alfa  ','Joe','Mike','Steven','Tim','Jim','Dana','Jake','Ben','Davo','Nick','Rambo','Seb','Danny','Josh','Evan','Caleb','Sven','Tank','Austin','Seth','Matt','Jeremy','Darran','Myles','Lenny','Chris','Drew','Donald','Jamar','Baker','Payton','Antonio','Dylan','Charlie','Samuel','Gareth','Liam','Lucas','Jose','Mateo','Noel','Adam','Jonas','Elias','Marko','Johnny','Harry','Bobby','Logan','Phil','Vincent','Randy','Russel','Gabriel','Louis','Eugene','Ralph','Jordan','Noah','Bruce','Ethan','Keith','Jan','Cameron','Ahmed','Hamada','Jens','Junior','Omar','Manish','Jude','Thiago','Alexis','Elijah','Javier','Ari','Rawiri','Lukas','Riccardo','Hans','Leon','Vicktor','Tommaso','Goran','Zoran','Flyn','Emil','Davit','Minik', 'Carlos','Damion','Denzel','Mychal','Genard','Brogan','Derron','Britton','Ross','Derrick','Zay','Tom','Merlin','Milan','Melin','Ace','Martin','Martyn','Marvin','Harper','Jace','Corvert','Glenn','Dai','Travis','Tomas','Ayat','Duncan','Seren','Hassan','Dillan','Ada','Kiran','Franky','Mitchel','Shay','Ray','Jenson','Miguel','Paisley','Antoni','Hugo','Arlo','Dexter','Callam','DJ')


	last_names=('Rooney','Smith','Beckam','Broad ','Jones','Ford','Stansf','Abacus','Plato','Shaw','Robert','Sping ','Taylor','Lee ','Wilson','Bailey','Hoss','Gavate','Green ','Oneil ','Thomon','Avery','Chubb','Mayfield','Ward','Thomas','Scott','Salako','Reiter','Nassib','Njoku','Ratley','Schobert','Kindred','Johnson','Dayes','Ekuale','Fells','Garrett','Rogers','Price','Bell','Gibson','Mills','Booth','Dixon','Lane','Harper','Walker','Watson','Jackson','Davis','Cox','Fox','Ali','Hart','Whiteman','Frazer','Clarke','Clark','Webb','Kelley','James','Barnes','Gill','Hudson','Cook','Allen','Poole','Lawson','Stewart','Read','Reid','Powell','Barker','Dawson','Cann','Brooks','Ellis','Khan','Carter','Patel','Adams','Potter','Bishop','Field','Payne','Bolton','Hardy','Parry','Marsh','Burns','French','Park','Forrest','Banks','Lynch','Sharp','Bates','Riley','Atkins','Love','Hawkins','Duncan','Byrne','Pritchard','Simmons','Perry','Fabino','Orchard','Vogel','Rice','Berry','Cajuste','Tretter','Robinson','Bello','Currie','Grace','Gay','Stanton','Janis','Sankoh','Caldwell','Hubbard','Graham','Wagner','Stanley','Cunningham','Kennedy','Lee','Holt','Lowe','Ozel','Swenney','Weaver','Whyte','Black','Shelton','Olsen','Ortiz','Howarth','Pasons','Major','Corben','Bird','Santos','Whitehouse','Mccoy','Meyer','Laing','Blair','Bauer','Baver','Garze','Last')

	choices = []
	nskill=skill+1
	choices=list(range(minskill,nskill))


	players = []
	for i in range(gk):
		#add a weighing to random numbers to stop clustering of skills
		weights = [0.03, 0.03,0.03, 0.07,0.07, 0.07,0.07, 0.07,0.06, 0.06,0.06, 0.06,0.06, 0.06,0.06, 0.04,0.04, 0.03,0.02, 0.01]
		#if weighted == 0:
		rskill = "{:<2}".format(random.randint  (minskill,skill))
		#else:
#			rskill  = "{:<2}".format(numpy.random.choice(choices, p=weights))
		# turning into number
		rskilln=int(rskill)
		# creating players skills the format adds some space to help the output look nicer but it does turn it from num to char
		rmaxskill= "{:<2}".format(random.randint (rskilln,maxskill))
		rchar = "{:<2}".format(random.randint  (minrchar,char))
		
		rage=random.randint (minage,maxage)
		rmaxage ="{:<2}".format(rage)
		
		rexp = betterexp(rage)
		rexp = "{:<2}".format(rexp)

		playersfname = "{:<8}".format(random.choice(first_names))
		playerssname = "{:<10}".format(random.choice(last_names))
		players.append (["GK  ",playersfname,playerssname,rskill,rmaxskill,rchar,rexp,rmaxage])
	for i in range(defe):
		#add a weighing to random numbers to stop clustering of skills
		weights = [0.03, 0.03,0.03, 0.07,0.07, 0.07,0.07, 0.07,0.06, 0.06,0.06, 0.06,0.06, 0.06,0.06, 0.04,0.04, 0.03,0.02, 0.01]
		rskill = "{:<2}".format(random.randint  (minskill,skill))
                # turning into number
		rskilln=int(rskill)
                # creating players skills the format adds some space to help the output look nicer but it does turn it from num to char
		rmaxskill= "{:<2}".format(random.randint (rskilln,maxskill))
		rchar = "{:<2}".format(random.randint  (minrchar,char))


		rage=random.randint (minage,maxage)
		rmaxage ="{:<2}".format(rage)
		
		rexp = betterexp(rage)
		rexp = "{:<2}".format(rexp)

		rmaxage ="{:<2}".format(random.randint (minage,maxage))
		playersfname = "{:<8}".format(random.choice(first_names))
		playerssname = "{:<10}".format(random.choice(last_names))
		players.append (["DEF ",playersfname,playerssname,rskill,rmaxskill,rchar,rexp,rmaxage])
	for i in range(mid):
		#add a weighing to random numbers to stop clustering of skills
		weights = [0.03, 0.03,0.03, 0.07,0.07, 0.07,0.07, 0.07,0.06, 0.06,0.06, 0.06,0.06, 0.06,0.06, 0.04,0.04, 0.03,0.02, 0.01]
		rskill = "{:<2}".format(random.randint  (minskill,skill))
                # turning into number
		rskilln=int(rskill)
                # creating players skills the format adds some space to help the output look nicer but it does turn it from num to char
		rmaxskill= "{:<2}".format(random.randint (rskilln,maxskill))
		rchar = "{:<2}".format(random.randint  (minrchar,char))

		rage=random.randint (minage,maxage)
		rmaxage ="{:<2}".format(rage)

		rexp = betterexp(rage)
		rexp = "{:<2}".format(rexp)


		playersfname = "{:<8}".format(random.choice(first_names))
		playerssname = "{:<10}".format(random.choice(last_names))
		players.append (["MID ",playersfname,playerssname,rskill,rmaxskill,rchar,rexp,rmaxage])
	for i in range(ata):
		#add a weighing to random numbers to stop clustering of skills
		weights = [0.03,0.03, 0.03,0.05, 0.05,0.06, 0.07,0.08, 0.08,0.08, 0.07,0.07, 0.07,0.06, 0.05,0.04, 0.03,0.02, 0.02, 0.01]
		#if weighted == 0:
		rskill = "{:<2}".format(random.randint  (minskill,skill))
		# turning into number
		rskilln=int(rskill)
		# creating players skills the format adds some space to help the output look nicer but it does turn it from num to char
		rmaxskill= "{:<2}".format(random.randint (rskilln,maxskill))
		rchar = "{:<2}".format(random.randint  (minrchar,char))

		rage=random.randint (minage,maxage)
		rmaxage ="{:<2}".format(rage)

		rexp = betterexp(rage)
		rexp = "{:<2}".format(rexp)


		playersfname = "{:<8}".format(random.choice(first_names))
		playerssname = "{:<10}".format(random.choice(last_names))
		players.append (["ATA ",playersfname,playerssname,rskill,rmaxskill,rchar,rexp,rmaxage])
	return players
