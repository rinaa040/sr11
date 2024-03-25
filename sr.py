# import argparse
# import csv
# import json
# import sys
#
# parser = argparse.ArgumentParser(
#     description="convert integers to decimal system")
# parser.add_argument('--port', type=int,
#                     help='default numeric system')
# parser.add_argument('--server', type=str)
# parser.add_argument('--filename', type=str)
# parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
#                     help='the file where converted data should be written')
#
# args = parser.parse_args()
# print(args)
#
# lst = []
# d = {}
# a = []
# with open(args.filename, encoding="utf8") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter='+', quotechar='"')
#     for row in reader:
#         row['name'] = row['last_name'] + " " + row['first_name']
#         d['name'] = row['name']
#         d['lie'] = []
#         d['truth'] = []
#
#         if row['validity'] == 'lie':
#             d['lie'].append(row['message'])
#         if row['validity'] == 'truth':
#             d['truth'].append(row['message'])
#
#         if d not in lst:
#             lst.append(d)
#         d = {}
#
# print(lst)

# with open('res.json', 'w') as cat_file:
#     json.dump(lst, cat_file)
# args.log.write(args.server)
# args.log.close()




# задача номер 1 неотсортированная
# import sys
#
# data = [x.rstrip('\n') for x in sys.stdin.readlines()]
# d = {}
# letters = {}
# for line in data[1:]:
#     if line.count(data[0]) != 0:
#         d[line] = line.count(data[0])
# s = ''
# for key in d.keys():
#     if d[key] == min(d.values()):
#         s = key
# for symb in s:
#     letters[symb] = s.count(symb)
# # letters = {k: v for k, v in sorted(letters.items(), key=lambda x: x[1])}
# a = [f"{k} - {v}" for k, v in sorted(letters.items(), key=lambda x: (x[1], x[0]))]
# print(a)


import requests
import json
from json import dumps

d = {
    "Camatic": ["Bellambi", "Kiama", "Eden"],
    "Magnolia": ["Kembla", "Kiama"],
    "Beth": ["Sidney", "Nelson", "Kiama"],
    "Win": ["Danvin", "Kembla"]
}

cities = []


def func(*args, address, port):
    # response = requests.get(f"http://{address}:{port}").json()
    response = d
    a = []
    with open('response.json', 'w') as cat_file:
        json.dump(response, cat_file)

    with open('response.json') as cat_file:
        f = cat_file.read()
        data1 = json.loads(f)
        for key, value in data1.items():
            for item in args:
                if item in value:
                    cities.append((key, len(set(value) & set(args))))

    cities.sort(key=lambda x: (x[1], reversed))
    for x in sorted(list(set(cities))):
        a.append(x[0])
    return a


data = ["Kiama", "Nelson", "Eden"]
print(func(*data, address="127.0.0.1", port=5000))

# # Данные на сервере: