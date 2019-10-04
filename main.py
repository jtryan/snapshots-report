import csv

from pymongo import MongoClient


csv_columns = [
    'Description',
    'Encrypted',
    'OwnerId',
    'Progress',
    'SnapshotId',
    'StartTime',
    'State',
    'VolumeId',
    'VolumeSize'
]


def write_file(file_name, data):
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    data_list = []

    client = MongoClient('localhost', 27017)
    db = client['db']
    collection = db['collection']

    data = collection.find({}, projection={'_id': False, 'Tags':False, 'KmsKeyId':False})

    for d in data:
        data_list.append(d)

    write_file('fdb-production.csv', data_list)

    client.close()


if __name__ == "__main__":
    main()