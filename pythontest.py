import httplib, urllib, urllib2, demjson, requests, functions, json
#import simplejson as json 

print functions.turn("INIT")
print functions.turn("PLAY")["ServerState"]['ServerTiers']['DB']["ServerRegions"]["AP"]['NodeCount']
print functions.makechange([0,0,0], [0,0,0], [0,0,0])