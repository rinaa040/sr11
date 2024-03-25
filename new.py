import io
import logging
from json import dumps
from time import sleep
import argparse
import requests
from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            '2025-12-01': [105, 54, 57, 288],
            '2034-04-25': [217, 106, 81, 219, 1, 112],
            '2018-03-05': [44, 168, 29],
            '2021-10-05': [13, 3, 17, 248, 21, 138]
        },
        {
            '2013-05-23': [7, 31, 230, 26, 98, 240, 222],
            '2019-11-21': [117, 56, 241, 1],
            '2001-06-02': [67, 223, 204, 71],
            '2018-04-09': [270, 17, 27, 18],
            '2021-10-09': [297, 94, 83, 67]
        }
    ]

    index = 0
    while (index := int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        while (
                row := input(
                    'Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':

            parser = argparse.ArgumentParser()
            parser.add_argument('server', type=str)
            parser.add_argument('port', type=str, help="port")
            parser.add_argument('data', nargs='+', help="data")
            parser.add_argument('--coeff', type=int, default=2)
            parser.add_argument('--subtract', type=int)

            args = parser.parse_args()
            response = requests.get(f"http://{args.server}:{args.port}").json()
            lst = []
            for a in response.keys:
                if a == date:
                    for date in args.data:
                        nums = []
                        c = 0

                        for num in response[date]:
                            if num % 2 != 0:
                                num *= args.coeff
                                nums.append(num)
                            elif args.subtract and num % 2 == 0:
                                s = num - args.subtract
                                if s > 0:
                                    nums.append(s)
                                else:
                                    nums.append(num)
                            else:
                                nums.append(num)
                        for num in nums:
                            if num < sum(nums) / len(nums):
                                c += 1
                else:


                d = {
                    "date": a,
                    "cost": sum(nums),
                    "number": c
                }
                lst.append(d)
                    print(lst)

import csv
import json
import sys

data = sys.stdin.read().rstrip('\n')
lst = []
with open(data, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter='.', quotechar='"')
    for row in reader:
        del row['id'], row['distance']
        row['city'] = row['destination']
        row['name2'] = row['name']
        del row['name']
        row['name'] = row['name2']
        del row['destination'], row['name2']

        lst.append(row)
lst.sort(key=lambda x: (x['city'], x['name']))
print(lst)

with open('res.json', 'w') as cat_file:
    json.dump(lst, cat_file)



MIG
YKGMIGFCQIACWMDERDMIGR
CXATHLOMIGCX
YWMIGIS
CSVVXQWOQOLHDKNOFYPRB
