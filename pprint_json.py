import json


def load_data(filepath):
    if filepath != '':
        with open(filepath) as data_file:
            return json.load(data_file)
    else:
        return -1

def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    data = -1
    while data == -1:
        print('Enter path to the file:')
        data = load_data(input())

    pretty_print_json(data)
