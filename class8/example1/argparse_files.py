import argparse


# def arg_parse():
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename", type=str, help="its takes conf file path")
# parser.add_argument("-i", "--id", type=str, help="id of user")

args = parser.parse_args()