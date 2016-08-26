import json
import urllib

url = raw_input("Enter location: ").rstrip()
if len(url) < 1 :
    #url = "http://python-data.dr-chuck.net/comments_42.json"
    url="http://python-data.dr-chuck.net/comments_302876.json"
print 'Retrieving',url
input = urllib.urlopen(url).read()
print 'Retrieved',len(input),'characters'

info = json.loads(str(input))

count = 0
sum=0
for item in info["comments"]:
    sum+= int(item["count"])
    count+=1
print 'Count:',count
print 'Sum:',sum
