import json
from argparse_files import args

def main():
    # context manager  -- with
    # k = open("filename", "r")
    # k.close()
    filename = args.filename
    with open(filename, "r") as config_data:
        data = config_data.read()
        dict_data = json.loads(data)
        print(dict_data)

if __name__ == "__main__":
    main()