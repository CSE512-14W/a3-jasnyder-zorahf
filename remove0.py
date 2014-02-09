import csv
import sys

reader = csv.DictReader(open(sys.argv[1], "rb"))
states = {}

print "bpl,latitude,longitude"

for line in reader:
    bpl = int(line['bpl'])
    lati = float(line['latitude'])
    longi = float(line['longitude'])
    
    print str(bpl) + "," + str(lati) + "," + str(longi)
