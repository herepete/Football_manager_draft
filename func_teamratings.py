#!/usr/bin/python3.4
import func_create_players
import os


####Functions
def scores(value):
                if value <= 5:
                        quality="Pub Quality"
                elif 6 <= value <= 10:
                        quality="Conference Quality"
                elif 11 <= value <= 13:
                        quality="Championship Quality"
                elif 14 <= value <= 15:
                        quality="Premier League Quality"
                elif 16 <= value <=18:
                        quality="Champions League Quality"
                else:
#                        print (value)
                        quality="World Class Quality"

                return quality

####formation
gk=1
d=4
m=4
s=2
printo="99"


def teams(gk,defe,mid,ata,createteam,printo):

	import mylog

	incrmentalnum=-1
	checkp="nty"
	gskillnum=0
	dskillnum=0
	mskillnum=0
	sskillnum=0
	teamchar=0
	teamexp=0
	teamage=0
	gkfinalscore=0
	deffinalscore=0
	midfinalscore=0
	atafinalscore=0
	expfinalscore=0
	charfinalscore=0
	gplayerrange=[]
	dplayerrange=[]
	mplayerrange=[]
	splayerrange=[]
	for i in range(len(createteam)):
		incrmentalnum=1+incrmentalnum
		singlerecord = createteam[incrmentalnum]
		field1pos=singlerecord[0]
		if field1pos =="GK  ":
			gfield4skill=int(singlerecord[3])
			gplayerrange.append(gfield4skill)
			gskillnum=gskillnum+gfield4skill
			teamchar=teamchar+int(singlerecord[5])
			teamexp=teamexp+int(singlerecord[6])
			teamage=teamage+int(singlerecord[7])
		if field1pos =="DEF ":
			dfield4skill=int(singlerecord[3])
			dplayerrange.append(dfield4skill)
			dskillnum=dskillnum+dfield4skill
			teamchar=teamchar+int(singlerecord[5])
			teamexp=teamexp+int(singlerecord[6])
			teamage=teamage+int(singlerecord[7])
		if field1pos =="MID ":
			mfield4skill=int(singlerecord[3])
			mplayerrange.append(mfield4skill)
			mskillnum=mskillnum+mfield4skill
			teamchar=teamchar+int(singlerecord[5])
			teamexp=teamexp+int(singlerecord[6])
			teamage=teamage+int(singlerecord[7])
		if field1pos =="ATA ":
			sfield4skill=int(singlerecord[3])
			splayerrange.append(sfield4skill)
			sskillnum=sskillnum+sfield4skill
			teamchar=teamchar+int(singlerecord[5])
			teamexp=teamexp+int(singlerecord[6])
			teamage=teamage+int(singlerecord[7])
	

	gplayerrange.sort(reverse=True)
	dplayerrange.sort(reverse=True)
	mplayerrange.sort(reverse=True)
	splayerrange.sort(reverse=True)

	if printo != checkp :
		print ("First 11 Scout Report")
		print ("##########\n")
	playerpositionts=-1

	rating=""
	sr=""
	for i in gplayerrange:
		playerpositionts=playerpositionts+1
		if gk > playerpositionts:
			gkfinalscore=gkfinalscore+i
		rating=gkfinalscore
		quality=""
		sr=scores(rating)
	if printo != checkp :
		print ("GoalKeeper Score (out of 20)",gkfinalscore,sr)

	playerpositionts=-1
	dkfinalscore=0
	rating=""
	sr=""




	for i in dplayerrange:
		playerpositionts=playerpositionts+1
		if d > playerpositionts:
			dkfinalscore=dkfinalscore+i
		rating=int(dkfinalscore/4)
		deffinalscore=rating
		sr=scores(rating)
	if printo != checkp :
		print ("Defence Score (out of 20)",rating,sr)

	playerpositionts=-1
	mkfinalscore=0
	rating=""
	sr=""

	for i in mplayerrange:
		playerpositionts=playerpositionts+1
		if m > playerpositionts:
			mkfinalscore=mkfinalscore+i
		rating=int(mkfinalscore/m)
		midfinalscore=rating
		sr=scores(rating)
	if printo != checkp :
		print ("Midfield Score (out of 20)",rating,sr)

	playerpositionts=-1
	skfinalscore=0
	rating=""
	sr=""


	for i in splayerrange:
		playerpositionts=playerpositionts+1
		if s > playerpositionts:
			skfinalscore=skfinalscore+i
		rating=int(skfinalscore/s)
		atafinalscore=rating
		sr=scores(rating)
	
	if printo != checkp :
		print ("Atacking Score (out of 20)",rating,sr)
		print ()
	
		print ("Team Details")
		print  ("###########\n")
	#add 1 to allow division
	incrmentalnum=incrmentalnum+1
	rating=int((teamchar/incrmentalnum)*2)
	charfinalscore=rating
	outof=incrmentalnum*10
	sr=scores(rating)
	if printo != checkp:
		print ("Total Team Characteur",teamchar)

	# *2 below didn't seem enough so * by 3
	rating=int((teamexp/incrmentalnum)*2)
	expfinalscore=rating
	sr=scores(rating)
	if printo != checkp :
		print ("Total Team Experience",teamexp)

	rating=int(teamage/incrmentalnum)
	avgage=rating
	#sr=scores(rating)
	if printo != checkp :
		print ("Average Age of team",avgage)
		print ()

	gkscore=gkfinalscore
	defscore=deffinalscore
	midscore=midfinalscore
	atascore=atafinalscore
	erating=expfinalscore
	eteamchar=charfinalscore


	
	mylog.fmlog(detail=str(("Gk Score ", gkfinalscore)), verbosity=1)
	mylog.fmlog(detail=str(("defe Score ", deffinalscore)), verbosity=1)
	mylog.fmlog(detail=str(("mid Score ", midfinalscore)), verbosity=1)
	mylog.fmlog(detail=str(("ata Score ", atafinalscore)), verbosity=1)
	mylog.fmlog(detail=str(("exp Score ", expfinalscore)), verbosity=1)
	mylog.fmlog(detail=str(("char Score ", charfinalscore)), verbosity=1)

	ourattackscore=int(((deffinalscore*4)+(midfinalscore*8)+(atafinalscore*6)+(teamexp/7)+(teamchar/4))/4.5)
	ourdefscore=int(((gkfinalscore*4)+(deffinalscore*8)+(midfinalscore*4)+(atafinalscore*2)+(teamexp/7)+(teamchar/4))/4.5)

	print ("Team Game day stats ")
	print ("#########\n")
	print ("Match Day Attack Score",ourattackscore)
	mylog.fmlog(detail=str(("total att Score ", ourattackscore)), verbosity=1)
	print ("Match Day Defense Score",ourdefscore)
	mylog.fmlog(detail=str(("total def Score ", ourdefscore)), verbosity=1)
	print ("")
	
	#return (gkscore,defscore,midscore,atascore,teamchar,rating,)	
	return (gkscore,defscore,midscore,atascore,teamchar,teamexp,avgage)	

