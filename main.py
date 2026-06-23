import csv
import json

IMAGE_LIMIT = 1000

data = []

with open('mnist_train.csv') as f:
    reader = csv.reader(f)

    next(reader)

    for i, row in enumerate(reader):
        if i >= IMAGE_LIMIT:
            break
        if not row:
            continue

        data.append([[int(p) for p in row[1:]], [int(row[0])]])

js = f'var data = {json.dumps(data)};\n'

with open('train_data.js', 'w') as js_file:
    js_file.write(js)