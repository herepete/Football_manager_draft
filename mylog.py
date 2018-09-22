#!/usr/bin/python3.4


# creating my own logging as the built in stuff seems overley complicated
# this is all thats need to get it to run
#
'''
#!/usr/bin/python3.4
import  mylog

text="i have worked"
v123=1

mylog.fmlog(detail=text, verbosity=v123)
mylog.fmlog(detail=str(("GoalKeeper Score ", gk)), verbosity=1)

'''




import inspect

def fmlog(detail,verbosity):

#variables
        import os
        import sys
        frame_records = inspect.stack()[1]
        b=calling_module = inspect.getmodulename(frame_records[1])
        from datetime import datetime
        file = open("log.txt","a")
        n = datetime.now()

###writing
        file.write(str(n))
        file.write (" -")
        file.write(detail)
        file.write (" -")
        file.write (b)
        file.write (" -")
        file.write (" verbosity ")
        file.write (str(verbosity))
        file.write("\n")
        file.close()
