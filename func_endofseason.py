#!/usr/bin/python3.4

import random
import  mylog
import pdb


#mylog.fmlog(detail=str(("GoalKeeper Score ", gk)), verbosity=1)


def changes(ourteam,playoffexppoints,seasonnumber):
	
	mylog.fmlog(detail=str(("playoffexppoints just begening of script ", playoffexppoints)), verbosity=12)
#	playoffexppoints=0
	incrmentalnum=-1
	veryold=random.randint (30,34)
	verygoodchar=random.randint (8,9)
	#was 1,4
	verypoorchar=random.randint (5,7)
	averagechar=random.randint (7,8)
	changes=""
	changesp=""
	changesn=""
	changesms=""
	pointslostpadding=""


	for i in range(len(ourteam)):

##### loop through players and work out the + and - scores based on char & age (+ maybe a few more later)
		incrmentalnum=1+incrmentalnum
		singlerecord = ourteam[incrmentalnum]
#		mylog.fmlog(detail=str(("Player before end of season ",seasonnumber ,singlerecord)), verbosity=13)

		ageforskills=int(singlerecord[7])
		charforskills=int(singlerecord[5])
		pluspoints=0
		negativepoints=0
		randomnumberlskillincrease = random.randint (0,4)
#		print (randomnumberlskillincrease)
		veryrandomnumberlskillincrease = random.randint (0,25)
#		print (veryrandomnumberlskillincrease)

		if ageforskills > veryold:
			negativepoints=negativepoints+10
		elif ageforskills >30:
			if charforskills >= int(verygoodchar):
				negativepoints=negativepoints+2
			elif charforskills <= verypoorchar:
				negativepoints=negativepoints+6
			else:
				negativepoints=negativepoints+4
		elif ageforskills < 21:
			if charforskills >= verygoodchar:
				pluspoints=pluspoints+6
			elif charforskills <= verypoorchar:
				pluspoints=pluspoints+1
			else:
				pluspoints=pluspoints+4
		elif ageforskills < 24:
			if charforskills >= verygoodchar:
				pluspoints=pluspoints+4
			elif charforskills <= verypoorchar:
				pluspoints=pluspoints+1
			else:
				pluspoints=pluspoints+2
		else:
			if charforskills >= verygoodchar:
				pluspoints=pluspoints+2
			elif charforskills <= verypoorchar:
				pluspoints=pluspoints+1
			else:
				pluspoints=pluspoints+2
		# added a degree of luck for a young player to boost skill + 2
		if (ageforskills <= 24) and (randomnumberlskillincrease >= 3) and (charforskills > 9) :
			pluspoints=pluspoints+15
		if (ageforskills <= 24) and (randomnumberlskillincrease >= 3) and (charforskills > 8) :
			pluspoints=pluspoints+7
		if (ageforskills < 24) and (veryrandomnumberlskillincrease > 24) and (charforskills > 7) :
			pluspoints=pluspoints+7
		if ageforskills > 24 and (veryrandomnumberlskillincrease > 22):
			negativepoints=negativepoints+5
		if ageforskills > 24 and (veryrandomnumberlskillincrease < 8):
			negativepoints=negativepoints+3
		randomloss=random.randint (6,9)
		if charforskills <= averagechar:
			negativepoints=negativepoints+int(randomloss)
			






##### work out scores for max skill increase

		maxskillpoints=0
		playersmaxskill=int(singlerecord[4])
		playercurrentskill=int(singlerecord[3])
		playersexperience=int(singlerecord[6])
		if ageforskills > veryold:
			maxskillpoints=maxskillpoints-4
		elif ageforskills >30:
			maxskillpoints=maxskillpoints-2
		else: 
			maxskillpoints=maxskillpoints+2
		if charforskills  > 8:
			maxskillpoints=maxskillpoints+2
		elif charforskills > 5:
			maxskillpoints=maxskillpoints+1
		else:
			maxskillpoints=maxskillpoints+0
		if playercurrentskill > 15:
			maxskillpoints=maxskillpoints+1
		if playersexperience > 10:
			maxskillpoints=maxskillpoints+2
		elif playersexperience > 5:
			maxskillpoints=maxskillpoints+1
		else:
			maxskillpoints=maxskillpoints+0
		if playersmaxskill-playercurrentskill < 2:
			maxskillpoints=maxskillpoints+3
		#stop anyone getting over 20 hack
#		if playersmaxskill == 20:
#			maxskillpoints=0
#		if playercurrentskill == 20:		
#			pluspoints=0


		
		

			
			



# insert if winning season...

		
# upgrade/downgrade skills
#### based on earlier worked out +- scores
#### postive score v random number in 0-8 range = increase in skills
#### for every negative points try a random number in 0-1 range (so 50:50) and if = 1 you lose a point
#### a if skill is less than 2 has been inserted to stop negative values

		randomnumber = random.randint (0,8)
		randomnumberms = random.randint (0,15)
		name =""
		nposition=""
		pointsadded="0"
		if randomnumber <= pluspoints:
			skill=int(singlerecord[3])
			skillpadding=str(int(singlerecord[3]))
			skillpadding="{:<2}".format(skillpadding)
			if pluspoints > 10:
				singlerecord[3]="{:<2}".format(skill + 2)
#				if skill == 19:
				increasetext="+2"
#				else:
#					increasetext="+2"
			else:
				singlerecord[3]="{:<2}".format(skill + 1)
				increasetext="+1"
			name=singlerecord[1]+" "+singlerecord[2]
			nposition=singlerecord[0]
			age=singlerecord[7]
			newrecord=""
			newrecord= nposition+" "+name+" "+increasetext+" "+str(singlerecord[3])+" "+age+"\n"
			changesp=changesp+newrecord
			pointsadded="1"

			 
		if negativepoints == 0 or int(pointsadded) > 0:
			changes="1"

		else:
			count=0
			changed=0
			pointslost=0
			while ( negativepoints > count):
				count=count+1
				nrandomnumber = random.randint (0,1)
#				name=singlerecord[1]+singlerecord[2]
#				changesn=changesn+name+"\n"
				if nrandomnumber == 1:
					skill=int(singlerecord[3])
					if skill > 2: # stop a negative skill number and an infinte loop
						singlerecord[3]="{:<2}".format(skill - 1)
						changed=1
						pointslost=pointslost+1
			if changed == 1:
				name=singlerecord[1]+" "+singlerecord[2]
				pointslostpadding="{:<2}".format(pointslost)
				age=singlerecord[7]
				nposition=singlerecord[0]
				newline=""
				#newline=nposition+" "+name+" "+"-"+str(pointslost)+" "+str(singlerecord[3])+" " +age+"\n"
				newline=nposition+" "+name+" "+"-"+pointslostpadding+" "+str(singlerecord[3])+" " +age+"\n"
				changesn=changesn+newline
#max skill
		if randomnumberms <= maxskillpoints :
			currentms=int(singlerecord[4])
			currentmspadding=str(int(singlerecord[4])+1)
			currentmspadding="{:<2}".format(currentmspadding)
			singlerecord[4]="{:<2}".format(currentms + 1)
			namems=singlerecord[1]+" "+singlerecord[2]
			positionms=singlerecord[0]
			agems=singlerecord[7]
			newrecordms=""
                        #newrecordms= positionms+" "+namems+" "+"1"+" "+str(currentms+1)+" "+agems+"\n"
			newrecordms= positionms+" "+namems+" "+"+1"+" "+currentmspadding+" "+agems+"\n"
			#pdb.set_trace()
			changesms=changesms+newrecordms
			pointsadded="1"





# age +1, experience +1
		age=singlerecord[7]
		age='{}' .format (int(age)+1)
		singlerecord[7]="{:<2}".format(age)

		mylog.fmlog(detail=str(("playoffexppoints just before add ", playoffexppoints)), verbosity=12)
		experience=singlerecord[6]
		experience='{}' .format (int(experience)+playoffexppoints)
		singlerecord[6]="{:<2}".format(experience)
		mylog.fmlog(detail=str(("Player at end of season ",seasonnumber, singlerecord)), verbosity=13)

		

		

	



	return (ourteam,changesp,changesn,changesms)
