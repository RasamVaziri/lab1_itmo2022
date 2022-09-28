import csv
import random


def count_books():
    with open('books-en.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        entries_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
                entries_count += 7
            line_count += 1
            entries_count += 7
        print(f'Processed {line_count} lines.')
        print(f'Processed {entries_count} entries.')


def check_books_name():
    with open('books-en.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        number_of_books = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1

            counter = 0
            for _ in row["Book-Title"]:
                counter += 1
            if counter > 30:
                number_of_books += 1

        print(f'number of records that have a string longer than 30 characters is {number_of_books} books.')


def year_of_publication():
    with open('books-en.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        booksCount = 0

        for row in csv_reader:
            yop = row["Year-Of-Publication"]
            if yop.isnumeric():
                year = yop
                if int(year) >= 2018:
                    booksCount += 1

        print(f'number of records with year of publication more than 2018 are {booksCount} books.')


def Random(n):
    with open("books-en.csv", "r") as student_csv_file:
        csv_reader = csv.reader(student_csv_file)
        next(csv_reader)
        return random.choice([line[n] for line in csv_reader])


with open('readme.txt', 'w', encoding="utf-8") as f:
    for x in range(0, 10):
        a = Random(1)
        b = Random(2)
        c = Random(3)
        book_author = "<Book author>: "
        book_name = " - <Book name>: "
        publication_year = " - <Year of Publication>: "

        lines = [str(book_author), str(Random(1)), str(book_name),
                 str(Random(2)), str(publication_year), str(Random(3))]
        print(lines)
        f.writelines(lines)
        f.write('\n')

count_books()
check_books_name()
year_of_publication()