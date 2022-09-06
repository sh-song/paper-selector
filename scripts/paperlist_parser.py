import csv
import numpy as np
import pandas as pd
import argparse

argparser = argparse.ArgumentParser(
    description="ask shs"
)

argparser.add_argument(
    '--conf_name',
    default='cvpr',
    help='conference name'
)
argparser.add_argument(
    '--year',
    default='2022',
    help='year in 4 digits'
)

args = argparser.parse_args()


CONF_NAME = args.conf_name
YEAR = args.year

filename = CONF_NAME + "-" + YEAR 

#Open file
file = open('raws/' + filename + '-raw.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

#Read names
names = []
for i, line in enumerate(lines):
    if i % 4 == 0:
        line = line.strip('\n')
        names.append(line)

#Set tags and selected flags

tags = []
checked = []
selected = []
for i, name in enumerate(names):
    tag = CONF_NAME + "-" + YEAR + "-" + str(i)
    tags.append(tag) 
    checked.append(0)
    selected.append(0)

dict = {'tag': tags, 'name':names, 'checked':checked, 'selected': selected}
df = pd.DataFrame(data=dict)
df.to_csv('csvs/' + filename + ".csv", index=False)
print(filename + ".csv saved in csvs/")