import csv
import random


with open("F:/编程作业/books-en.csv",encoding="latin-1") as file:
    reader=list(csv.DictReader(file,delimiter=";"))
    books=random.sample(reader,20)
with open("Books.txt","w",encoding="latin-1") as f:
    for index,book in enumerate(books,start=1):
        f.write(f"{index}.{book["Book-Author"]}.{book["Book-Title"]}-{book["Year-Of-Publication"]}\n")

    print("Generation complete")
