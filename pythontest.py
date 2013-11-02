import httplib, urllib, urllib2, requests, functions, json

DBEUrecords= []
DBNArecords= []
DBAPrecords= []
JVEUrecords=[]
JVNArecords=[]
JVAPrecords =[]
WBEUrecords=[]
WBNArecords=[]
WBAPrecords=[]

functions.turn("INIT")


#print functions.makechange([0,0,0], [0,0,0], [0,0,0])
# 
i=0
while (i<1000):
	state = functions.turn("PLAY")
	functions.addRecords(DBEUrecords,DBNArecords,DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state)
	#if WBEUrecords[i] != WBEUrecords[ i-1] and i >=1:
	#	print i
	#	break

	if (i  %25==0 and i !=0):
		print functions.rateofchange(WBNArecords[i-25:i])
		if (functions.rateofchange(WBNArecords[i-25:i]) > 1):
			functions.makechange([0,1,0], [0,0,0], [0,0,0])
		elif (functions.rateofchange(WBNArecords[i-25:i]) <1 and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NodeCount'] != 1):
			functions.makechange([0,-1,0], [0,0,0], [0,0,0])
	i+= 1

#print DBEUrecords these only start changing after 1000 turns.
#JVEUrecords takes 829 turns
#10,080
