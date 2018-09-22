#!/usr/bin/python3.4
# badly named this is really the pre draft stuff between end of season training and 1st Round of the draft

################ Imports and System Bits
import os
import random
import func_create_players
import func_gameday
import func_teamratings
import func_endofseason
import func_oppteamscore
import func_playoffs
import mylog
import pdb
#file = open('log.txt', 'w+')
#import func_analsyispicks
import subprocess





os.system('clear')
global playerstobuy
timespressed=0
#################################################### Functions

def scoutthedraft (draft1):

	os.system('clear')
	print ("Here is a sneak look at the first round of the draft")

	for i in range(len(draft1)):
		for j in range(len(draft1[i])):
			print (draft1[i][j], end=' ')

		print ()


	
	input("Press a button to continue")


#def scoutthedraft (draft1):

#	position=""
#	fname=""
#	skill=""
#	mskill=""
#	char=""
#	age=""
#	GKrating=[]
#	DEFrating=[]
#	MIDrating=[]
#	ATArating=[]
#
#	for i in range(len(draft1)):
#		for j in range(len(draft1[i])):
#			position= (draft1[i][0])		
#			position=position.strip()
#			
#			fname= (draft1[i][1])		
#
##			skill= (draft1[i][3])
#			skill=int(skill)	
#
##			mskill=(draft1[i][4])
#			mskill=int(mskill)
#
#			char=(draft1[i][5])
#			char=int(char)
#
#			age=(draft1[i][7])
#			age=int(age)
#		
#			if (age < 20) and (skill >=13) and (char>=8) and (mskill >=14):
#				pdb.set_trace()
#				list_to_insert_to=position+"rating"
#				list_to_insert_to.insert="1"
#				
#			if (age < 20) and (skill >=14) and char(>=9) and (mskill >=15):
#			if (age < 20) and (skill >=14) and char(>=9) and (mskill >=15):
#			if (age < 20) and (skill >=14) and char(>=9) and (mskill >=15):
#			if (age < 20) and (skill >=14) and char(>=9) and (mskill >=15):
#			if (age < 20) and (skill >=14) and char(>=9) and (mskill >=15):
			
				
		#	pdb.set_trace()

			

def movedowndraft(firstroundthisyear,secondroundthisyear,thirdoroundthisyear):

	os.system('clear')
	timespressed=0
	dealrejected=0
	print ("Here are your current picks")
	print ("====================")
	print ("Firstroundthisyear",firstroundthisyear)
	print ("Secondroundthisyear",secondroundthisyear)
	print ("Thirdoroundthisyear",thirdoroundthisyear)
	print ("====================")

	if firstroundthisyear>0:
		offer1=input ("\nOffer-Do you want add an extra second and third for your first choice. press y to accept\n")
		if offer1=="y":
			firstroundthisyear=firstroundthisyear-1
			secondroundthisyear=secondroundthisyear+1
			thirdoroundthisyear=thirdoroundthisyear+1
			input("swap done, Press enter to contiue")
			
		else:
			input("no swap done, Press  button to Continue")	
			dealrejected=1	

	if  secondroundthisyear>0:

		offer2=input ("\nOffer-Do you want to add 2 third for your second. press y to accept\n")
		if offer2=="y":
			secondroundthisyear=secondroundthisyear-1
			thirdoroundthisyear=thirdoroundthisyear+2
			input("swap done, Press enter to contiue")
		else:
#			print("Fair enough , no swap done")
			input("no swap done, Press  button to Continue")	

	elif dealrejected==1:
		input("You do not have any first or second round picks to move down the draft")	
	else:
		pass
	return (firstroundthisyear,secondroundthisyear,thirdoroundthisyear)
def buypplayer (firstroundthisyear,secondroundthisyear,thirdoroundthisyear,playerstobuy,ourteam):

	enoughcapital=0
	maxoption=len(playerstobuy)+1
	#pdb.set_trace()

	while True:
		select3=input("\nWho do you want to Buy (or press e to exit?)...")
		mylog.fmlog(detail=str(("Who do you want to Buy (press e to exit)...", select3)), verbosity=9)
		if select3=="e":
			enoughcapital=0
			intselect3="99"
			break
		if select3.isnumeric():
			if 0<=int(select3) <=maxoption:
				intselect3=int(select3)
#				a2test= ourteam[intselect3]
				# hacking data to make is usable, stripping out fields and commas ,
				try:
					a2 = playerstobuy[intselect3]
				except:
					pdb.set_trace()
				mylog.fmlog(detail=str(("Who am i going to buy ", a2)), verbosity=9)
				a2p = a2[1:2]
				a2p= (''.join(a2p))
				mylog.fmlog(detail=str(("Players Position ", a2p)), verbosity=9)
				valueofplayer=a2[9:10]
				valueofplayer=(''.join(valueofplayer))
				mylog.fmlog(detail=str(("Value of player ", valueofplayer)), verbosity=9)
				#strip a few bits out of player to make is usable for our team
				a2.pop(0)
				a2.pop(8)
				firstroundthisyear,secondroundthisyear,thirdoroundthisyear,enoughcapital=sellplayerbuy(firstroundthisyear,secondroundthisyear,thirdoroundthisyear,valueofplayer,a2)
				break
			else:
				print ("Invalid number please try again")
				pdb.set_trace()

		print ("Invalid option try again...\n")

	incrementalnumber=0
	playinposition=0
	minposition=0
	maxposition=0
	z=0
	rangeofpaval=[]
	print ()
	os.system('clear')

	if enoughcapital==1:
		print ("These are the people you can replace")
		print ("P    Name                S  MS C  E  A  N")
		for i1 in range(len(ourteam)):
			incrementalnumber=incrementalnumber+1
			for j1 in range(len(ourteam[i1])):
				playerposinteam=ourteam[i1][0]
				if playerposinteam in a2p:
	#				incrementalnumber=incrementalnumber+1
					playinposition=playinposition+1
					if playinposition ==1:
						playinposition=incrementalnumber
					maxposition=incrementalnumber					
					print(ourteam[i1][j1], end=' ')
					z=1
				else:
					z=0
			if z == 1:
	#			incrementalnumber=incrementalnumber+1
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
		#input ("Who do you choose?")
		mylog.fmlog(detail=str(("minposition= ", minposition)), verbosity=9)	
		mylog.fmlog(detail=str(("maxposition= ", maxposition)), verbosity=9)	

		while True:
			select2=input("\nWho do you want to Sell? " )
			if select2.isnumeric():
				if minposition<= int(select2) <= maxposition :
					whotoreplace=int(select2)-1
					break
				else:
					pass
				print ("Invalid option try again...\n")


		#pdb.set_trace()
#		if enoughcapital==1:
		del ourteam[whotoreplace]
		#	del playerstobuy[intselect3]
		del playerstobuy[intselect3]
		ourteam.insert(whotoreplace, (a2))
	
		os.system('clear')
		print ("here is your current team")
		print ("P    Name                S  MS C  E  A")
		for i in range(len(ourteam)):
			for j in range(len(ourteam[i])):
				print(ourteam[i][j], end=' ')
			print()

		input("Press a button to continue")
		#playertodelete=intselect3
		#enoughcapital=0

	return (firstroundthisyear,secondroundthisyear,thirdoroundthisyear,playerstobuy,ourteam,intselect3,enoughcapital)

def sellplayerbuy(firstroundthisyear,secondroundthisyear,thirdoroundthisyear,valueofplayer,a2):

	thirdoroundthisyearneeded=0
	secondroundthisyearneeded=0
	firstroundthisyearneeded=0
	enoughcapital=0

	
	#pdb.set_trace()

	if valueofplayer =="1 Third Rounder":
		thirdoroundthisyearneeded=1                
	if valueofplayer =="1 Second Rounder":
		secondroundthisyearneeded=1
	if valueofplayer =="1 Second + 1 Third Rounder":
		thirdoroundthisyearneeded=1
		secondroundthisyearneeded=1
	if valueofplayer =="1 First + 1 Third Rounder":
		thirdoroundthisyeaneeded=1
		firstroundthisyearneeded=1
	if valueofplayer =="1 First + 1 Second Rounder":
		secondroundthisyearneeded=1   
		firstroundthisyearneeded=1
	if valueofplayer =="1 First + 1 Second + 1 Third Rounder":
		thirdoroundthisyearneeded=1
		secondroundthisyearneeded=1
		firstroundthisyearneeded=1
	if valueofplayer =="2 First + 1 Second + 1 Third Rounder":
		thirdoroundthisyearneeded=1
		secondroundthisyearneeded=1
		firstroundthisyearneeded=2              
	if valueofplayer =="2 First Rounders + 1 Second Round + Third Round":
		thirdoroundthisyearneeded=1
		secondroundthisyearneeded=1
		firstroundthisyearneeded=2                
	if valueofplayer =="3 First Rounders + 1 Second Round":
		secondroundthisyearneeded=1
		firstroundthisyearneeded=3
			 
	if valueofplayer =="2 First Rounders + 2 Second Round + 2 Third Rounders":
		thirdoroundthisyearneeded=2
		secondroundthisyearneeded=2
		firstroundthisyearneeded=2
	
	if valueofplayer =="2 Second Rounder":
		secondroundthisyearneeded=2
	
	if valueofplayer =="1 First Rounder":
		firstroundthisyearneeded=1
	
	if valueofplayer =="2 Third Rounder":
		thirdoroundthisyearneeded=2
	
	if valueofplayer =="1 First + 1 Second + 2 Third Rounder":
		thirdoroundthisyearneeded=2
		firstroundthisyearneeded=1
		secondroundthisyearneeded=1
		
	if valueofplayer =="1 First + 2 Second + 2 Third Rounder":
		thirdoroundthisyearneeded=2
		firstroundthisyearneeded=1
		secondroundthisyearneeded=2
		
		
		
	if (thirdoroundthisyearneeded <= thirdoroundthisyear) and (secondroundthisyearneeded <=secondroundthisyear) and (firstroundthisyearneeded <=firstroundthisyear):
#		print("Yes you have enough capital")
		enoughcapital=1
		thirdoroundthisyear=thirdoroundthisyear-thirdoroundthisyearneeded 
		secondroundthisyear=secondroundthisyear-secondroundthisyearneeded 
		firstroundthisyear=firstroundthisyear-firstroundthisyearneeded 

	else:
		os.system('clear')
		print ("You don't have enough captial")
#		print (a2)
		print ("\nThis is what you need:\n")
		print ("thirdoroundthisyearneeded",thirdoroundthisyearneeded)
		print ("secondroundthisyearneeded",secondroundthisyearneeded)
		print ("firstroundthisyearneeded",firstroundthisyearneeded)
		print ("\nAnd this is what you have\n")
		print ("\nthirdoroundthisyear",thirdoroundthisyear)
		print ("secondroundthisyear",secondroundthisyear)
		print ("firstroundthisyear",firstroundthisyear)
		input("Press a button to continue")
		enoughcapital=0

#	input("Wait")

	return(firstroundthisyear,secondroundthisyear,thirdoroundthisyear,enoughcapital)



def moveupdraft(firstroundthisyear,secondroundthisyear,thirdoroundthisyear):

	movetosecond=0	
	movetofirst=0
	notenoughcaptial=0

	os.system('clear')
	print ("First Round Value =3")
	print ("Second Round Value =1")
	print ("Third Round Value =0.5")
	print ("You need to equal the value to entice a team to move up...\n ")


	movetosecond=0.5*thirdoroundthisyear
	movetofirst=(0.5*thirdoroundthisyear)+(1*secondroundthisyear)
	print ("You have the following picks this year:")
	print ("\nFirst Round picks",firstroundthisyear)
	print ("Second Round picks",secondroundthisyear)
	print ("Third Round picks",thirdoroundthisyear)

	if movetofirst >= 3:
		print("\nYou have enought points to move up to the first round\n")
		mud=input("Do you want to swap your 2nd/3rd round picks to move up and get another first round pick (y)")
		if mud =="y":
		# doing maths to work out how much to take of each round to make up the 3
			firstroundthisyear=firstroundthisyear+1
			if secondroundthisyear >=2:
				secondroundthisyear=secondroundthisyear-2
				thirdoroundthisyear=thirdoroundthisyear-1
			elif secondroundthisyear ==1:
				secondroundthisyear=secondroundthisyear-1
				thirdoroundthisyear=thirdoroundthisyear-2
			else:
				thirdoroundthisyear=thirdoroundthisyear-6
			input("\nDraft picks swapped,Press a button to continue")
	else:
		notenoughcaptial=notenoughcaptial+1
	if movetosecond >=1:
		print("\nYou have enought points to move up to the second round\n")
		mud=input("Do you want to swap your 3rd round picks to move up and get another second round pick (y)")
		if mud =="y":
		# doing maths to work out how much to take of each round to make up the 3
			secondroundthisyear=secondroundthisyear+1
			thirdoroundthisyear=thirdoroundthisyear-2
			input("\nDraft picks swapped,Press a button to continue")

	else:
		notenoughcaptial=notenoughcaptial+1
	
	if notenoughcaptial==2:
		print("\nYou do not have enought draft captial to move up the draft yet")
		input("\nPress a button to continue")



	return (firstroundthisyear,secondroundthisyear,thirdoroundthisyear)



def sellplayer(ourteam,numofplayertoswap,firstroundthisyear,secondroundthisyear,thirdoroundthisyear,playerstoswap,season):

	replacementplayer1=[]
	whotoreplace=""
	field0=""
	firstroundnextyear=1
	secondroundnextyear=1
	thirdoroundnextyear=1

	while True:
		select2=input("\nWho do you want to Sell?(or press e to exit)... " )
		if select2=="e":
			whotoreplace="99"
			break
		if select2.isnumeric():
			if int(select2) in numofplayertoswap:
				break
			else:
				pass
	
			print ("Invalid option try again...\n")


# delete player from squad

        # work out the position of a player we need to create (i.e to same position as the player we are going to delete)
	#print ("whotpreplace",whotoreplace)
	
	if whotoreplace=="99":
		return (ourteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear)
#		exit
	else:
		whotoreplace=int(select2)

	positiontoreplace=""
	positiontoreplace1=ourteam[whotoreplace]
	positiontoreplace=positiontoreplace1[0]
        #iprint ("i am going to replace a..",positiontoreplace)

        # create player to add in
        # adding extra space in compare clause
	if positiontoreplace =="GK  ":
		replacementplayer=func_create_players.rn3(gk =1, defe =0, mid =0, ata =0, exp =4, maxskill =5, skill =5, skillpeak =0, char =10, maxage=34, minskill=2,weighted=0,minage=20,minrchar=2)
	elif positiontoreplace =="DEF ":
		replacementplayer=func_create_players.rn3(gk =0, defe =1, mid =0, ata =0, exp =4, maxskill =5, skill =5, skillpeak =0, char =10, maxage=34, minskill=2,weighted=0,minage=20,minrchar=2)
	elif positiontoreplace =="MID ":
		replacementplayer=func_create_players.rn3(gk =0, defe =0, mid =1, ata =0, exp =4, maxskill =5, skill =5, skillpeak =0, char =10, maxage=34, minskill=2,weighted=0,minage=20,minrchar=2)
	elif positiontoreplace =="ATA ":
		replacementplayer=func_create_players.rn3(gk =0, defe =0, mid =0, ata =1, exp =4, maxskill =5, skill =5, skillpeak =0, char =10, maxage=34, minskill=2,weighted=0,minage=20,minrchar=2)
	else:
		error1=input ("\nErr what the hell, i cannot work out what position to replace ...\n ")

        # get data in needed format
	replacementplayer1=replacementplayer[0]

# increment avaliable picks
########## i am looping through offers and using index as input from team loop
########## so chosing to replace num 24 when there are only 4 offers = error
########## so it needs a better way to match the 2 lists and the offer

	loopcount="-1"
	field9="no value yet"
	for i in range (len(playerstoswap)):
		loopcount=int(loopcount)+1
		for j in range (len(playerstoswap[i])):
			singlerecord = playerstoswap[loopcount]
			field0 = singlerecord[0]
			if int(field0) == int(whotoreplace):
				singlerecord9 = playerstoswap[loopcount]
				field9 =singlerecord[9]


        #print (field9


	firstroundthisyear,secondroundthisyear,thirdoroundthisyear=acceptedvalue(offered=field9,frty=firstroundthisyear,srty=secondroundthisyear,trty=thirdoroundthisyear)

#       playerchosen=ourteam[whotoreplace]
#       print (playerchosen)
#       offerchose=playerchose[9]
#       offerchose=playerchosen[8]
#       print (offerchose)


        # del and add player
	del ourteam[whotoreplace]
	ourteam.insert(whotoreplace, (replacementplayer1))

	os.system('clear')
	print ("Thanks for doing business with me, Swap done...i have given you one of my worse players!")
	avaliablepicks(firstroundthisyear,secondroundthisyear,thirdoroundthisyear)
	print ("\nHere is your new look squad\n")

# confirm who is int team
	print ("P    Name                S  MS C  E  A")
	for i in range(len(ourteam)):
		for j in range(len(ourteam[i])):
			print(ourteam[i][j], end=' ')
		print()

	input("\nPlease press a button to continue")
	return (ourteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear)


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







def offervalue(value1):

	if value1 ==1:
		offer1 ="1 Third Rounder"
	if value1 ==11:
		offer1 ="1 Second Rounder"
	if value1 ==2:
		offer1 ="1 Second + 1 Third Rounder"
	if value1 ==3:
		offer1 = "1 First + 1 Third Rounder"
	if value1 ==4:
		offer1 = "1 First + 1 Second Rounder"
	if value1 ==5:
		offer1 = "1 First + 1 Second + 1 Third Rounder"
	if value1 ==6:
		offer1 = "2 First + 1 Second + 1 Third Rounder"
	if value1 ==7:
		offer1 = "2 First Rounders + 1 Second Round + Third Round"
	if value1 ==8:
		offer1 = "3 First Rounders + 1 Second Round"
	if value1 ==9:
		offer1 = "2 First Rounders + 2 Second Round + 2 Third Rounders"
	if value1 ==12:
		offer1 = "2 Second Rounder"
	if value1 ==13:
		offer1 = "1 First Rounder"
	if value1 ==14:
		offer1 = "2 Third Rounder"
	if value1 ==15:
		offer1 = "1 First + 1 Second + 2 Third Rounder"
	if value1 ==16:
		offer1 = "1 First + 2 Second + 2 Third Rounder"

	return offer1



def acceptedvalue(offered,frty,srty,trty):

	#import create
	
	firstroundthisyear=frty
	secondroundthisyear=srty	
	thirdoroundthisyear=trty
	firstroundnextyear=1	
	secondroundnextyear=1
	thirdoroundnextyear=1

	if offered == "1 Third Rounder":
		thirdoroundthisyear=trty+1
	if offered == "1 Second Rounder":
		secondroundthisyear=srty+1
	if offered == "1 Second + 1 Third Rounder":
		thirdoroundthisyear=trty+1
		secondroundthisyear=srty+1
	if offered == "1 First + 1 Second Rounder":
		secondroundthisyear=srty+1
		firstroundthisyear=frty+1
	if offered == "1 First + 1 Third Rounder":
		firstroundthisyear=frty+1
		thirdoroundthisyear=trty+1
	if offered == "1 First + 1 Second + 1 Third Rounder":
		firstroundthisyear=frty+1
		secondroundthisyear=srty+1
		thirdoroundthisyear=trty+1
	if offered == "2 First + 1 Second + 1 Third Rounder":
		firstroundthisyear=frty+2
		secondroundthisyear=srty+1
		thirdoroundthisyear=trty+1
	if offered == "2 First Rounders + 1 Second Round + Third Round":
		firstroundthisyear=frty+2
		secondroundthisyear=srty+1
		thirdoroundthisyear=trty+1
	if offered == "3 First Rounders + 1 Second Round":
		firstroundthisyear=frty+3
		secondroundthisyear=srty+1

	return firstroundthisyear,secondroundthisyear,thirdoroundthisyear



def avaliablepicks(firstroundthisyear,secondroundthisyear,thirdoroundthisyear):
	print ("\nFirst Round Picks avaliable this Year",firstroundthisyear)
	print ("Second Round Picks avaliable this Year",secondroundthisyear)
	print ("Third Round Picks avaliable this Year",thirdoroundthisyear)
	#print ("First Round Picks avaliable Next Year",firstroundnextyear)
	#print ("Second Round Picks avaliable Next Year",secondroundnextyear)
	#print ("Third Round Picks avaliable Next Year",thirdoroundnextyear)
	print ("")

############## player offer

def sell_player(ourteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear,draft1,season):

	draftfound=0
	#global	playersavliable
	playersavliable=[]
	randomnum1=random.randint(0,1)
	ffc=random.randint(1,2)

	while True:
		#pdb.set_trace()
		global	playersavliable


	#firstroundthisyear=1
	#secondroundthisyear=1
	#thirdoroundthisyear=1
	#firstroundnextyear=1
	#secondroundnextyear=1
	#thirdoroundnextyear=1
		draftfound=draftfound+1
		os.system('clear')
		print ("In this Section you will have offers for your more highley rated players")
		print ("##################")

		avaliablepicks(firstroundthisyear,secondroundthisyear,thirdoroundthisyear)

		######################## set variables
		#print ("We have intrest in exchanging for these players\n")
		incrmentalnum=-1
		teamchar=0
		teamexp=0
		teamage=0
		playerstoswap=[]
		numofplayertoswap=[]
	
	#	playersavliable=[]
		playerstobuy=[]

		#########
	
		print ("Your Scout as mentioned these players are avaliable to swap for:\n")
	#	pdb.set_trace()
		if draftfound==1:
			#playersavliable=func_create_players.rn3(gk =5, defe =5, mid =5, ata =5, exp =4, maxskill =23, skill =23, skillpeak =0, char =10, maxage=34, minskill=15,weighted=0,minage=23,minrchar=5)
			randomgk=random.randint(6,8)
			randomdef=random.randint(6,10)
			randommid=random.randint(6,10)
			randomata=random.randint(6,8)
			if season < 4:
				playersavliable=func_create_players.rn3(gk=randomgk, defe=randomdef, mid=randommid, ata=randomata, exp =4, maxskill =24, skill =24, skillpeak =0, char =10, maxage=34, minskill=15,weighted=0,minage=20,minrchar=5)
			elif season <8:
				playersavliable=func_create_players.rn3(gk=randomgk, defe=randomdef, mid=randommid, ata=randomata, exp =4, maxskill =24, skill =24, skillpeak =0, char =10, maxage=33, minskill=16,weighted=0,minage=20,minrchar=6)
			elif season <12:
				playersavliable=func_create_players.rn3(gk=randomgk, defe=randomdef, mid=randommid, ata=randomata, exp =4, maxskill =24, skill =24, skillpeak =0, char =10, maxage=33, minskill=17,weighted=0,minage=20,minrchar=7)
			else:
				playersavliable=func_create_players.rn3(gk=randomgk, defe=randomdef, mid=randommid, ata=randomata, exp =4, maxskill =24, skill =24, skillpeak =0, char =10, maxage=33, minskill=17,weighted=0,minage=19,minrchar=8)
		mylog.fmlog(detail=str(("Who is avaliable to buy ", playersavliable)), verbosity=11)
	
		for i in range(len(playersavliable)):
				playerfound=0
				playerfoundscore=0
	#                       masterplayersfound=0
			#	if incrmentalnum==0:
		#			incrmentalnum=1
				incrmentalnum=1+incrmentalnum
				incrementalnumwp="{:<2}".format(incrmentalnum)
				singlerecord = playersavliable[incrmentalnum]

				position1=singlerecord[0]
				name1=singlerecord[1]
				name2=singlerecord[2]
				gfield4skill=int(singlerecord[3])
				maxskill=int(singlerecord[4])
				char=int(singlerecord[5])
				charformated="{:<2}".format(char)
				experience=int(singlerecord[6])
				experienceformated="{:<2}".format(experience)
				age=int(singlerecord[7])
				ageformated="{:<3}".format(age)

				if (age < 24):
					if char > 6:
						if 17 <=  gfield4skill < 20:
							playerfound=1
							playerfoundscore=4
							offer2=offervalue(4)
							masterplayersfound=1
						elif 20 <=  gfield4skill < 23:
							playerfound=1
							playerfoundscore=6
							offer2=offervalue(6)
							masterplayersfound=1
						elif 23 <=  gfield4skill < 25:
							playerfound=1
							playerfoundscore=16
							offer2=offervalue(16)
							masterplayersfound=1
						elif gfield4skill >= 25:
							playerfound=1
							playerfoundscore=16
							offer2=offervalue(16)
							masterplayersfound=1

						else:
							playerfound=1
							playerfoundscore=11
							offer2=offervalue(11)
							masterplayersfound=1
					else:
					#	ffc=random.randint(1,2)
						playerfound=1
						playerfoundscore=2
						offer2=offervalue(2)
						masterplayersfound=1
						


				elif age < 27:
					if char > 6:
						if 17 <=  gfield4skill < 20:
							playerfound=1
							playerfoundscore=3
							offer2=offervalue(3)
							masterplayersfound=1
						elif 20 <=  gfield4skill < 23:
							playerfound=1
							playerfoundscore=4
							offer2=offervalue(4)
							masterplayersfound=1
						elif 23 <=  gfield4skill < 25:
							playerfound=1
							playerfoundscore=15
							offer2=offervalue(15)
							masterplayersfound=1
						elif gfield4skill >= 25:
							playerfound=1
							playerfoundscore=15
							offer2=offervalue(15)
							masterplayersfound=1

						else:
							playerfound=1
							playerfoundscore=1
							offer2=offervalue(1)
							masterplayersfound=1
					else:
						playerfound=1
						playerfoundscore=14
						offer2=offervalue(14)
						masterplayersfound=1


				elif age < 30:
					if char >6:
						if 17 <=  gfield4skill < 20:
							playerfound=1
							playerfoundscore=13
							offer2=offervalue(13)
							masterplayersfound=1
						elif 20 <=  gfield4skill < 23:
							playerfound=1
							playerfoundscore=3
							offer2=offervalue(3)
							masterplayersfound=1
						elif 23 <=  gfield4skill < 25:
							playerfound=1
							playerfoundscore=4
							offer2=offervalue(4)
							masterplayersfound=1
						elif gfield4skill >= 25:
							playerfound=1
							playerfoundscore=5
							offer2=offervalue(5)
							masterplayersfound=1

						else:
							playerfound=1
							playerfoundscore=11
							offer2=offervalue(11)
							masterplayersfound=1
					else:
						playerfound=1
						playerfoundscore=14
						offer2=offervalue(14)
						masterplayersfound=1

				elif age < 32:
					if char >6:
						if 17 <=  gfield4skill < 20:
							playerfound=1
							playerfoundscore=11
							offer2=offervalue(11)
							masterplayersfound=1
						elif 20 <=  gfield4skill < 23:
							playerfound=1
							playerfoundscore=12
							offer2=offervalue(12)
							masterplayersfound=1
						elif 23 <=  gfield4skill < 25:
							playerfound=1
							playerfoundscore=12
							offer2=offervalue(12)
							masterplayersfound=1
						elif gfield4skill >= 25:
							playerfound=1
							playerfoundscore=13
							offer2=offervalue(13)
							masterplayersfound=1

						else:
							playerfound=1
							playerfoundscore=11
							offer2=offervalue(11)
							masterplayersfound=1
					else:
						playerfound=1
						playerfoundscore=14
						offer2=offervalue(14)
						masterplayersfound=1


				elif age < 34:
					if char >6:
						if 17 <=  gfield4skill < 20:
							playerfound=1
							playerfoundscore=1
							offer2=offervalue(1)
							masterplayersfound=1
						if 20 <=  gfield4skill < 23:
							playerfound=1
							playerfoundscore=14
							offer2=offervalue(14)
							masterplayersfound=1
						if 23 <=  gfield4skill < 25:
							playerfound=1
							playerfoundscore=14
							offer2=offervalue(14)
							masterplayersfound=1
						if gfield4skill >= 25:
							playerfound=1
							playerfoundscore=2
							offer2=offervalue(2)
							masterplayersfound=1

						else:
							playerfound=1
							playerfoundscore=1
							offer2=offervalue(1)
							masterplayersfound=1
					else:
						playerfound=1
						playerfoundscore=1
						offer2=offervalue(1)
						masterplayersfound=1

				else:
					#randomnum1=random.randint(0,1)
					if randomnum1==0:
						ffchance=14
					else:
						ffchance=11
								
					playerfound=1
					playerfoundscore=int(ffchance)
					offer2=offervalue(int(ffchance))
					masterplayersfound=1
					

				if playerfound == 1:
					playerstobuy.append ([incrementalnumwp,position1,name1,name2,gfield4skill,maxskill,charformated,experienceformated,ageformated,offer2])
					numofplayertoswap.append (int(incrementalnumwp))
					playerfound = 0
					playerfoundscore=0



		print ("B  P    Name                S  MS C  E  A   Offer")
		for i in range(len(playerstobuy)):
			for j in range(len(playerstobuy[i])):
				print(playerstobuy[i][j], end=' ')
			print()


		incrmentalnum=-1
		teamchar=0
		teamexp=0
		teamage=0
		playerstoswap=[]
		numofplayertoswap=[]

#		playersavliable=[]
#		playerstobuy=[]


		print ("\nOpposition teams have intrest in exchanging for these players in your squad:\n")


#playerfound=0

# looping through each player and valuing each player to determine draft value

# based on following table 
#	24	27	30	34		Age
#17	3	2	1	1		
#20	4	3	2	1		
#23	5	4	3	2		
#25	7	5	4	3		
#Skill			

# and value of those picks =
#       Round   Value
#	1	3
#	2	1
#	3	0.5

# so a 24 year old with skill of 25 would get a value of 7
# which would mean an offer of 2 1st Rounders and a second Round


		masterplayersfound=0
			

		for i in range(len(ourteam)):
				playerfound=0
				playerfoundscore=0
#				masterplayersfound=0

				incrmentalnum=1+incrmentalnum
				incrementalnumwp="{:<2}".format(incrmentalnum)
				singlerecord = ourteam[incrmentalnum]
                
				position1=singlerecord[0]
				name1=singlerecord[1]
				name2=singlerecord[2]
				gfield4skill=int(singlerecord[3])
				maxskill=int(singlerecord[4])
				char=int(singlerecord[5])
				charformated="{:<2}".format(char)
				experience=int(singlerecord[6])
				experienceformated="{:<2}".format(experience)
				age=int(singlerecord[7])
				ageformated="{:<3}".format(age)
		
				if (char > 6) and (age < 24):
					if 17 <=  gfield4skill < 20:
						playerfound=1
						playerfoundscore=3
						offer2=offervalue(3)
						masterplayersfound=1
					if 20 <=  gfield4skill < 23:
						playerfound=1
						playerfoundscore=4
						offer2=offervalue(4)
						masterplayersfound=1
					if 23 <=  gfield4skill < 25:
						playerfound=1
						playerfoundscore=5
						offer2=offervalue(5)
						masterplayersfound=1
					if gfield4skill >= 25:
						playerfound=1
						playerfoundscore=7
						offer2=offervalue(7)
						masterplayersfound=1

				
				elif (char > 6) and (age < 27):
					if 17 <=  gfield4skill < 20:
						playerfound=1
						playerfoundscore=2
						offer2=offervalue(2)
						masterplayersfound=1
					if 20 <=  gfield4skill < 23:
						playerfound=1
						playerfoundscore=3
						offer2=offervalue(3)
						masterplayersfound=1
					if 23 <=  gfield4skill < 25:
						playerfound=1
						playerfoundscore=4
						offer2=offervalue(4)
						masterplayersfound=1
					if gfield4skill >= 25:
						playerfound=1
						playerfoundscore=5
						offer2=offervalue(5)
						masterplayersfound=1

				elif (char > 6) and (age < 30):
					if 17 <=  gfield4skill < 20:
						playerfound=1
						playerfoundscore=1
						offer2=offervalue(11)
						masterplayersfound=1
					if 20 <=  gfield4skill < 23:
						playerfound=1
						playerfoundscore=2
						offer2=offervalue(2)
						masterplayersfound=1
					if 23 <=  gfield4skill < 25:
						playerfound=1
						playerfoundscore=3
						offer2=offervalue(3)
						masterplayersfound=1
					if gfield4skill >= 25:
						playerfound=1
						playerfoundscore=4
						offer2=offervalue(4)
						masterplayersfound=1


				elif (char > 6) and (age < 34):
					if 17 <=  gfield4skill < 20:
						playerfound=1
						playerfoundscore=1
						offer2=offervalue(1)
						masterplayersfound=1
					if 20 <=  gfield4skill < 23:
						playerfound=1
						playerfoundscore=1
						offer2=offervalue(1)
						masterplayersfound=1
					if 23 <=  gfield4skill < 25:
						playerfound=1
						playerfoundscore=11
						offer2=offervalue(11)
						masterplayersfound=1
					if gfield4skill >= 25:
						playerfound=1
						playerfoundscore=3
						offer2=offervalue(3)
						masterplayersfound=1

				if playerfound == 1:
#                     print (name1)
					playerstoswap.append ([incrementalnumwp,position1,name1,name2,gfield4skill,maxskill,charformated,experienceformated,ageformated,offer2])
					numofplayertoswap.append (int(incrementalnumwp))
					playerfound = 0
					playerfoundscore=0

		print ("B=Player to buy, P=Position,S=Skill,MS=Max Skill,C=Character,E=Experience,A=Age")
		print ("")



		offernumber=0
		efound=0
		bfound=0
		sfound=0
		mfound=0
		dfound=0
		ffound=0
		timespressed=0
#	pdb.set_trace()
		if masterplayersfound == 0:
			print("No players good enough :( ")
		#return
		
		else:
			print ("B  P    Name                S  MS C  E  A   Offer")
			for i in range(len(playerstoswap)):
				offernumber=offernumber+1
				for j in range(len(playerstoswap[i])):
					print(playerstoswap[i][j], end=' ')
				print()
	
	        ### Error check users input is a number


		while True:
				select1=input("\nWhat do you want to do? ... \n\ne to Exit this section and start with the first avaliable round of the draft(presuming you have picks-if not the new season will start)\nr for a team/player report\nb for buy a player your Scout has found \ns for sell one of your players for extra draft picks\nm Move up draft  \nd Move down draft\nf Feedback of your team (from the end of the previous season)\n1 Scout first round\n" )

				
				if select1 =="":
					break
				if select1=="1":
					scoutthedraft(draft1)
					break
				if select1 =="e":
					efound=1
					break
				if select1 =="f":
					mylog.fmlog(detail=str(("f hit on menu")), verbosity=30)
					ffound=1
					timespressed=timespressed+1
					# immport here as to high and log.txt hasn't been created
					#if timespressed==1:
					#import func_analsyispicks
					#func_analsyispicks()
#					os.system(./func_analsyispicks.py)
					subprocess.call("python3 func_analsyispicks.py", shell=True)
					break
				if select1 =="d":
					dfound=1
					firstroundthisyear,secondroundthisyear,thirdoroundthisyear=movedowndraft(firstroundthisyear,secondroundthisyear,thirdoroundthisyear)
					break
				if select1 =="r":
					teamreport1(createteam=ourteam,printto="yp")
					break
				if select1 =="b":
					
					mylog.fmlog(detail=str(("playerstobuy_before_Work ", playerstobuy)), verbosity=11)

					firstroundthisyear,secondroundthisyear,thirdoroundthisyear,playerstobuy,ourteam,playertodelete,enoughcapital=buypplayer (firstroundthisyear,secondroundthisyear,thirdoroundthisyear,playerstobuy,ourteam)
					# getting messy and painful trying to delete the picked player so he doesn't show up again
					#pdb.set_trace()
#					playertodelete=int(playertodelete-1)
						
					try:
						#del playerstobuy[playertodelete]
						if enoughcapital ==1:
							del playersavliable[playertodelete]
					except:
						print ("\ni errored dropping into debug more...\n")
						print ("playertodeletenumber",playertodelete)
						print ( "playertodelete-list",playertodelete)
						print ( "playersavaliable-list",playersavliable)
						pdb.set_trace()
#					del playersavliable[playertodelete]
					mylog.fmlog(detail=str(("playerstobuy_after_Work ", playerstobuy)), verbosity=11)
						
					bfound=1
					#pdb.set_trace()
					break
				if select1 =="m":
					mfound=1
					firstroundthisyear,secondroundthisyear,thirdoroundthisyear=moveupdraft(firstroundthisyear,secondroundthisyear,thirdoroundthisyear)
					break
				if select1 =="s":
					if masterplayersfound == 0:
						input ("No players good enough to swap, press enter to get back to the main menu")
						break
					else:
						os.system('clear')
						print ("O  P    Name                S  MS C  E  A   Offer")
						for i in range(len(playerstoswap)):
							offernumber=offernumber+1
							for j in range(len(playerstoswap[i])):
								print(playerstoswap[i][j], end=' ')
							print()

						sfound=1
				#print ("S found")
						ourteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear=sellplayer(ourteam=ourteam,numofplayertoswap=numofplayertoswap,firstroundthisyear=firstroundthisyear,secondroundthisyear=secondroundthisyear,thirdoroundthisyear=thirdoroundthisyear,playerstoswap=playerstoswap,season=season)
						break
		if efound==1:
			break
		else:
			continue
#	if bfound==1:
#		continue
			

	return ourteam,firstroundthisyear,secondroundthisyear,thirdoroundthisyear






