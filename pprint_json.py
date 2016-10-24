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
    print('Enter path to the file:', end='')
    data = load_data(input())
    while data is None:
        print('Looks like the filepath is wrong. Please, enter the real path to JSON file.')
        data = load_data(input())

    pretty_print_json(data)
