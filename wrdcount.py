#!/usr/bin/env python
import sys
from operator import itemgetter
def top(x):
    x[1]
def wrdcnt(filen):
    filer=open(filen,'r')
    wrdcntd={}
    wrdli=[]
    for line in filer:
        line.strip()
        word=line.split()
        for w in word:
            if w not in wrdcntd:
                wrdcntd[w]=1
            else:
                wrdcntd[w]+=1
    filer.close()
    sort=sorted(wrdcntd.items(),key=itemgetter(1),reverse=True)
    print sort
    fo=open(filen +'out.txt','w')
    for x in sort:
        print >> fo.write(("\n"+x[0]+"\t"+str(x[1])))
#print wrdcnt()
filen=sys.argv[1]
wrdcnt(filen)
