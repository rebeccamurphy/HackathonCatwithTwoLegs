import json, httplib, urllib, urllib2

data = {
        'Command': 'INIT',
        'Token' :  '3b00ea6d-1383-4fdc-a6a8-9578091947f9',
        'ChangeRequest': None,
}

data_sting = json.dumps(data)

url = 'http://hermes.wha.la/api/hermes'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data2 = urllib.urlencode(data)

req = urllib2.Request(url, data2)
response = urllib2.urlopen(req)
print response.read()