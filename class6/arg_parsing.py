import argparse


# def arg_parse():
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", type=str, help="its takes username as the input string", nargs=2)
# parser.add_argument("-i", "--id", type=str, help="id of user")

args = parser.parse_args()



if __name__ == "__main__":
    print("args file print elements")
    print("machine name", args.name[0])
    print("machine id", args.name[1])
    print("args file print elements end elements")

# print(args.id)









