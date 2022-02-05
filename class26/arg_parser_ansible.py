import argparse


# def arg_parse():
parser = argparse.ArgumentParser()

parser.add_argument("--running", action="store_true", help="mention this flag for filtering running instances")
# parser.add_argument("-i", "--id", type=str, help="id of user")

args = parser.parse_args()