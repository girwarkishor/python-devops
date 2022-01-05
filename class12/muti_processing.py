from multiprocessing import Pool
import time

def func_lazy(n):
    time.sleep(n)
    string_output = f"sleep completed with time {str(n)}"
    return string_output
    # print("sleep completed with time {}".format(str(n))) #for python < 3.6



# result = func_lazy(3)
# print(result)

time_intervels = [5,4,3,2,1,6]
# #
# for each in time_intervels:
#     result = func_lazy(each)
#     print(result)

def main():
    pool = Pool(16)
    result = pool.imap_unordered(func_lazy, time_intervels)
    for each in result:
        print(each)


if __name__=="__main__":
    main()
    # pass