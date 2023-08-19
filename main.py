import json

def main():
    data = ''
    line = input()
    while (line != '!'):
        data += line
        line = input()

    export_to_csv(data);
    print('exported successfully')

def export_to_csv(data):
    result = []
    raw = json.loads(data)
    firstEntry = raw[0]
    header_items = [];
    get_header_items(header_items, firstEntry)
    result.append(header_items)

    for entry in raw:
        data = []
        add_items_to_data(data, entry)
        result.append(data)

    with open('output.csv', 'w') as output_file:
        for element in result:
            output_file.write(','.join(map(str, element)) + '\r')


def get_header_items(result, values):
    for key in values:
        if isinstance(values[key], dict):
            result.append(key)
            get_header_items(result, values[key])
        else:
            result.append(key)

def add_items_to_data(result, values):
    for key in values:
        result.append(str(values[key]).replace(",", "").replace("[", "").replace("]", "").replace("'", ""))

main()