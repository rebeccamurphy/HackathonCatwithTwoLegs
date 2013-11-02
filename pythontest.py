import json, httplib, urllib, urllib2

data = {
        'Command': 'INIT',
        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None,
}


url = 'http://hermes.wha.la/api/hermes'

data2 = urllib.urlencode(data)

req = urllib2.Request(url, data2)
response = urllib2.urlopen(req)

print response.read()

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
print response2.read()