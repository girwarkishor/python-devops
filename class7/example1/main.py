import json
from argparse_files import args

class GetConfig:
    def __init__(self):
        self.config = {
                          "cpu": 1,
                          "ram": 4,
                          "region": "ap-south-1"
                        }

    def overwrite_config(self, userdata):
        self.config.update(userdata)
        return self.config


def main():
    """
    usage: python main.py -f config.json
    :return:
    """
    # context manager  -- with
    # k = open("filename", "r")
    # k.close()
    config = GetConfig()
    filename = args.filename
    with open(filename, "r") as config_data:
        data = config_data.read()
        dict_data = json.loads(data)
        config_dict = config.overwrite_config(dict_data)
        print(config_dict)

if __name__ == "__main__":
    main()