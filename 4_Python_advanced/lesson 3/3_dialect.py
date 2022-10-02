import csv


class CustomDialect(csv.Dialect):

    quoting = csv.QUOTE_ALL
    quotechar = "~"
    delimiter = "|"
    lineterminator = '\n'


csv.register_dialect('my_dialect', CustomDialect)

with open('test.csv', 'w') as file:
    writer = csv.writer(file, dialect='my_dialect')
    writer.writerow(['one', 'two', 'three'])
    writer.writerow(['eleven', 'twelve', 'thirteen'])
    writer.writerow(['twenty one', 'twenty two', 'twenty three'])
