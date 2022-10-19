import csv
import json

DATA_ADS = 'ad.csv'
JSON_ADS = 'ads.json'
DATA_CATEGORIES = 'category.csv'
JSON_CATEGORIES = 'categories.json'
DATA_LOCS = 'location.csv'
JSON_LOCS = 'locations.json'
DATA_USER = 'user.csv'
JSON_USER = 'users.json'


def convert_file(csv_file, json_file, model_name):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            record_to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'Id' in row:
                del row['Id']
            else:
                del row['id']
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            record_to_add['fields'] = row
            result.append(record_to_add)
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_file(DATA_USER, JSON_USER, 'users.user')
