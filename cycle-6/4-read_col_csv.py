import csv
f=open("D:\Dona-McaS1\python\Cycle_6\cycle-6\Book1.csv",'r')
content=csv.reader(f)
for x in content:
    print(x)