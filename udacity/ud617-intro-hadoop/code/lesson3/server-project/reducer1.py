import sys

totalHits = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisAddress = data_mapped

	if oldKey and oldKey != thisKey:
		if oldKey == "/assets/js/the-associates.js":
			print oldKey, "\t", totalHits
		oldKey = thisKey
		totalHits = 0

	oldKey = thisKey
	totalHits += 1

if oldKey != None:
	print oldKey, "\t", totalHits