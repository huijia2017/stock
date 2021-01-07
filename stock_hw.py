import csv
import pandas as pd

# 1. read csv-files in a given folder
import os
import glob

path = 'C:\\Users\\huijia\\Desktop\\python_sgh\\classnote&hw'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
print(result)

# 2. read and write each file

# 2.1 GOOG ---read-write-save

## read the file goog
with open('goog.csv', 'r') as org_goog:
    csv_reader = csv.reader(org_goog)

    for line in csv_reader:
        print(line)


## write the file in a new file(new_goog.csv)

with open('goog.csv', 'r') as org_goog:
    csv_reader = csv.reader(org_goog)

    with open('new_goog.csv', 'w') as new_goog:
        csv_writer = csv.writer(new_goog, delimiter = ',')

        for line in csv_reader:
            csv_writer.writerow(line)


## Change = (Close-Open)/Open
df = pd.read_csv('new_goog.csv') # panda
print(df.head())

df['Change'] = (df['Close'] - df['Open'])/df['Open'] # create a new column named Change
print(df.head())
df.to_csv("new_goog.csv", index=False) # save the new file with inserted column


# IBM

with open('ibm.csv', 'r') as org_ibm:
    csv_reader = csv.reader(org_ibm)

    with open('new_ibm.csv', 'w') as new_ibm:
        csv_writer = csv.writer(new_ibm, delimiter = ',')

        for line in csv_reader:
            csv_writer.writerow(line)

df2 = pd.read_csv('new_ibm.csv')
print(df2.head())

df2['Change'] = (df2['Close']-df2['Open'])/df2['Open']
print(df2.head())
df2.to_csv("new_ibm.csv", index=False)


# msft

with open('msft.csv', 'r') as org_msft:
    csv_reader = csv.reader(org_msft)

    with open('new_msft.csv', 'w') as new_msft:
        csv_writer = csv.writer(new_msft, delimiter = ',')

        for line in csv_reader:
            csv_writer.writerow(line)

df3 = pd.read_csv('new_msft.csv')
print(df3.head())

df3['change'] = (df3['Close'] - df3['Open'])/df3['Open']
print(df3.head())
df3.to_csv("new_msft.csv", index = False)
