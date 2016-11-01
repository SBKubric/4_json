import json
import os


def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath) as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    data = load_data(input('Enter path to the file:\n=> '))
    while data is None:
        data = load_data(input('Looks like the file path is wrong. Please, enter the real path to JSON file.\n=> '))

    pretty_print_json(data)
