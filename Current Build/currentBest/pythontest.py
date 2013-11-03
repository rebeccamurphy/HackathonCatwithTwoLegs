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

flag = 0
#print functions.makechange([0,0,0], [0,0,0], [0,0,0])
# 
i=0
while (True):
	state = functions.turn("PLAY")
	functions.addRecords(DBEUrecords,DBNArecords,DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state)
	#if WBEUrecords[i] != WBEUrecords[ i-1] and i >=1:
	#       print i
	#       break
	if(state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["AP"]['NodeCount'] > 0 or state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["EU"]['NodeCount'] > 0):
		if (i == 0):
			functions.makechange([0,0,0], [0,0,0], [0,1,0])
		elif (i == 5):
			functions.makechange([0,0,0], [0,0,0], [-1,0,-1])
	
	print state["ServerState"]['TurnNo']
	print state["ServerState"]['ProfitAccumulated']

	if (i  %9==0 and i !=0):
		#print functions.rateofchange(WBNArecords[i-8:i])
		if (functions.rateofchange(WBNArecords[i-9:i]) > 1):
			functions.makechange([0,1,0], [0,0,0], [0,0,0])
		elif (functions.rateofchange(WBNArecords[i-9:i]) < 1 and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NodeCount'] != 1):
			functions.makechange([0,-1,0], [0,0,0], [0,0,0])
		if (functions.rateofchange(WBEUrecords[i-9:i]) > 1):
			functions.makechange([1,0,0], [0,0,0], [0,0,0])
		elif (functions.rateofchange(WBEUrecords[i-9:i]) < 1 and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NodeCount'] != 1):
			functions.makechange([-1,0,0], [0,0,0], [0,0,0])
		if (functions.rateofchange(WBAPrecords[i-9:i]) > 1):
			functions.makechange([0,0,1], [0,0,0], [0,0,0])
		elif (functions.rateofchange(WBAPrecords[i-9:i]) < 1 and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["AP"]['NodeCount'] != 1):
			functions.makechange([0,0,-1], [0,0,0], [0,0,0])
	elif (i  %13==0 and i !=0):
		#print functions.rateofchange(JVNArecords[i-6:i])
		if (functions.rateofchange(JVNArecords[i-13:i]) > 1):
			functions.makechange([0,0,0], [0,1,0], [0,0,0])
		elif (functions.rateofchange(JVNArecords[i-13:i]) < 1 and state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["NA"]['NodeCount'] != 1):
			functions.makechange([0,0,0], [0,-1,0], [0,0,0])
		if (functions.rateofchange(JVEUrecords[i-13:i]) > 1):
			functions.makechange([0,0,0], [1,0,0], [0,0,0])
		elif (functions.rateofchange(JVEUrecords[i-13:i]) < 1 and state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["EU"]['NodeCount'] != 1):
			functions.makechange([0,0,0], [-1,0,0], [0,0,0])
		if (functions.rateofchange(JVAPrecords[i-13:i]) > 1):
			functions.makechange([0,0,0], [0,0,1], [0,0,0])
		elif (functions.rateofchange(JVAPrecords[i-13:i]) < 1 and state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["AP"]['NodeCount'] != 1):
			functions.makechange([0,0,0], [0,0,-1], [0,0,0])
	elif (i  %15==0 and i !=0):
		if (functions.rateofchange(DBNArecords[i-15:i]) > 1):
			functions.makechange([0,0,0], [0,0,0], [0,1,0])
		elif (functions.rateofchange(DBNArecords[i-15:i]) < 1 and state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["NA"]['NodeCount'] != 1):
			functions.makechange([0,0,0], [0,0,0], [0,-1,0])
	
	if (state["ServerState"]['ProfitAccumulated'] >= 75000 and flag == 0):
			functions.makechange2()
			flag = 1
	
	i+= 1

#print DBEUrecords these only start changing after 1000 turns.
#JVEUrecords takes 829 turns
#10,080
