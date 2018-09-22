#!/usr/bin/python3

### import modules
import pdb
import os

### sort out variables
os.system('clear')

pdblog="0"
try:
	os.remove("stripped.log")
except:
	pass
lines=""


strippedlog=[]
countverb13=0

logname="log.txt"
currentteamnames=[]
found = 0

### definitions


def stripoutsinglequotes(input):

	input=str(input)
	input=input.replace("'","")

	return input

def stripoutbrackets(input1):

	input1=str(input1)
	input1=input1.replace("[","")
	input1=input1.replace("]","")

	return input1

def stripbrackets(input2):
	
	input2=str(input2)
	input2=input2.replace(")","")
	input2=input2.replace("(","")

	return input2

### get log
with open (logname) as f:
	lines= f.readlines()	

numoflines=len(lines)
#print ("number of lines in lines %s"%numoflines)


### loop through log
if pdblog=="2":
	pdb.set_trace()
try:
	for i in range(len(lines)):
	#for j in range(a):
		templine=""
		templine=(lines[i])
		countverb13=countverb13+1
		if "verbosity 13" in templine:
			strippedlog.append(templine)
		countverb13=countverb13+1
except:
	if pdb==1:
		pdb.set_trace()
			
			
### write out stipped log
#Write out initally used for understanding output
#print ()
#print ("number of loops of lines %s" %countverb13)
numofitemsinstrippedlog=len(strippedlog)
#print ("items in stripped log %s"%numofitemsinstrippedlog)
print("This will only show players at the end of their first season after training\nNo value under drafted means they were an orginal member of the team\n")
countstrippedlog=0
if pdb==1:
	pdb.set_trace()
for i in range (len(strippedlog)):
	f= open("stripped.log", "a")
	f.write(strippedlog[i])

###### start magic on log
### get season

for i in range(len(strippedlog)):
#	eachline=(strippedlog[i])
#	seasonfromline=eachline[60:63]
	lineintonewlist_s=strippedlog[i]
	lineintonewlist_s=lineintonewlist_s.split(',')
	season_s=(lineintonewlist_s[1])



#print ("Final - we are in season %s" %season_s)

print ("Current team...")
print ()
print (" P     Name                  C  A   S  OS DS Drafted            ")

### get players in the current season based on the highest season 
for i in range(len(strippedlog)):

	lineintonewlist=strippedlog[i]
	lineintonewlist=lineintonewlist.split(',')

	season=(lineintonewlist[1])
	season=str(season)
	season=season.replace("'","")

	position=(lineintonewlist[2])
	position=stripoutsinglequotes(position)
	position=stripoutbrackets(position)
	

	firstname=(lineintonewlist[3])
	firstname=stripoutsinglequotes(firstname)
	

	surname=(lineintonewlist[4])
	surname=stripoutsinglequotes(surname)
	
	skill=(lineintonewlist[5])
	skill=stripoutsinglequotes(skill)
	
	maxskill=(lineintonewlist[6])
	maxskill=stripoutsinglequotes(maxskill)
	
	char=(lineintonewlist[7])
	char=stripoutsinglequotes(char)
	
	exp=(lineintonewlist[8])
	exp=stripoutsinglequotes(exp)



	age=(lineintonewlist[9][2:4])

	# if last season matches current record print (i.e members of the current team)
	if season==season_s:
		#print(position,firstname,surname,skill,maxskill,char,exp,age,end="")
		print(position,firstname,surname,char,age,skill,end="")
		fullname=firstname+"  "+surname
		currentteamnames.append(fullname)
		#lets get draft value if it exists
		for i in range(len(lines)):
#			pdb.set_trace()
			templine1=(lines[i])
			searchterm1="verbosity 22"
			searchterm4="verbosity 9"
	
		
			# lots of hacking to remove space and commas
			searchterm2=firstname
			searchterm2=str(searchterm2)
			searchterm2=searchterm2.replace("'","")
			searchterm2=searchterm2.rstrip()
			searchterm2=searchterm2.lstrip()

			
			# lots of hacking to remove space and commas
			searchterm3=surname
			searchterm3=str(searchterm3)
			searchterm3=searchterm3.replace("'","")
			searchterm3=searchterm3.rstrip()
			searchterm3=searchterm3.lstrip()

			lastfewlinesoffield=templine1[-15:]
			if (searchterm1 in lastfewlinesoffield) and (searchterm2 in templine1) and (searchterm3 in templine1) :

			#hack again, list into string, strip out rubbish

				draftround=templine1.split(",")
				draftround= (draftround[1])
				draftround=str(draftround)
				draftround=draftround.replace('"',"")

				skillwhendrafted=templine1.split(",")
				skillwhendrafted=(skillwhendrafted[5])
				skillwhendrafted=str(skillwhendrafted)
				skillwhendrafted=skillwhendrafted.replace("'","")


				print (skillwhendrafted+" D "+draftround)
				found=1

			if (searchterm4 in lastfewlinesoffield) and (searchterm2 in templine1) and (searchterm3 in templine1) :
			#hack again, list into string, strip out rubbish


				#hack data from log to get it into a nice output putting into a few list with different seperators
				draftround1=templine1.split(",")
				draftround1= (draftround1[10])
				draftround1=draftround1.split("-")
				draftround1= (draftround1[0])
				draftround1=stripoutsinglequotes(draftround1)
				draftround1=stripoutbrackets(draftround1)
				draftround1=stripbrackets(draftround1)
				
				

				skillwhendrafted1=templine1.split(",")
				skillwhendrafted1=(skillwhendrafted1[5])
				skillwhendrafted1=str(skillwhendrafted1)
				skillwhendrafted1=skillwhendrafted1.replace("'","")

			#	pdb.set_trace()

				print (skillwhendrafted1+" S "+draftround1)
				found=1


		# if no value found start a new line
		if found==0:
			print ()
		else:
			found=0
print ("\n##################")
print ("P=Position")
print ("C=Current Char")
#print ("MS=Current Max skill")
#print ("E=Current Experience")
print ("A=Current Age")
print ("S=Current Skill")
print ("OS=Original Skill When drafted")
print ("DS=Draft/Scouted")
print ("Drafted=Orginal Value of player")

input("\nPress a button to continue")
