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
        # assignment # static method
        # get each key value and update each key # cpu = userdata.get("cpu", 1)
        self.config.update(userdata)
        return self.config

    def check_config(self, userdata):
        if not "shape" in userdata:
            raise KeyError("shape doesn't exist in config")
        # shape = userdata["shape"]
        # return shape

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
        try:
            config.check_config(dict_data)
        except KeyError as e:
            print("Exception occured is", str(e))
            exit(0)
        else:
            print("validations are succesfull")
        config_dict = config.overwrite_config(dict_data)
        print(config_dict)

if __name__ == "__main__":
    main()