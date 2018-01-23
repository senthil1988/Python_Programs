#!/usr/bin/env python

import sys,os
from xml.etree import ElementTree as ET
filename="policies.xml"
path=os.path.abspath(filename)
root =ET.parse(path).getroot()
fo=(open("PolicyReport"+'out.txt','w'))



#print "root :",root.tag

value = root.getchildren()[1].getchildren()[1].getchildren()[1].getchildren()

output =[]
count=0
print >> fo.write("%-45s%-15s%-20s\n" %("PolicyName","PSMEnabled","RecordingSafe"))

for x in value:
    for y in x.getchildren():
        if y.get("Enable") == "Yes":
            pcy=("%-45s%-15s%-20s" %(x.get("ID"),y.get("Enable"),y.get("SessionRecorderSafe")))
            output.append(pcy)
            count+=1
        elif y.get("Enable") == "No":
            output.append("%-45s%-15s%-20s" %(x.get("ID"),y.get("Enable"),"Null"))
            pass

for i in sorted(output):
    print >> fo.write(i+"\n")

print >> fo.write("\nThe TotalNo of Policies is %d. No of Policies with PSM Enabled is %d" %(len(output),count))
