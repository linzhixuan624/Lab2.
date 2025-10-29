import csv


publisher_once=set()
with open("F:/编程作业/books-en.csv",encoding="latin-1")as file:
     reader=csv.DictReader(file,delimiter=";")
     for row in reader:
          publisher=row.get('Publisher','')
          publisher_once.add(publisher)
for publishers in sorted(publisher_once):
     print(publishers)


               

