#!/usr/bin/python3.4
# this is used in working out who won a match
import random
import os
import func_gameday
import mylog
import time

#######################variables

bigdiff=70
smalldif=20

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

def wherearewe(round,ourgk,ourdef,ourmid,ourata,ourchar,ourexp):
	oppgk=0
	oppdef=0
	oppmid=0
	oppata=0
	oppexp=0
	oppchar=0

	if round=="w":
		print ("###Wildcard Weekend###   > Divisonal > Conference > Superbowl")
		oppgk=random.randint (15,20)
		oppdef=random.randint (10,15)
		oppmid=random.randint (10,13)
		oppata=random.randint (10,13)
		oppexp=random.randint (100,200)
		oppchar=random.randint (125,200)
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("The Score was",forscore,against)



	if round=="d":
		print ("Wildcard Weekend  > ###Divisonal### > Conference > Superbowl")
		oppgk=random.randint (15,20)
		oppdef=random.randint (13,15)
		oppmid=random.randint (13,15)
		oppata=random.randint (13,15)
		oppexp=random.randint (130,200)
		oppchar=random.randint (130,200)
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("The Score was",forscore,against)

	if round=="c":
		mylog.fmlog(detail=str(("Wildcard Weekend -start ")), verbosity=1)
		print ("Wildcard Weekend  > Divisonal > ###Conference### > Superbowl")
		oppgk=random.randint (15,20)
		oppdef=random.randint (15,18)
		oppmid=random.randint (15,18)
		oppata=random.randint (15,18)
		oppexp=random.randint (150,200)
		oppchar=random.randint (150,200)
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("The Score was",forscore,against)



	if round=="s":
		print ("Wildcard Weekend   > Divisonal > Conference > ###Superbowl###")

		oppgk=random.randint (15,20)
		oppdef=random.randint (17,20)
		oppmid=random.randint (17,20)
		oppata=random.randint (17,20)
		oppexp=random.randint (175,200)
		oppchar=random.randint (175,200)
		forscore,against=func_gameday.bat(ourgk=ourgk,oppgk=oppgk,ourdef=ourdef,oppdef=oppmid,ourmid=ourmid,oppmid=oppmid,ourata=ourata,oppata=oppata,ourchar=ourchar,oppchar=oppchar,ourexp=ourexp,oppexp=oppexp)
		print ("The Score was",forscore,against)


	return forscore,against

def overtime():

	usrandomnumber=random.randint (0,1)
	opprandomnumber=1

# u = us
# o =opposition
	whowon=""
	time.sleep(3)
	print ("Playing Overtime")
	if usrandomnumber == 1:
		whowon="u"
		print ("You won in overtime")
	else:
		whowon="o"
		print ("You Lost in overtime\n")
		time.sleep(3)
	return whowon


def bat(ourgk,ourdef,ourmid,ourata,ourchar,ourexp,ourwins):
	os.system('clear')
# work out which round to drop be in
	#time.sleep(3)
	resulto=""
	howwedo=""
	whowon=""
	seasonexp=1
	#os.system('clear')
	if 8 < ourwins < 11:
	#if 4 < ourwins < 11:
		time.sleep(3)
		print ("You are entering the play offs , there are 4 rounds and the games will get harder at each step\n if you win you players get extra experience but you will also not have as good a draft choice next season\n")
	#	oppgk,oppdef,oppmid,oppata,oppexp,oppchar=wherearewe(round="w",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
		forscore,against=wherearewe(round="w",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
		# tie lets go get a result
		mylog.fmlog(detail=str(("Forscore ", forscore)), verbosity=1)
		mylog.fmlog(detail=str(("Againstscore ", against)), verbosity=1)
	#	forscore = 7
#		against = 7
		if int(forscore) == int(against):
			# get overtime result
			mylog.fmlog(detail="if hit ", verbosity=1)
			resulto=overtime()
			mylog.fmlog(detail=str(("Overtime score ", resulto)), verbosity=1)
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("You won,your off to the Divisional round!\n")
			resulto="u"
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("You lost\n")
			howwedo="Wildcard Weekend"
			resulto="o"
			time.sleep(3) 
	if (ourwins > 10) or (resulto =="u"):
		#whowon=""
		time.sleep(3) 
		forscore,against=wherearewe(round="d",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
                # tie lets go get a result
		if int(forscore) == int(against):
			resulto=overtime()
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("You won, you are off to the conference final!\n")
			resulto="u"
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("You lost\n")
			resulto="o"
			time.sleep(3) 
			howwedo="Divisional round"

	if  (resulto =="u"):
		#whowon=""
		time.sleep(3) 
		forscore,against=wherearewe(round="c",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
                # tie lets go get a result
		if int(forscore) == int(against):
			resulto=overtime()
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("You won you are off to the superbowl!\n")
			resulto="u"
		if int(against) > int(forscore)  or (whowon=="o"):
			print ("You lost\n")
			resulto="o"
			time.sleep(3) 
			howwedo="Conference Final"
			seasonexp=2
	if  (resulto =="u"):
		time.sleep(3) 
		forscore,against=wherearewe(round="s",ourgk=ourgk,ourdef=ourdef,ourmid=ourmid,ourata=ourata,ourchar=ourchar,ourexp=ourexp)
                # tie lets go get a result
		if int(forscore) == int(against):
			resulto=overtime()
		if (int(forscore) > int(against)) or (whowon=="u"):
			print ("You have won the superbowl!")
			
			howwedo="Won SuperBowl"
			seasonexp=3
		if (int(against) > int(forscore)) or (whowon=="o"):
			print ("You lost\n")
			howwedo="Lost SuperBowl"


#	time.sleep(3)

	return (howwedo,seasonexp) 
























