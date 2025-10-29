import csv


with open("F:/编程作业/books-en.csv",encoding="latin-1") as file:
    reader=csv.DictReader(file,delimiter=";")
    Author=input("Author:")
    newreader=[]
    for row in reader:
        try:
            price=float(row["Price"])
            if price>=150 and row["Book-Author"]==Author:
                newreader.append(row)
        except:
            pass
    if not newreader:
        print(" No book")
    else:
        for i in newreader:

            print(i["Book-Title"],i["Book-Author"],i["Price"])
