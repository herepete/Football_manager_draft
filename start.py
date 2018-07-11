#!/usr/bin/python3.4
# this is a combo of my 2 favourite sports NFL and  Football (Soccer)
# you will have 11 players and a squad of x -Football
# you will be in a division of 4 and have playoffs and a superbowl - Nfl
# you will have a draft to improve your team -Nfl

################ Imports and System Bits
import os
import random
import func_create_players
import func_gameday
import func_teamratings
import func_endofseason
import func_oppteamscore

os.system('clear')
##################################################### Functions

#######  get team report 


def teamreport1(createteam,printto):
	os.system('clear')
	reportneeded=input("Press enter button to continue or r for team report or t for squad...\n")
	os.system('clear')
	if reportneeded=="r":
		teamscore=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=createteam, printo="yp")
		input("Press enter button to continue...\n")
	if reportneeded=="t":
		print ("\nYour team\n")
		print ("P    Name                S  MS C  E  A")
		for i in range(len(createteam)):
			for j in range(len(createteam[i])):
				print(createteam[i][j], end=' ')
			print()
		print ("")
		print ( "Key")
		print ("========")
		print ("P=Position")
		print ("S=Skill")
		print ("MS=Max Skill")
		print ("C=Character")
		print ("E=Experience")
		print ("A=Age")
		print ("")
		input("Press enter button to continue...\n")





######### function Draft

def draft(myteam,draft,typeofdraft):
	### print Draft team
	os.system('clear')
	reportneeded=input("Press enter button to continue or r for team report or t for squad...\n")
	os.system('clear')
	if reportneeded=="r":
		teamscore=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=myteam, printo="yp")
		input("Press enter button to continue...\n")
	if reportneeded=="t":
		print ("\nYour team\n")
		print ("P    Name                S  MS C  E  A")
		for i in range(len(createteam)):
			for j in range(len(createteam[i])):
				print(createteam[i][j], end=' ')
			print()
		print ("")
		print ( "Key")
		print ("========")
		print ("P=Position")
		print ("S=Skill")
		print ("MS=Max Skill")
		print ("C=Character")
		print ("E=Experience")
		print ("A=Age")
		print ("")
		input("Press enter button to continue...\n")


	
#	print ()
	 
	positioninteam=0
	os.system('clear')
	print ("Avaliable players in the {} of the Draft\n" .format(typeofdraft))
	print ("P    Name                S  MS C  E  A  N")
	for i in range(len(draft)):
		positioninteam=positioninteam+1
		#print (positioninteam, end=' ')
		#print (" ", end= ' ')
		for j in range(len(draft[i])):
			print(draft[i][j], end=' ')
		print (positioninteam, end=' ')
		print()


	### print your team
	numofplayerscreated=(len(myteam))
	numofplayerscreatedwithspace=str(numofplayerscreated) + " "
	#print ("nopc=",numofplayerscreated)
	print ("\nYour team\n")
	print ("P    Name                S  MS C  E  A")
	for i in range(len(myteam)):
		for j in range(len(myteam[i])):
                	print(myteam[i][j], end=' ')
		print()

	print ("")
	print ( "Key")
	print ("========")
	print ("N=Players number in the draft (this is not sorted)")
	print ("P=Position")
	print ("S=Skill")
	print ("MS=Max Skill")
	print ("C=Character")
	print ("E=Experience")
	print ("A=Age")
	print ("")

#############
	### Error check users input is a number

	while True:
        	#print ("Who do you select in the {} of the draft?" .format(typeofdraft)
		select1=input("Who do you want to select in the {} of the draft? Avaliable options are 1-{} ... or Press e to not select anyone and exit this round of the draft ... \n" .format(typeofdraft,positioninteam))
	        # select1number = try and convert it into a number i.e is a number
		if select1 =="e":
			break
		if select1.isnumeric() and int(select1) < numofplayerscreated and int(select1) <= positioninteam :
			break
		print ("Invalid option try again...\n")

	#### formatting data
	if select1 != "e":
		select1=int(select1)
		select1=select1-1
		nameofselect1=draft[select1]


		a2 = draft[select1]
		a2p = a2[:1]
		positioninteam=-1
		positioninteam1=-1
		z=0
	
		os.system('clear')
		# get person drafted
		print ("You have Chosen...\n")

		print ("P    Name                S  MS C  E  A")

		for i in range(len(draft)):
			positioninteam1=positioninteam1+1
			for j in range(len(draft[i])):
				if select1 == positioninteam1:
					print(draft[i][j], end=' ')
			#del draft[i]
					z=1
				else:
					z=0
			if z == 1:
        	        	print ()



	##############who to replace

		print ("\nThis are the people in the team who can be replaced, who do you want to remove? :")


		incrementalnumber=0
		z=0
		rangeofpaval=[]
		print ()
		print ("P    Name                S  MS C  E  A  N")
		for i1 in range(len(myteam)):
        		incrementalnumber=incrementalnumber+1
	        	for j1 in range(len(myteam[i1])):
        	        	playerposinteam=myteam[i1][0]
	                	if playerposinteam in a2p:
        	                	print(myteam[i1][j1], end=' ')
	        	                z=1
        	        	else:
                	        	z=0
		        if z == 1:
        		        print (incrementalnumber, end=' ')
                		print ()
	                	rangeofpaval.append (incrementalnumber)
		print ("")
		print ( "Key")
		print ("========")
		print ("N=Players number in the draft (this is not sorted)")
		print ("P=Position")
		print ("S=Skill")
		print ("MS=Max Skill")
		print ("C=Character")
		print ("E=Experience")
		print ("A=Age")
		print ("")


	###############
		buildrange=""
		buildrangel=[]
		for x in range (len(rangeofpaval)):
        		#string version
	        	buildrange = buildrange + str(rangeofpaval[x]) + " "
		        #list version
        		buildrangel.append(rangeofpaval[x])

		minrange=int(min(buildrangel))
		maxrange=int(max(buildrangel))

		while True:
        		select1replace=input("\nAvaliable options are {}...\n" .format(buildrange))
	        	#if select1replace.isnumeric and int(minrange) <= int(select1replace) <= int(maxrange):
	        	if select1replace.isnumeric() and int(minrange) <= int(select1replace) <= int(maxrange):
        	        	break
	        	print ("Invalid option please try again")
		numinsquad=len(createteam)
		select1replace=int(select1replace)
		select1replace=select1replace - 1

		a2 = draft[select1]
		del createteam[select1replace]
		del draft[select1]
		draftreturned = draft
		numinsquad=len(createteam)
		createteam.insert(select1replace, (a2))

		return createteam,draftreturned
	else:
		draftreturned=createteam,
		return createteam,draftreturned


#######function opposition team
def oppteamscores(ng):
	
#Opposition scores


	if ng == 1:
		ogk=random.randint (5,20)
		odef=random.randint (5,15)
		omid=random.randint (5,15)
		oata=random.randint (5,15)
		ochar=random.randint (50,150)
		oexp=random.randint (50,150)
	if ng == 2:
		ogk=random.randint (5,15)
		odef=random.randint (5,20)
		omid=random.randint (5,15)
		oata=random.randint (5,15)
		ochar=random.randint (50,150)
		oexp=random.randint (50,150)
	if ng == 3:
		ogk=random.randint (5,15)
		odef=random.randint (5,15)
		omid=random.randint (5,20)
		oata=random.randint (5,15)
		ochar=random.randint (50,150)
		oexp=random.randint (50,150)
	if ng == 4:
		ogk=random.randint (5,15)
		odef=random.randint (5,15)
		omid=random.randint (5,15)
		oata=random.randint (5,20)
		ochar=random.randint (50,150)
		oexp=random.randint (50,150)
	if ng == 5:
		ogk=random.randint (5,15)
		odef=random.randint (5,15)
		omid=random.randint (5,15)
		oata=random.randint (5,15)
		ochar=random.randint (50,200)
		oexp=random.randint (50,200)
	if ng == 6:
		ogk=random.randint (10,15)
		odef=random.randint (10,15)
		omid=random.randint (10,15)
		oata=random.randint (10,15)
		ochar=random.randint (100,150)
		oexp=random.randint (100,150)
	if ng == 7:
		ogk=random.randint (10,15)
		odef=random.randint (10,15)
		omid=random.randint (10,15)
		oata=random.randint (10,15)
		ochar=random.randint (100,150)
		oexp=random.randint (100,150)
	if ng == 8:
		ogk=random.randint (10,15)
		odef=random.randint (10,15)
		omid=random.randint (10,15)
		oata=random.randint (10,15)
		ochar=random.randint (100,150)
		oexp=random.randint (100,150)
	if ng == 9:
		ogk=random.randint (10,15)
		odef=random.randint (10,15)
		omid=random.randint (10,15)
		oata=random.randint (10,15)
		ochar=random.randint (100,150)
		oexp=random.randint (100,150)
	if ng == 10:
		ogk=random.randint (13,18)
		odef=random.randint (13,18)
		omid=random.randint (13,18)
		oata=random.randint (13,18)
		ochar=random.randint (125,200)
		oexp=random.randint (125,200)
	if ng == 11:
		ogk=random.randint (13,18)
		odef=random.randint (13,18)
		omid=random.randint (13,18)
		oata=random.randint (13,18)
		ochar=random.randint (125,200)
		oexp=random.randint (125,200)
	if ng == 12:
		ogk=random.randint (13,18)
		odef=random.randint (13,18)
		omid=random.randint (13,18)
		oata=random.randint (13,18)
		ochar=random.randint (125,200)
		oexp=random.randint (125,200)
	if ng == 13:
		ogk=random.randint (15,20)
		odef=random.randint (15,20)
		omid=random.randint (15,20)
		oata=random.randint (15,20)
		ochar=random.randint (150,200)
		oexp=random.randint (150,200)
	if ng == 13:
		ogk=random.randint (15,20)
		odef=random.randint (15,20)
		omid=random.randint (15,20)
		oata=random.randint (15,20)
		ochar=random.randint (100,200)
		oexp=random.randint (100,200)
	if ng == 14:
		ogk=random.randint (15,20)
		odef=random.randint (15,20)
		omid=random.randint (15,20)
		oata=random.randint (15,20)
		ochar=random.randint (100,150)
		oexp=random.randint (125,150)
	if ng == 15:
		ogk=random.randint (16,19)
		odef=random.randint (16,20)
		omid=random.randint (16,19)
		oata=random.randint (16,20)
		ochar=random.randint (123,150)
		oexp=random.randint (150,200)
	if ng == 16:
		ogk=random.randint (15,20)
		odef=random.randint (15,20)
		omid=random.randint (15,20)
		oata=random.randint (15,20)
		ochar=random.randint (175,200)
		oexp=random.randint (175,200)
	return ogk,odef,omid,oata,ochar,oexp



################################################################################ start of program
# for season stats
win = 0
draw = 0
lost = 0
for1 = 0
against = 0
points = 0
goald =0
season = "W   D   L   F   A   P   GD\n"

############## Intro

print ("""Welcome to Football Manager Draft
===============
This game is a mashup of football and NFL
The aim of the game is to improve your team through the draft (at the end of each season)
Your players will also gain/lose skills at the end of each season based on age/character/experience of them and the team/skill/max skill 
You are trying to win as many games as possible hopefully you can win the superbowl :)
You will have 15 season's to play and 16 games in each season
If you win more than 10 games you will compete for the superbowl
The results of your team is based on your team score and the oposition team score & a degree of randomness""")
print ("")
print ("Draft")
print ("#######\n")
print ("there are 4 rounds to the draft, each round has 16 players to choose from:")
print ("free agency, older players -Mix of skills ")
print ("first round, young players,- High skills  ")
print ("second round, young players- Medium skills ")
print ("third  round, youngest range of players -Low Skill set\n")

print ("here is your team, at the end of every season you will have a chance to upgrade the team...")
print ("You may also get offers from other teams to swap draft picks")

############### Create initial team

createteam=func_create_players.rn3 (gk =3, defe =8, mid =7, ata =6, exp =0, maxskill =15, skill =5, skillpeak =0, char =10, maxage=33, minskill=2,weighted=0,minage=25)
#createteam=func_create_players.rn3 (gk =3, defe =7, mid =7, ata =5, exp =10, maxskill =19, skill =19, skillpeak =0, char =10, maxage=21, minskill=14,weighted=0,minage=18)
print ("P    Name                S  MS C  E  A")
for i in range(len(createteam)):
    for j in range(len(createteam[i])):
        print(createteam[i][j], end=' ')
    print()
print ("")
print ( "Key")
print ("========")
print ("P=Position")
print ("S=Skill")
print ("MS=Max Skill")
print ("C=Character")
print ("E=Experience")
print ("A=Age")
print ("")

##############playing

#teamscore=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=createteam)

#############

input ("Press any button to start the first season...\n")
os.system('clear')

############

############# Play a season



ng=0
gamesinseasion =16
seasontoplay=20
seasonsplayed=0
#os.system('clear')
while ( seasonsplayed < seasontoplay):
	seasonsplayed = seasonsplayed + 1
	win = 0
	draw = 0
	lost = 0
	for1 = 0
	against = 0
	against1 = 0
	points = 0
	goald = 0
	#default 1 more if playoff
	seasonexp=1
	bseasonoutcome=0


	while (ng < gamesinseasion):
		#print ("Season",seasonsplayed)
		ng = ng + 1
		# opposition scores
		oppgk,oppdef,oppmid,oppata,oppchar,oppexp=func_oppteamscore.oppteamscores(ng)
		



		#

		da=input("press enter to continue...\n")
		ans=True
		while ans:
			if (da == ''):
				ans=False
			elif (da == 'q'):
				print ("ok goodbye")
				ans=False
			else:
				print ("please enter a valid option...\n")
				da=input("select q to exit or enter to continue...\n")
				ns=True
			os.system('clear')
####################### game day
#get my scores
		gkscore,defscore,midscore,atascore,teamchar,rating=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=createteam, printo="nty")

#		ourdefc=(gkscore*3)+(defscore*2)+midscore
#		ouratac=(atascore*3)+(midscore*2)+defscore


		forscore="0"
#		against="0"
		os.system('clear')
		print ("Season {} Game {} " .format(seasonsplayed,ng))
		print ("============================================")

		forscore,against=func_gameday.bat(ourgk=gkscore,oppgk=oppgk,ourdef=defscore,oppdef=oppdef,ourmid=midscore,oppmid=oppmid,ourata=atascore,oppata=oppata,ourchar=teamchar,oppchar=oppchar,ourexp=rating,oppexp=oppexp)
		print ("The Score was",forscore,against)

		#tally scores
		for1 = int(forscore) + int(for1)
		against1 = int(against1) + int(against)
		goald = int(goald) + int(for1) - int(against1)
		if (str(forscore)==str(against)):
			draw = draw + 1
			points = points + 1
		if int(forscore) > int(against):
			win = win + 1
			points = points +3
		if int(forscore) < int(against):
			lost = lost + 1
		print ("============================================")
		print ("This season results")
		glis = gamesinseasion - ng
		print ("Game left", glis)
		print ("Won" ,win)
		print ("draw" , draw)
		print ("lost" , lost)
		print ("goals scored", for1)
		print ("goal conceded", against1)
		print ("")
		print ("============================================")
		if seasonsplayed > 1:
			print ("Previous seasons result (most recent at the bottom of the list)")
			print (season)


	ng = 0		
# superbowl and playoff logic

	oppgks=random.randint (17,20)
	oppdefs=random.randint (17,20)
	oppmids=random.randint (17,20)
	oppatas=random.randint (17,20)
	oppchars=random.randint (150,200)
	oppexps=random.randint (150,200)
	seasonoutcome=""

		
	oppgkp=random.randint (15,18)
	oppdefp=random.randint (15,18)
	oppmidp=random.randint (15,18)
	oppatap=random.randint (15,18)
	oppcharp=random.randint (150,180)
	oppexpp=random.randint (150,180)
	playoffwon="n"
	

	if win > 8 and win <= 10:
		print ("You are off to the Play Offs")
		forscores,againsts=func_gameday.bat(ourgk=gkscore,oppgk=oppgkp,ourdef=defscore,oppdef=oppdefp,ourmid=midscore,oppmid=oppmidp,ourata=atascore,oppata=oppatap,ourchar=teamchar,oppchar=oppcharp,ourexp=rating,oppexp=oppexpp)

		print ("The Score was",forscores,againsts)
		if int(forscores) > int(againsts):
			print ("You are of to the SuperBowl Woop!!!!")
			input("Press a button to continue")
			playoffwon="y"
			os.system('clear')
	
		else:
			print ("You Have lost the Playoff")
			input(" :( Press a button to continue ")
			seasonoutcome="Lost in Playoff"
			seasonexp=1
		

	if win > 10 or playoffwon=="y":
		os.system('clear')
		print ("You are off to the Superbowl")
		forscores,againsts=func_gameday.bat(ourgk=gkscore,oppgk=oppgks,ourdef=defscore,oppdef=oppdefs,ourmid=midscore,oppmid=oppmids,ourata=atascore,oppata=oppatas,ourchar=teamchar,oppchar=oppchars,ourexp=rating,oppexp=oppexps)
		da=input("Press enter to play the superbowl...\n")
		print ("The Score was",forscores,againsts)
		if int(forscores) > int(againsts):
			print ("You Have won the SuperBowl Woop!!!!")
			input("yeh yeh :) yeh yeh\n\n\n\n\n")
			seasonoutcome="Superbowl champions"
			seasonexp=3
		elif  (str(forscores)==str(againsts)):
			randomnumbersbw=random.randint (1,2)
			if randomnumbersbw==1:
				print ("You Have won the SuperBowl In overtime Woop!!!!")
				input("yeh yeh :) yeh yeh\n\n\n\n\n")
				seasonoutcome="Superbowl champions"
				bseasonoutcome=1
				seasonexp=3
			else:
				print ("You Have lost the SuperBowl in Overtime")
				input(" :( \n\n\n\n\n")
				seasonoutcome="Lost in Superbowl in overtime"
				seasonexp=2
				
		else:
			print ("You Have not won the SuperBowl")
			input(" :( \n\n\n\n\n")
			seasonoutcome="Lost in Superbowl"
			seasonexp=2


		

		
 
	print ("End of season...",seasonsplayed)
	teamreport1(createteam=createteam,printto="yp")
	input("please press a button to continue...\n")
	
	
	# end of season stats
	space1="  "

#sort out spacing

	wins="{:<2}".format(win)
	draws="{:<2}".format(draw)
	losts="{:<2}".format(lost)
	for1s="{:<2}".format(for1)
	againsts="{:<2}".format(against1)
	pointss="{:<2}".format(points)
	goald=int(for1)-int(against1)
	goalds="{:<2}".format(goald)


# seasons results
	season +=str(wins) + space1 + str(draws)+ space1 + str(losts)+ space1  + str(for1s) +space1 +str(againsts) +space1 + str(pointss) +space1 +str(goalds)+space1 + seasonoutcome + "\n"
	seasonoutcome=""


	

# team +-
	os.system('clear')
	print ("End of season updates due to Training ")


#	temppop=1

	createteam,changesp,changesn,changesms=func_endofseason.changes(ourteam=createteam,playoffexppoints=seasonexp)
	
	print ("\nPlayers with increased skills\n")
	print ("P    Name                SC NS A")
	print (changesp)
	print ("Players with decreased skills\n")
	print ("P    Name                SC NS A")
	print (changesn)

	#print ()
	#print ("Players with changed Max Skill\n")
	#print ("P    Name                SG NMS A")

#	print (changesms)

	print ("")
	print ( "Key")
	print ("========")
	print ("P=Position")
	print ("SC=Skill Change")
	print ("SG=New Max Skill Gained")
	print ("NS=New Skill")
#	print ("NMS=New Max Skill")
	print ("A=Age")
	print ("")


	input("please press a button to continue...\n")
# Draft
# random number between 1 and x to add a bit of spice to the draft (the further you get in the game the less useful a 3rd round draft is)
# season 1-5  x= 4
# season 6-10 x= 5
# season > 11 x=7

# if  1/5/6/7 offer - swap  1 star for all picks (if not accepted go down path of d,1,2,3 as "normal")
#     else
#       draft 1st round (if you win the superbowl you get penialized with a worse selection of picks)
#       if 2 - swap 2nd and 3rd round picks for another 1st round (this offer feels to good , further tweaks may be needed) if not accepted go down path of 2 and 3 as "normal
#       if 3 - swap 2nd and 3rd round picks for a squad player if not accepted go down path of 2 and 3 as "normal
#       if 4 - normal draft

	randomnumberd=random.randint (1,4)
	#randomnumberd=3
	if seasonsplayed > 5:
		randomnumberd=random.randint (1,5)
	if seasonsplayed > 10:
		randomnumberd=random.randint (1,7)
	if bseasonoutcome == 1:
		randomnumberd=random.randint=7


#	randomnumberdp=random.randint (1,4)
#	randomnumberd=3
	if randomnumberd == 1 or randomnumberd == 5 or randomnumberd == 6 or randomnumberd == 7:

		gkdp=0
		ddp=0
		mdp=0
		adp=0
		if randomnumberdp == 1:
			gkdp=1
			mdp=1
		elif randomnumberdp == 2:
			ddp=1
			gkdp=1
		elif randomnumberdp == 3:
			mdp=1
			ddp=1
		elif randomnumberdp == 4:
			adp=1
			mdp=1

		drafts=func_create_players.rn3(gk =gkdp, defe =ddp, mid =mdp, ata =adp, exp =10, maxskill =20, skill =20, skillpeak =0, char =10, maxage=31, minskill=18,weighted=0,minage=27)
		os.system('clear')
		print ("P    Name                S  MS C  E  A  ")
		for p in range(len(drafts)):
			for r in range(len(drafts[p])):
				print(drafts[p][r], end=' ')
			print()

		while True:
			moveupdraft = input ("Draft alert - A Desprate team are offering you one of their 2 star players in exchange for all your draft picks (y/n)?(above are the options to choose from)... ")
			if moveupdraft =="y" or moveupdraft =="n":
				break
			else:
				print ("Invalid option try again... (y/n)")
	
	
		rngkd=0
		rngkd=random.randint(2,4)
		rnded=random.randint(2,4)
		rnmid=random.randint(2,4)
		rnstd=random.randint(2,4)


		print ("Here is your current team")
		for i in range(len(createteam)):
		    for j in range(len(createteam[i])):
		        print(createteam[i][j], end=' ')
		    print()
		print ("")
		print ( "Key")
		print ("========")
		print ("P=Position")
		print ("S=Skill")
		print ("MS=Max Skill")
		print ("C=Character")
		print ("E=Experience")
		print ("A=Age")
		print ("")

	
		################################################

		if moveupdraft == "y":
			createteam,drafts=draft(myteam=createteam, draft=drafts, typeofdraft="Player swap")
		else:
			draftfa=func_create_players.rn3(gk =rngkd, defe =rnded, mid =rnmid, ata =rnstd, exp =5, maxskill =20, skill =18, skillpeak =0, char =8, maxage=32, minskill=10,weighted=0,minage=26)
			createteam,draftreturned=draft(myteam=createteam, draft=draftfa, typeofdraft="Free Agency")
			draft1=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =2, maxskill =20, skill =14, skillpeak =0, char =10, maxage=22, minskill=10,weighted=0,minage=19)
			createteam,draftreturned=draft(myteam=createteam, draft=draft1, typeofdraft="First round of Draft")
			draft2=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =10, skillpeak =0, char =10, maxage=21, minskill=7,weighted=0,minage=19)
			createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Second round of Draft")
			draft2=func_create_players.rn3(gk =3, defe =5, mid =5, ata =4, exp =0, maxskill =15, skill =9, skillpeak =0, char =10, maxage=20, minskill=5,weighted=0,minage=18)
			createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Third round of Draft")
	
	else:
		rngkd=random.randint(2,4)
		rnded=random.randint(2,4)
		rnmid=random.randint(2,4)
		rnstd=random.randint(2,4)
		rngkdfr=random.randint(2,4)
		rndedfr=random.randint(3,5)
		rnmidfr=random.randint(3,5)
		rnstdfr=random.randint(2,4)


		draftfa=func_create_players.rn3(gk =rngkd, defe =rnded, mid=rnmid, ata=rnstd, exp =15, maxskill =20, skill =16, skillpeak =0, char =8, maxage=32, minskill=10,weighted=0,minage=30)
		createteam,draftreturned=draft(myteam=createteam, draft=draftfa, typeofdraft="Free Agency")

		if bseasonoutcome == 1:
			draft1=func_create_players.rn3(gk =rngkdfr, defe =rndedfr, mid =rnmidfr, ata =rnstdfr, exp =2, maxskill =20, skill =13, skillpeak =0, char =8, maxage=22, minskill=10,weighted=0,minage=20)
			createteam,draftreturned=draft(myteam=createteam, draft=draft1, typeofdraft="First round of Draft")
		else:	
			draft1=func_create_players.rn3(gk =rngkdfr, defe =rndedfr, mid =rnmidfr, ata =rnstdfr, exp =2, maxskill =20, skill =14, skillpeak =0, char =10, maxage=22, minskill=10,weighted=0,minage=19)
			createteam,draftreturned=draft(myteam=createteam, draft=draft1, typeofdraft="First round of Draft")

		if randomnumberd == 2 :

			os.system('clear')
			print ("P    Name                S  MS C  E  A  ")
			for p in range(len(draftreturned)):
				for r in range(len(draftreturned[p])):
					print(draftreturned[p][r], end=' ')
				print()
			moveupdraft = input ("Draft alert - A Division rival have  offered another place in the first round in exchange for your second & third pick,do you accept(y/n)?...(above is the people left in the first round of the draft) ?\n ")
			
			if moveupdraft == "y":
				createteam,draftreturned=draft(myteam=createteam, draft=draftreturned, typeofdraft="First round of Draft -2nd pick")
			else:
				draft2=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =10, skillpeak =0, char =10, maxage=21, minskill=7,weighted=0,minage=19)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Second round of Draft")
				
				draft2=func_create_players.rn3(gk =3, defe =5, mid =5, ata =4, exp =0, maxskill =15, skill =9, skillpeak =0, char =10, maxage=20, minskill=7,weighted=0,minage=18)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Third round of Draft")


		if randomnumberd == 3 :
			randomnumberdr=random.randint (1,2)
			randomnumberdr1=random.randint (1,3)
			randomnumberdr2=random.randint (1,3)
			randomnumberdr3=random.randint (1,3)
			draftmp=func_create_players.rn3(gk =randomnumberdr, defe =randomnumberdr1, mid =randomnumberdr2, ata =randomnumberdr3, exp =10, maxskill =20, skill =18, skillpeak =0, char =8, maxage=33, minskill=11,weighted=0,minage=26)

			os.system('clear')
			print ("P    Name                S  MS C  E  A  ")
			for p in range(len(draftmp)):
				for r in range(len(draftmp[p])):
 					print(draftmp[p][r], end=' ')
				print()
			while True:
				moveupdraft = input ("Draft alert - A Division rival has offered you 1 of his squad in exchange for your second and third round picks,do you accept(y/n)?...(above are the people avaliable) ?\n ")
				if moveupdraft =="y" or moveupdraft =="n":
					break
				else:			
					print ("Invalid option try again... (y/n)")

			if moveupdraft == "y":
				createteam,draftreturned=draft(myteam=createteam, draft=draftmp, typeofdraft="Player swap for draft picks ")
			else:
				draft2=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =10, skillpeak =0, char =10, maxage=21, minskill=7,weighted=0,minage=19)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Second round of Draft")

				draft2=func_create_players.rn3(gk =3, defe =5, mid =5, ata =4, exp =0, maxskill =15, skill =9, skillpeak =0, char =10, maxage=20, minskill=7,weighted=0,minage=18)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Third round of Draft")


		if randomnumberd == 4 :
				draft2=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =10, skillpeak =0, char =10, maxage=21, minskill=7,weighted=0,minage=19)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Second round of Draft")

				draft2=func_create_players.rn3(gk =3, defe =5, mid =5, ata =4, exp =0, maxskill =15, skill =9, skillpeak =0, char =10, maxage=20, minskill=7,weighted=0,minage=18)
				createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Third round of Draft")



	









os.system=('clear')
print ("This is the end of the game i hoped you enjoyed it :)")
############ End of Game

