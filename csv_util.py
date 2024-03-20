import csv

def create_csv(filename, fieldnames):
    f = open(filename, 'w')
    csv.writer(f).writerow(fieldnames)
    f.close()


def write_to_csv_with_dict(filename, fieldnames, data):
    f = open(filename, 'a')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(data)
    f.close()