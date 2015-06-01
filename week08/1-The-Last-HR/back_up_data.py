import json


class BackUpData:

    @staticmethod
    def save_data_in_file(file_name, data):
        json_data = json.dumps(data, indent=4,  ensure_ascii=False)
        with open(file_name, 'w') as opened_file:
            opened_file.write(json_data)

    @staticmethod
    def read_data_from_file(file_name):
        with open(file_name, 'r') as opened_file:
            data = json.loads(opened_file.read())
        return data
