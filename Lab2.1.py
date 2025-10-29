import csv
count=0
with open("F:/编程作业/books-en.csv", encoding="latin-1") as file:
    reader=csv.DictReader(file,delimiter=";")
    for row in reader:
        if len(row["Book-Title"])>30:
            count+=1
print(count)