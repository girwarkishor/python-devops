from arg_parser_ansible import *
from to_get_instances import *


# import pdb
# pdb.set_trace()
filter_dict = {'running_status': {"name":"instance-state-name", "value":"running"}}


def main():
    running_status = args.running
    if running_status:
        instance_obj = GetInstancesIds(filter_dict["running_status"]["name"], filter_dict["running_status"]["value"])
        ids_list = instance_obj.get_id()
        print(ids_list)

        with open("hosts", "w+") as hosts:
            hosts.write("[running_instances]\n")
            for each_id in ids_list:
                hosts.write(each_id + "\n")






if __name__=="__main__":
    main()