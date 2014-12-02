import json as js
import requests as r

#get the feed
request1 = r.get("http://www.youtypeitwepostit.com/api/")
request1.text

test = r.post("http://www.youtypeitwepostit.com/api/", json={ 
    "template" : {"data" : [{"prompt" : "Text of message", "name" : "text", "value" : "hhhhhello"}]}})



data = js.loads(request1.text)

for item in data['collection']['items']['data']:

    print item['data'][0]