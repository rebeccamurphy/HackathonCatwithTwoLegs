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
'''
while i<10:
	state = functions.turn("PLAY")
	functions.addRecords(DBEUrecords,DBNArecords,DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state)
	i+=1
print WBEUrecords
print functions.rateofchange(WBEUrecords)

'''
while (i<10080):
        state = functions.turn("PLAY")
        functions.addRecords(DBEUrecords,DBNArecords,DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state)
        #if WBEUrecords[i] != WBEUrecords[ i-1] and i >=1:
        #        print i
        #        break
        turns = 20
        if (i %turns==0 and i !=0):
                print functions.rateofchange(WBEUrecords[i-turns:i], turns)
                if (functions.rateofchange(WBEUrecords[i-turns:i], turns) > 180 * state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NodeCount']):
                        functions.makechange([1,0,0], [0,0,0], [0,0,0])
                elif (functions.rateofchange(WBEUrecords[i-turns:i], turns) <180 * state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NodeCount'] and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NodeCount'] != 1):
                        functions.makechange([-1,0,0], [0,0,0], [0,0,0])
                print functions.rateofchange(WBEUrecords[i-turns:i], turns)
                if (functions.rateofchange(WBNArecords[i-turns:i], turns) > 180 * state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NodeCount']):
                        functions.makechange([0,1,0], [0,0,0], [0,0,0])
                elif (functions.rateofchange(WBNArecords[i-turns:i], turns) <180 * state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NodeCount'] and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NodeCount'] != 1 ):
                        functions.makechange([0,-1,0], [0,0,0], [0,0,0])
        i+= 1

#print DBEUrecords these only start changing after 1000 turns.
#JVEUrecords takes 829 turns
#10,080

'''i=0
state = functions.turn("PLAY")
print state
functions.addRecords(DBEUrecords,DBNArecords,DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state)
print WBEUrecords[0]
if WBEUrecords[0] > 180:
	print functions.makechange([1,0,0], [0,0,0], [0,0,0])
state = functions.turn("PLAY")
print state

state = functions.turn("PLAY")
print state'''


#and state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NodeCount'] !=