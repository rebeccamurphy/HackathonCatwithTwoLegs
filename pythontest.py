import json, httplib, urllib, urllib2, demjson, requests
url = 'http://hermes.wha.la/api/hermes'
#answer = raw_input('Start the Game (Y/N)')

#while (answer != 'N'):
headers = {'content-type': 'application/json'}

datainit = {
        'Command': 'INIT',
        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None,
}

response = requests.post(url, datainit)


start = {
        'Command': 'PLAY',
        'Token' : '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None
        }

response = requests.post(url, data = start)
text2 = json.loads(response.text)
print text2["ServerState"]['ServerTiers']['DB']["ServerRegions"]["AP"]['NodeCount']

#print response.text
change =  {'Servers':{
               'DB':{
                   'ServerRegions':{
                       'EU':{
                           'NodeCount':-2
                           }
                       }
                   },
               'JAVA':{
                       'ServerRegions':{
                           'NA':{
                               'NodeCount':-2
                               }
                           }
                       },
                'WEB':{
                       'ServerRegions':{
                               'AP':{
                                   'NodeCount':-2
                                   }
                               }
                           }
               }
          }

print change['Servers']['DB']["ServerRegions"]["EU"]['NodeCount']
'''			   
changeVals = {
        'Command': 'CHNG',
        'Token' : '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': change
}
headers = {'content-type': 'application/json'}

response = requests.post(url, data= json.dumps(changeVals), headers=headers)
print response.text




data2 = urllib.urlencode(datainit)

req = urllib2.Request(url, data2)
response = urllib2.urlopen(req)

text = response.read()
text2 = json.loads(text)


start = {
	        'Command': 'PLAY',
	        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
	        'ChangeRequest': None,
	}

send = urllib.urlencode(start)

req2 = urllib2.Request(url, send)
response2 = urllib2.urlopen(req2)
#print text
print ["ServerState"]['ServerTiers']['DB']["ServerStartTurnTime"]
#answer ='N'

print json.dumps(response.read())

print 'start game'


start = {
        'Command': 'PLAY',
        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None,
}


send = urllib.urlencode(start)

req2 = urllib2.Request(url, send)
response2 = urllib2.urlopen(req2)
print response2.read()

req2 = urllib2.Request(url, send)
response2 = urllib2.urlopen(req2)
print response2.read()'''