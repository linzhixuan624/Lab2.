import csv


books=[]
with open("F:/编程作业/books-en.csv",encoding="latin-1")as file:
    reader=csv.DictReader(file,delimiter=';')
    for row in reader:
        download_str = row.get('Downloads','0').strip()
        download_num=int(download_str)
        title = row.get('Book-Title', '')
        author = row.get('Book-Author', '') 
        book_info={'title':title,'download':download_num,'author':author}
        books.append(book_info)
books_sorted=sorted(books,key=lambda x: x['download'], reverse=True)
books20th = books_sorted[:20]
for i,book in enumerate(books20th, 1):

    print(book["title"],book["author"],book["download"])
