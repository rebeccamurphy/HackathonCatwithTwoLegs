import httplib, urllib, urllib2, demjson, requests, json
#import simplejson as json 

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
#print response.text
#print text2["ServerState"]['ServerTiers']['DB']["ServerRegions"]["AP"]['NodeCount']
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
