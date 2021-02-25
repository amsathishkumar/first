import re

with open('dotnew.txt', 'r') as furls:
    lines = furls.readlines()

myDict = dict() 
noport = []
for line in  lines:
   hoslinematch = re.findall("Host : ",line)
   if (hoslinematch):
       host = dict()
       tem= line.split("Host")[1]
       tem1 = tem.split(" ")
       global hostname
       sip =tem1[2]
       hostname= tem1[3].replace("(","").replace(")","").replace("\n","")
       host['IP']=sip
       myDict[hostname] = host 
       mylist = []
   else:
        x1 = re.findall("port",line)
        if(x1):
           a=myDict[hostname]
           if(re.findall('open',line)):
              pp = re.findall(r'\d+', line)
              mylist.append(pp[0])
              a['PORT']=mylist
           myDict[hostname]=a

for URL in myDict.keys():
    if 'PORT' in myDict[URL].keys():
        words = ['80','443']
        portLst = myDict[URL]['PORT']
        if all((w in portLst for w in words)):
            print(URL)
            print(myDict[URL]['IP'])
            print(myDict[URL]['PORT'])
    else:
         noport.append(URL)
print("No ports Hosts")
print(noport)