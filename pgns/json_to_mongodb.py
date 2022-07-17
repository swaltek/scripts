import pymongo
import json

import argparse
argparser = argparse.ArgumentParser(description='Slam some JSON onto a MongoDB server')
argparser.add_argument('json_file',metavar='JSON', type=str, help='json to write')
argparser.add_argument('server_url',metavar='URL', type=str, help='url for mongoDB server')
argparser.add_argument('database',metavar='DB', type=str, help='database on mongoDB server')
argparser.add_argument('collection',metavar='COL', type=str, help='collection on mongoDB server')

args = argparser.parse_args()

client = pymongo.MongoClient(args.server_url)
db = client[args.database]
collection = db[args.collection]
print(collection)
requests = []

with open(args.json_file, 'r') as file:
    data_list = json.loads(file.read())
    for data_dict in data_list:
        requests.append(pymongo.InsertOne(data_dict))


result = collection.bulk_write(requests)
client.close()
