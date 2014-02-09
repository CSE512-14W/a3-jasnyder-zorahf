import csv
import sys

reader = csv.DictReader(open(sys.argv[1], "rb"))
states = {}

for line in reader:
    fip = int(line['STATEFIP'])
    bpld = int(line['BPLD'])
    wt = int(line['PERWT']) / 100.0
    if fip in states:
        if bpld in states[fip]:
            states[fip][bpld] += wt
        else:
            states[fip][bpld] = wt
    else:
        states[fip] = {}
        states[fip][bpld] = wt
        
print "State,Birthplace,Weight"
        
for fip, fipdict in states.iteritems():
    for bpld, wt in fipdict.iteritems():
        print str(100*fip) + "," + str(bpld) + "," + str(wt)
