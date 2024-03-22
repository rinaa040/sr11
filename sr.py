import argparse
import csv
import json
import sys

parser = argparse.ArgumentParser(
    description="convert integers to decimal system")
parser.add_argument('--port', type=int,
                    help='default numeric system')
parser.add_argument('--server', type=str)
parser.add_argument('--filename', type=str)
parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
                    help='the file where converted data should be written')

args = parser.parse_args()
print(args)

lst = []
d = {}
a = []
with open(args.filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='+', quotechar='"')
    for row in reader:
        row['name'] = row['last_name'] + " " + row['first_name']
        d['name'] = row['name']
        d['lie'] = []
        d['truth'] = []

        if row['validity'] == 'lie':
            d['lie'].append(row['message'])
        if row['validity'] == 'truth':
            d['truth'].append(row['message'])

        if d not in lst:
            lst.append(d)
        d = {}

print(lst)

# with open('res.json', 'w') as cat_file:
#     json.dump(lst, cat_file)
# args.log.write(args.server)
# args.log.close()
