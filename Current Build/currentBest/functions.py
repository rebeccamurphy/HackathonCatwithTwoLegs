import httplib, urllib, urllib2, requests, json

url = 'http://hermes.wha.la/api/hermes'
headers = {'content-type': 'application/json'}

datainit = {
        'Command': 'INIT',
        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None,
}

start = {
        'Command': 'PLAY',
        'Token' : '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None
        }

def turn(kind):
	if kind == 'INIT':
		response = requests.post(url, data =json.dumps(datainit), headers = headers)
		text = json.loads(response.text)
		return text
	if kind == 'PLAY':
		response = requests.post(url, data = json.dumps(start), headers = headers)
		text= json.loads(response.text)
		return text

#pass arrays of 3 [EU, NA, AP] 
def makechange(WEBNODE, JAVANODE, DBNODE):
	change =  {'Servers':{
	               'WEB':{
	                   'ServerRegions':{
	                       'EU':{
	                           'NodeCount': WEBNODE[0]
	                           },
	                       'NA':{
	                           'NodeCount': WEBNODE[1]
	                           },
	                       'AP':{
	                           'NodeCount': WEBNODE[2]
	                           },
	                       }
	                   },
	               'JAVA':{
	                       'ServerRegions':{
	                       	'EU':{
	                           'NodeCount': JAVANODE[0]
	                           },
	                        'NA':{
	                             'NodeCount': JAVANODE[1]
	                             },
	                        'AP':{
	                             'NodeCount': JAVANODE[2]
	                             },
	                           }
	                       },
	                'DB':{
	                       'ServerRegions':{
	                               'EU':{
	                           'NodeCount': DBNODE[0]
	                           },
	                        'NA':{
	                             'NodeCount': DBNODE[1]
	                             },
	                        'AP':{
	                             'NodeCount': DBNODE[2]
	                             },
	                           }          
	                     }
	               },
	          }
	changeVals = {'Command': 'CHNG', 'Token' : '3b00ea6d-1383-4fdc-a6a8-9578091947f9','ChangeRequest': change}
	response = requests.post(url, data= json.dumps(changeVals, sort_keys=False), headers=headers)
	text2 = json.loads(response.text)
	return text2

def addRecords(DBEUrecords, DBNArecords, DBAPrecords, JVEUrecords, JVNArecords, JVAPrecords , WBEUrecords, WBNArecords, WBAPrecords, state):
	DBEUrecords.append(state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["EU"]['NoOfTransactionsInput'])
	DBNArecords.append(state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["NA"]['NoOfTransactionsInput'])
	DBAPrecords.append(state["ServerState"]['ServerTiers']['DB']["ServerRegions"]["AP"]['NoOfTransactionsInput'])
	
	JVEUrecords.append(state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["EU"]['NoOfTransactionsInput'])
	JVNArecords.append(state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["NA"]['NoOfTransactionsInput'])
	JVAPrecords.append(state["ServerState"]['ServerTiers']['JAVA']["ServerRegions"]["AP"]['NoOfTransactionsInput'])
	

	WBEUrecords.append(state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["EU"]['NoOfTransactionsInput'])
	WBNArecords.append(state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["NA"]['NoOfTransactionsInput'])
	WBAPrecords.append(state["ServerState"]['ServerTiers']['WEB']["ServerRegions"]["AP"]['NoOfTransactionsInput'])


def linreg(X, Y):
    """
    X is a list, y is the length
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    y = mx+b
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in map(None, X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

def rateofchange(records):
	m,b = linreg(range(len(records)),records) #your x,y are switched from standard notation
	return m


def makechange2():
	change =  {
           'UpgradeInfraStructure' : True,
           'UpgradeToResearch' : 'GRID',
          }
	changeVals = {'Command': 'CHNG', 'Token' : '3b00ea6d-1383-4fdc-a6a8-9578091947f9','ChangeRequest': change}
	response = requests.post(url, data= json.dumps(changeVals, sort_keys=False), headers=headers)
	text2 = json.loads(response.text)
	print text2
	return text2