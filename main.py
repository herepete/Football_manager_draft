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
import func_gameday_overtime
import func_teamratings
import func_endofseason
import func_oppteamscore
import func_playoffs
import mylog
import func_faanddraft
import pdb


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
	printouttod=typeofdraft
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
		mylog.fmlog(detail=str(("Type of Draft ", typeofdraft)), verbosity=2)

		print ("P    Name                S  MS C  E  A")

		for i in range(len(draft)):
			positioninteam1=positioninteam1+1
			for j in range(len(draft[i])):
				if select1 == positioninteam1:
					print(draft[i][j], end=' ')
					b=(draft[i][j])
					b1=(draft[i])
					b2=(draft[j])
		#			mylog.fmlog(detail=str(("Player Drafted ", b)), verbosity=2)
			#	mylog.fmlog(detail=str(("Player Drafted ", b)), verbosity=2)

			#del draft[i]
					z=1
				else:
					z=0
			if z == 1:
        	        	print ()

		badstring=str(printouttod)+','+str(b1)
		mylog.fmlog(detail=str(("Player Drafted %s"%b )), verbosity=21)
		mylog.fmlog(detail=str(("Player Drafted ",badstring)), verbosity=22)
#		mylog.fmlog(detail=str(("Player Drafted %s"%b2 )), verbosity=23)

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

############## print draft picks

def draftpicks(firstroundthisyear,secondroundthisyear,thirdoroundthisyear):
	print ("you have First round this year=",firstroundthisyear)
	print ("you have Second round this year=",secondroundthisyear)
	print ("you have Third round this year=",thirdoroundthisyear)




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
season = "W   D   L   F   A   P   GD     GK  DE  MI  ST  CH   EX\n"
os.system('rm log.txt')
############## Intro
os.system('clear')
print ("""Welcome to Football Manager Draft
===============
This game is a mashup of football and NFL
The aim of the game is to win the Superbowl
And to give you 30ish mins of fun.

Each game will by default last 20 seasons (a lot of these seeing can be changed through pressing a)
You will be given a randomised poor squad at the begening of the game.

A squad constist of 3 Goalkeeper,8 Defenders,7 Midfielders & 6 Atackers 
Your team score is based on the skill ratings of your top 11 players in a 4-4-2 formation + the Experience and Character of the whole squad.

Typically a top team score is 100.
GK,Def,Mid contribute to def scores (with different weighings)
Def,Mid,Str contribute to ata scores (with different weighings)

If you draw a game the game will go to overtime to try and force a result.

You will play 16 games in a season and if you win enough games you will enter the playoffs (depending on the number of wins you will enter at a different point)
The playoff has 4 rounds, with the 4th being the Superbowl.

After the season has finished your players will lose/gain skill based on age/character/experience/luck.
At a random(ish!) age players skills will start to drop as they become to old (each game will have an 'old' value)

Then you will have a chance to improve your team by drafting young players through the draft or you can swap your picks for established players.
There are 3 rounds to the draft , with the 1st Round having players with better skills.
You can swap your players for extra draft picks.
You can move up and down the draft (i.e if you have swapped your players for extra picks you can create another first or second pick, so if you have 2 great GK you could trade one for another pick to help strethen another position)

And then you start a new season.


Good luck :) """)

advancedsettings=input ("\nPress a to enter advanced settings or anything else to continue\n")

##############
#defaults 
# adding here because they may be overwritten by menu options
stp=20 # number of seasons
maxa=33 # max age
mina=25 # min age
mins=2 # min skill
maxs=5 # skill
maxxs=20 #maxskill
exp=0 #experience

seasonsplayed=0

# set drafting defaults
firstroundthisyear=1
secondroundthisyear=1
thirdoroundthisyear=1
firstroundnextyear=1
secondroundnextyear=1
thirdoroundnextyear=1


#############
os.system('clear')
if advancedsettings=="a":
	while True:
		os.system('clear')
		print ("Default settings")
		print ("================")
		print ("Number of seasons to play=",stp)
		print ("Start in season=",seasonsplayed)
		print ("Max age of your initial team=",maxa)
		print ("Min age of your inital team=",mina)
		print ("Min skill of your inital team=",mins)
		print ("Max Skill of your inital team=",maxs)
		print ("First round draft picks first year=",firstroundthisyear)
		print ("Second round draft picks first year=",secondroundthisyear)
		print ("Third round draft picks first year", thirdoroundthisyear)
		print ("================")


#		whattodo=input("\nPress\n e to Save & Exit this menu\n s to change numbers of seasons to play\n o to get a old very good team \n y to get a good young team...\n a to get an amazing team \n t to change the season you start in\n c Clevland Browns Scenario (Large Draft Capital in the first year only)\n w Work the draft,get 2 second and 2 third round picks per year\n r Random team\n")
		whattodo=input("\nPress\n e to Save & Exit this menu\n s to change numbers of seasons to play\n o to get a old very good team \n y to get a good young team...\n a to get an amazing team \n r Random team\n t to change the season you start in\n c Clevland Browns Scenario (Large Draft Capital in the first year only)\n w Work the draft,get 2 second and 2 third round picks per year\n m minimize draft to help stuff stop scrolling of the page which is not good when using screen")


		if whattodo=="e":
			break
		if whattodo=="s":
			numberofseasonstpplay=input("how many seasons do you want to play?\n")
			stp=int(numberofseasonstpplay)
			print ("Changes made")
		if whattodo=="y":
			maxa=21
			mina=18
			mins=10
			maxs=20
			maxxs=20
			exp=2
			
			print ("Changes made")

		if whattodo=="r":
			maxa=33
			mina=18
			mins=8
			maxs=20
			maxxs=20
			exp=10
			print ("Changes made")


		if whattodo=="o": 
			maxa=35
			mina=28
			mins=13
			maxs=19
			maxxs=20
			exp=10
			print ("Changes made")
		if whattodo=="a":
			maxa=30
			mina=18
			mins=18
			maxs=19
			maxxs=20
			exp=10
			print ("Changes made")
		if whattodo=="t":
			numberofseasonsin=input("which Season do you want to start in?\n")
			seasonsplayed=int(numberofseasonsin)
			print ("Changes made")
		if whattodo=="c":
			firstroundthisyear=2
			secondroundthisyear=2
			thirdoroundthisyear=1
		if whattodo=="w":
			firstroundthisyear=0
			secondroundthisyear=2
			thirdoroundthisyear=2
			firstroundnextyear=0
			secondroundnextyear=2
			thirdoroundnextyear=2

			
			print ("Changes made")


			

#		else:
#			print ("\nInvalid option try again\n",whattodo)
			

#os.system=('clear')


############### Create initial team

print ("Here is your team...\n")
createteam=func_create_players.rn3 (gk =3, defe =8, mid =7, ata =6, exp =exp, maxskill =maxxs, skill =maxs, skillpeak =0, char =10, maxage=maxa, minskill=mins,weighted=0,minage=mina,minrchar=0)
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
#os.system('clear')

############

############# Play a season



ng=0
gamesinseasion =16
totalpoints = 0
totalgoaldifference = 0
totalplayoffsnsb = 0
totalsuperbowwins = 0
# set drafting defaults
#firstroundthisyear=1
#secondroundthisyear=1
#thirdoroundthisyear=1
#firstroundnextyear=1
#secondroundnextyear=1
#thirdoroundnextyear=1


# move higher up the tree so user can change this without it being overwritten
seasontoplay=stp
#seasonsplayed=0 moved to memory
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
		gkscore,defscore,midscore,atascore,eteamchar,erating,avgage=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=createteam, printo="nty")
		#gkscore,defscore,midscore,atascore,teamchar,rating=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=createteam, printo="nty")

		forscore="0"
		os.system('clear')
		print ("Season {} Game {} " .format(seasonsplayed,ng))
		print ("============================================")

		forscore,against=func_gameday.bat(ourgk=gkscore,oppgk=oppgk,ourdef=defscore,oppdef=oppdef,ourmid=midscore,oppmid=oppmid,ourata=atascore,oppata=oppata,ourchar=eteamchar,oppchar=oppchar,ourexp=erating,oppexp=oppexp)
		print ("The Score was",forscore,against)

#### insert me here

		if (str(forscore)==str(against)):
			print ("\nGoing to Overtime")
			forscore,against=func_gameday_overtime.bat(ourgk=gkscore,oppgk=oppgk,ourdef=defscore,oppdef=oppdef,ourmid=midscore,oppmid=oppmid,ourata=atascore,oppata=oppata,ourchar=eteamchar,oppchar=oppchar,ourexp=erating,oppexp=oppexp,ourprevgoals=int(forscore),oppprevgoals=int(against))
			print ("The Score was",forscore,against)




		for1 = int(forscore) + int(for1)
		against1 = int(against1) + int(against)
		totalgoaldifference = int(totalgoaldifference) + int(forscore)-int(against)
		if (str(forscore)==str(against)):
			draw = draw + 1
			points = points + 1
			totalpoints=int(totalpoints) + int(1)
		if int(forscore) > int(against):
			win = win + 1
			points = points +3
			totalpoints=int(totalpoints)+int(3)
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
			print ("Previous seasons result (most recent at the bottom of the list)& Teamstats")
			print (season)


	ng = 0		
# superbowl and playoff logic
	seasonoutcome,seasonexp=func_playoffs.bat(ourgk=gkscore,ourdef=defscore,ourmid=midscore,ourata=atascore,ourchar=eteamchar,ourexp=erating,ourwins=win,season=seasonsplayed)
	
	mylog.fmlog(detail=str(("Log-Season Wins ", win)), verbosity=1)	
	mylog.fmlog(detail=str(("Log-Season Outcome ", seasonoutcome)), verbosity=1)	
	mylog.fmlog(detail=str(("Log-Season Exp ", seasonexp)), verbosity=1)	

	if int(seasonexp)==3:
		totalsuperbowwins=totalsuperbowwins+1

		
 
	print ("End of season...",seasonsplayed)
#	teamreport1(createteam=createteam,printto="yp")
	while True:
		continuetonextstep=input("please press c button to continue...\n")
		if continuetonextstep=="c":
			break
	
	
	
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
	goalds="{:<3}".format(goald)

	gkscores="{:<2}".format(gkscore)
	defscores="{:<2}".format(defscore)
	midscores="{:<2}".format(midscore)
	atascores="{:<2}".format(atascore)
	teamchars="{:<2}".format(eteamchar)
	myteamexps="{:<2}".format(erating)



# seasons results
	season +=str(wins) + space1 + str(draws)+ space1 + str(losts)+ space1  + str(for1s) +space1 +str(againsts) +space1 + str(pointss) +space1 +str(goalds) +space1 +space1  + str(gkscores)+space1  + str(defscores) +space1 + str(midscores) +space1 + str(atascores) +space1 + str(teamchars) +space1 +str(myteamexps) +space1  + seasonoutcome + "\n"
	seasonoutcome=""

#add break to stop darft in last season

	if seasonsplayed == seasontoplay:
		break

# team +-
	os.system('clear')
	print ("End of season updates due to Training ")


#	temppop=1

	createteam,changesp,changesn,changesms=func_endofseason.changes(ourteam=createteam,playoffexppoints=seasonexp,seasonnumber=seasonsplayed)
	
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
### Draft
# random number between 1 and x to add a bit of spice to the draft (the further you get in the game the less useful a 3rd round draft is)
# season 1-5  x= 4
# season 6-10 x= 5
# season > 11 x=7
#	firstroundthisyear=1
#	secondroundthisyear=1
#	thirdoroundthisyear=1
#	firstroundnextyear=1
#	secondroundnextyear=1
#	thirdoroundnextyear=1

# moving draft higher to allow draft analysis
	
	draft1=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =20, skill =14, skillpeak =0, char =10, maxage=22, minskill=10,weighted=0,minage=19,minrchar=6)

	input("You now have the option to swap your players for extra draft picks")
	createteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear=func_faanddraft.sell_player(ourteam=createteam,firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear,draft1=draft1,season=seasonsplayed)


# if  1/5/6/7 offer - swap  1 star for all picks (if not accepted go down path of d,1,2,3 as "normal")
#     else
#       draft 1st round (if you win the superbowl you get penialized with a worse selection of picks)
#       if 2 - swap 2nd and 3rd round picks for another 1st round (this offer feels to good , further tweaks may be needed) if not accepted go down path of 2 and 3 as "normal
#       if 3 - swap 2nd and 3rd round picks for a squad player if not accepted go down path of 2 and 3 as "normal
#       if 4 - normal draft
	os.system('clear')
	draftpicks(firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear)
	input("Press a button to continue\n")
#	print ("you have First round this year=",firstroundthisyear)
#	print ("you have Second round this year=",secondroundthisyear)
#	print ("you have Third round this year=",thirdoroundthisyear)


	rngkd=random.randint(2,4)
	rnded=random.randint(2,4)
	rnmid=random.randint(2,4)
	rnstd=random.randint(2,4)

	#draftfa=func_create_players.rn3(gk =rngkd, defe =rnded, mid =rnmid, ata =rnstd, exp =5, maxskill =20, skill =18, skillpeak =0, char =8, maxage=32, minskill=10,weighted=0,minage=28,minrchar=3)
	#createteam,draftreturned=draft(myteam=createteam, draft=draftfa, typeofdraft="Free Agency")
	numofloops=0
	while firstroundthisyear > 0:
		#draft1=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =20, skill =14, skillpeak =0, char =10, maxage=22, minskill=10,weighted=0,minage=19,minrchar=6)
		# adding logic to reuse the already offered draft players rather than a new bunch of players
		if numofloops >= 1:
			createteam,draftreturned=draft(myteam=createteam, draft=draftreturned, typeofdraft="First round of Draft")
			numofloops=numofloops+1
		else:
			createteam,draftreturned=draft(myteam=createteam, draft=draft1, typeofdraft="First round of Draft")
			numofloops=numofloops+1
		firstroundthisyear=int(firstroundthisyear)-1
		os.system('clear')
		draftpicks(firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear)
		input("Press a button to continue\n")
	numofloops=0
	while secondroundthisyear > 0:
		draft2=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =12, skillpeak =0, char =10, maxage=21, minskill=9,weighted=0,minage=19,minrchar=6)
		if numofloops >= 1:
			createteam,draftreturned=draft(myteam=createteam, draft=draftreturned, typeofdraft="Second round of Draft")
			numofloops=numofloops+1
		else:
			createteam,draftreturned=draft(myteam=createteam, draft=draft2, typeofdraft="Second round of Draft")
			numofloops=numofloops+1
		secondroundthisyear=int(secondroundthisyear)-1
		os.system('clear')
		draftpicks(firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear)
		input("Press a button to continue\n")
	numofloops=0
	while thirdoroundthisyear > 0:
		draft3=func_create_players.rn3(gk =2, defe =5, mid =5, ata =4, exp =1, maxskill =15, skill =12, skillpeak =0, char =10, maxage=20, minskill=7,weighted=0,minage=18,minrchar=6)

		if numofloops >= 1:
			createteam,draftreturned=draft(myteam=createteam, draft=draftreturned, typeofdraft="Third round of Draft")
			numofloops=numofloops+1
		else:
			createteam,draftreturned=draft(myteam=createteam, draft=draft3, typeofdraft="Third round of Draft")
			numofloops=numofloops+1
		thirdoroundthisyear=int(thirdoroundthisyear)-1
		os.system('clear')
		draftpicks(firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear)
		input("Press a button to continue\n")


	# rebalance end of season numbers around so next season we have some players to pick from :)
	firstroundthisyear=firstroundnextyear
	secondroundthisyear=secondroundnextyear
	thirdoroundthisyear=thirdoroundnextyear

	firstroundnextyear=firstroundthisyear
	secondroundnextyear=secondroundthisyear
	thirdoroundnextyear=thirdoroundthisyear
	









os.system=('clear')
print ("This is the end of the game i hoped you enjoyed it :)")
print ("Here is how you did")
print ("Total points=",totalpoints)
print ("Total goal difference=",totalgoaldifference)
print ("Total number of playoff defeats (including Superbowl loss)=",totalplayoffsnsb)
print ("Total Superbowls=",totalsuperbowwins)
print ("\nStats")
print ("======")
print ("Previous seasons result (most recent at the bottom of the list)")
print (season)

############ End of Game

