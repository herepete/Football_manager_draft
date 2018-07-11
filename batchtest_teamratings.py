#!/usr/bin/python3.4
import func_teamratings
import func_create_players

testteam=func_create_players.rn3 (gk =3, defe =7, mid =7, ata =5, exp =10, maxskill =19, skill =19, skillpeak =0, char =10, maxage=21, minskill=15,weighted=0,minage=18)

#gkscore,defscore,midscore,atascore,teamchar,ratinggkscore,defscore,midscore,atascore,teamchar,rating=func_teamratings.teams(gk=1,defe=2,mid=3,ata=4,createteam=testteam,printo="nty")
#gkscore,defscore,midscore,atascore,teamchar,rating=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=testteam, printo="nty")
gkscore,defscore,midscore,atascore,teamchar,rating=func_teamratings.teams(gk =1, defe=2, mid=3, ata=4, createteam=testteam, printo="abc")


