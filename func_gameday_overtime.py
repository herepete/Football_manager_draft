#!/usr/bin/python3.4
# this is used in working out who won a match in overtime
import random
import os
import mylog



#######################variables
bigdiff=70
smalldif=20
ourprevgoals=0
oppprevgoals=0

######################Clever stuff


def bat(ourgk,oppgk,ourdef,oppdef,ourmid,oppmid,ourata,oppata,ourchar,oppchar,ourexp,oppexp,ourprevgoals,oppprevgoals):

	mylog.fmlog(detail=str(("Ourprevgoals  ",ourprevgoals )), verbosity=3)
	mylog.fmlog(detail=str(("Opprevgoals  ",oppprevgoals )), verbosity=3)

# create scores
	ourdefscore=0	
	ourattackscore=0	
	oppdefscore=0	
	ourattackscore=0	
	oppattackscore=0	

# a slightly different team score caculation to increase effect of exp and char 
	ourattackscore=int(((ourdef*4)+(ourmid*8)+(ourata*6)+(ourexp/6)+(ourchar/3))/4.5)
	oppattackscore=int(((oppdef*4)+(oppmid*8)+(oppata*6)+(oppexp/6)+(oppchar/3))/4.5)
	ourdefscore=int(((ourgk*4)+(ourdef*8)+(ourmid*4)+(ourata*2)+(ourexp/6)+(ourchar/3))/4.5)
	oppdefscore=int(((oppgk*4)+(oppdef*8)+(oppmid*4)+(oppata*2)+(oppexp/6)+(oppchar/3))/4.5)
 
# our goals tally
	ourcomaprescore=0
	ourgoals=0
	oppgoals=0

	ourcomparescore=int(ourattackscore)+int(ourdefscore)
	mylog.fmlog(detail=str(("Our compare score  ",ourcomparescore )), verbosity=3)
	oppcomparescore=int(oppattackscore)+int(oppdefscore)
	mylog.fmlog(detail=str(("Opp compare score",oppcomparescore )), verbosity=3)
	ourrandomnumber=random.randint (1,ourcomparescore)
	mylog.fmlog(detail=str(("Our random number  ", ourrandomnumber )), verbosity=3)
	opprandomnumber=random.randint (1,oppcomparescore)
	mylog.fmlog(detail=str(("Opp random number ",opprandomnumber )), verbosity=3)
	difference1=abs(ourrandomnumber - opprandomnumber)
	mylog.fmlog(detail=str(("Difference in numbers ",difference1 )), verbosity=3)
	difference2=int(ourrandomnumber - opprandomnumber)

	if difference1 < 10:
		ourgoals=ourprevgoals
		oppgoals=oppprevgoals
		mylog.fmlog(detail=str(("Our Goals ",ourgoals )), verbosity=3)
		mylog.fmlog(detail=str(("Opp Goals ",oppgoals )), verbosity=3)
		

	elif difference2 >= 11:
		ourgoals=int(ourprevgoals+1)
		oppgoals=oppprevgoals
		mylog.fmlog(detail=str(("Our Goals ",ourgoals )), verbosity=3)
		mylog.fmlog(detail=str(("Opp Goals ",oppgoals )), verbosity=3)

	elif difference2 < 0:
		ourgoals=ourprevgoals
		oppgoals=int(oppprevgoals+1)
		mylog.fmlog(detail=str(("Our Goals ",ourgoals )), verbosity=3)
		mylog.fmlog(detail=str(("Opp Goals ",oppgoals )), verbosity=3)

	else:
		ourgoals=ourprevgoals
		oppgoals=oppprevgoals


	return ourgoals,oppgoals


