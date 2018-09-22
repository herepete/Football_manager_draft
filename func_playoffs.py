#!/usr/bin/python3.4
# this is used in working out who won a match
import random
import os
import func_gameday
import mylog
import time
import func_gameday_overtime 

#######################variables

bigdiff=70
smalldif=20
#sleeptime
st=1.2

#######################logic
## pass me the team value and i will do something clever
## Diffence  % Win Draw Lose
## 100         80  10   10
## 50          70  20   10
## 30          50  30   20
## else        30  40   30
## if result is draw use char+exp to see if we can force a result

#######################functions
### which round are we in

def wherearewe(round,ourgk,ourdef,ourmid,ourata,ourchar,ourexp,season):
	oppgk=0
	oppdef=0
	oppmid=0
	oppata=0
	oppexp=0
	oppchar=0
	# increase chance of playoff skill every 2 years 
	season=int(season)
	season=(season/2)
	season=int(season)
	#expe char increased
	seasonex=(season)
	seasonex=int(seasonex)

	if round=="w":
		print ("###Wildcard Weekend###   > Divisonal > Conference > Superbowl")
		print ("=============================================================\n")
		print ("Team ratings")
		print ("============")
		oppgk=random.randint (15,(20+season))
		oppdef=random.randint (10,(15+season))
		oppmid=random.randint (10,(13+season))
		oppata=random.randint (10,(13+season))
		oppexp=random.randint (100,(200+seasonex))
		oppchar=random.randint (125,(200+seasonex))
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("Normal game time")
		print ("================")
		time.sleep(st)
		print ("The Score was",forscore,against)
		if (str(forscore)==str(against)):
			print ("\nGoing to Overtime")
			print ("=================")
			time.sleep(st)	
			forscore,against=func_gameday_overtime.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp,ourprevgoals=int(forscore),oppprevgoals=int(against))
			print ("The Score was",forscore,against)
			print ()

	if round=="d":
		print ("Wildcard Weekend  > ###Divisonal### > Conference > Superbowl")
		print ("=============================================================\n")
		print ("Team ratings")
		print ("============")
		oppgk=random.randint (15,(20+season))
		oppdef=random.randint (13,(15+season))
		oppmid=random.randint (13,(15+season))
		oppata=random.randint (13,(15+season))
		oppexp=random.randint (130,(200+seasonex))
		oppchar=random.randint (130,(200+seasonex))
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("Normal game time")
		print ("================")
		time.sleep(st)
		print ("The Score was",forscore,against)
		if (str(forscore)==str(against)):
			print ("\nGoing to Overtime")
			print ("=================")
			time.sleep(st)	
			forscore,against=func_gameday_overtime.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp,ourprevgoals=int(forscore),oppprevgoals=int(against))
			print ("The Score was",forscore,against)
			print ()


	if round=="c":
		mylog.fmlog(detail=str(("Wildcard Weekend -start ")), verbosity=1)
		print ("Wildcard Weekend  > Divisonal > ###Conference### > Superbowl")
		print ("=============================================================\n")
		print ("Team ratings")
		print ("============")
		oppgk=random.randint (14,(20+season))
		oppdef=random.randint (14,(18+season))
		oppmid=random.randint (14,(18+season))
		oppata=random.randint (14,(18+season))
		oppexp=random.randint (140,(200+seasonex))
		oppchar=random.randint (140,(200+seasonex))
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("Normal game time")
		print ("================")
		time.sleep(st)
		print ("The Score was",forscore,against)
		if (str(forscore)==str(against)):
			print ("\nGoing to Overtime")
			print ("==================")
			time.sleep(st)
			forscore,against=func_gameday_overtime.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp,ourprevgoals=int(forscore),oppprevgoals=int(against))
			print ("The Score was",forscore,against)
			print ()



	if round=="s":
		print ("Wildcard Weekend   > Divisonal > Conference > ###Superbowl###")
		print ("=============================================================\n")
		print ("Team ratings")
		print ("============")

		oppgk=random.randint (15,(20+season))
		oppdef=random.randint (16,(20+season))
		oppmid=random.randint (16,(20+season))
		oppata=random.randint (16,(20+season))
		oppexp=random.randint (150,(200+seasonex))
		oppchar=random.randint (150,(200+seasonex))
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("Normal game time")
		print ("================")
		time.sleep(st)
		print ("The Score was",forscore,against)

		if (str(forscore)==str(against)):
			print ("\nGoing to Overtime")
			print ("==================")
			time.sleep(st)
			forscore,against=func_gameday_overtime.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp,ourprevgoals=int(forscore),oppprevgoals=int(against))
			print ("The Score was",forscore,against)
			print ()


	return forscore,against

def overtime():

	usrandomnumber=random.randint (0,1)
	opprandomnumber=1
	time.sleep(st)

# u = us
# o =opposition
	whowon=""
	print ("\nSudden death Overtime")
	print ("=====================")
	time.sleep(st)
	if usrandomnumber == 1:
		whowon="u"
		print ("\nYou won in Sudden death overtime\n")
	else:
		whowon="o"
		print ("\nYou Lost in Sudden death overtime\n")
	return whowon


def bat(ourgk,ourdef,ourmid,ourata,ourchar,ourexp,ourwins,season):
	os.system('clear')
	#global season
# work out which round to drop be in
	#time.sleep(3)
	resulto=""
	howwedo=""
	whowon=""
	seasonexp=1
	#os.system('clear')
	randomplayoffs=random.randint (7,9)
	if ourwins < randomplayoffs:
		print("You team tried vantaltey but have not been good enough to reach the playoffs")
		input("\nPress Enter to continue\n")
		#time.sleep(2)
	else:
		print ("Playoff Rounds")
		print ("==============")
		print ("\nYou are entering the play offs , there are 4 rounds and the games will get harder at each step\nIf you win you players get extra experience\n")
	#	time.sleep(st)
	if randomplayoffs <= ourwins < 11:
		print("You team have Reached the Playoffs but you are not a top seed so you will need to work your way through the playoffs starting at the wildcard Weekend")
		print ("These are the stages\n\n#####Wildcard Weekend#####   > Divisonal > Conference > Superbowl")
		input("\nPress a button to continue\n")
		os.system('clear')
		#time.sleep(2)
	if (ourwins > 10):
		print ("You team have Reached the Playoffs you are a top seed so you will not have to play in the wildcard weekend and will start in the Divisional round")
		print ("These are the stages\n\nWildcard Weekend   > #####Divisonal#### > Conference > Superbowl")
		input("\nPress a button to continue\n")
		os.system('clear')
		#time.sleep(2)


	if randomplayoffs <= ourwins < 11:
		#print ("\nYou are entering the play offs , there are 4 rounds and the games will get harder at each step\nIf you win you players get extra experience but you will also not have as good a draft choice next season\n")
	#	oppgk,oppdef,oppmid,oppata,oppexp,oppchar=wherearewe(round="w",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
		forscore,against=wherearewe(round="w",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp,season=season)
		# tie lets go get a result
		mylog.fmlog(detail=str(("Forscore ", forscore)), verbosity=1)
		mylog.fmlog(detail=str(("Againstscore ", against)), verbosity=1)
	#	forscore = 7
#		against = 7
#		for testing to force playoff:
#		forscore=1
#		against=1

		if int(forscore) == int(against):
			# get overtime result
			mylog.fmlog(detail="if hit ", verbosity=1)
			whowon=overtime()
			mylog.fmlog(detail=str(("Overtime score ", resulto)), verbosity=1)
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("\nYou won,your off to the Divisional round!\n")
			resulto="u"
			input("Press a button to continue")
			os.system('clear')
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("\nPlayoff Summary")
			print ("===============")
			print ("You lost")
			howwedo="Wildcard Weekend"
			resulto="o"
			print ("But you gained +1 Exp")
			seasonexp=1
			input("\nPress a button to continue")
	if (ourwins > 10) or (resulto =="u"):
		#whowon=""
		#time.sleep(3) 
		forscore,against=wherearewe(round="d",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp,season=season)
                # tie lets go get a result
		if int(forscore) == int(against):
			whowon=overtime()
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("\nYou won, you are off to the conference final!\n")
			resulto="u"
			input("Press a button to continue")
			os.system('clear')
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("\nPlayoff Summary")
			print ("===============")
			print ("You lost")
			resulto="o"
			howwedo="Divisional round"
			seasonexp=2
			print ("But you gained +2 Exp")
			input("\nPress a button to continue")


	if  (resulto =="u"):
		#whowon=""
		#time.sleep(3) 
		forscore,against=wherearewe(round="c",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp,season=season)
                # tie lets go get a result
		if int(forscore) == int(against):
			whowon=overtime()
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("You won you are off to the superbowl!\n")
			resulto="u"
			input("Press a button to continue to the Superbowl")
			os.system('clear')
		if int(against) > int(forscore)  or (whowon=="o"):
			print ("\nPlayoff Summary")
			print ("===============")
			print ("You lost")
			resulto="o"
			howwedo="Conference Final"
			seasonexp=2
			print ("But you gained +2 Exp")
			input("\nPress a button to continue")
	if  (resulto =="u"):
		#time.sleep(3) 
		forscore,against=wherearewe(round="s",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp,season=season)
                # tie lets go get a result
		if int(forscore) == int(against):
			whowon=overtime()
		print ("\nPlayoff Summary")
		print ("===============")
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("\nYou have won the Superbowl!")
			howwedo="Won SuperBowl"
			print ("Woop Woop")
			print ("You gained +4 Exp")
			input("\nPress a button to continue")
			seasonexp=4
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("You lost\n")
			howwedo="Lost SuperBowl"
			seasonexp=3
			print ("But you gained +3 Exp")
			input("\nPress a button to continue")

#	time.sleep(3)
	mylog.fmlog(detail=str(("Experience from playoff ",seasonexp)), verbosity=12)

	return (howwedo,seasonexp) 
























