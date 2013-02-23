import csv
from shutil import copy
train=[]
with open("../raw/train.csv") as f:
	fr=csv.reader(f)
	print fr.next()
	for i in f:
		train.append(i.split(","))

print train[:5]

for i in train:
	if i[1].strip()=="0":
		copy("../raw/train/"+i[0],"../processed/negatives/")
	else:
		copy("../raw/train/"+i[0],"../processed/positives/")