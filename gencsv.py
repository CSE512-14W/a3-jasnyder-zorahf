import csv
import sys

reader = csv.DictReader(open(sys.argv[1], "rb"))
states = {}

for line in reader:
    fip = int(line['STATEFIP'])
    bpl = int(line['BPL'])
    wt = int(line['PERWT']) / 100.0
    if fip in states:
        if bpl in states[fip]:
            states[fip][bpl] += wt
        else:
            states[fip][bpl] = wt
    else:
        states[fip] = {}
        states[fip][bpl] = wt
        
print "State,Birthplace,Weight"
        
for fip, fipdict in states.iteritems():
    for bpl, wt in fipdict.iteritems():
        print str(fip) + "," + str(bpl) + "," + str(wt)
