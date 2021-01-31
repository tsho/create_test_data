import pandas as pd
import argparse
import logging
from multiprocessing import Pool
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def sample_func(initial_num):
    num = 0
    num += 1
    for i in range(10):
        num += i
  

if __name__ == '__main__':
    df = pd.read_csv('./iris.csv')
    df_output = pd.DataFrame(columns = df.columns)

    parser = argparse.ArgumentParser(description='XXX')
    parser.add_argument('N', help='Number of rows to create test data')
    parser.add_argument('multi_process', default=True)
    args = parser.parse_args()
    N = int(args.N)
    if args.multi_process == 'True':
        Multi = bool(True)
    else:
        Multi = bool(False)

    start = time.time()
    if Multi:
        print('Multi')
        initial_num_list = list(range(N))
        print(len(initial_num_list))
        with Pool(processes=4) as p:
            p.map(func=sample_func, iterable=initial_num_list)
    else:
        print('Single')
        for i in range(N):
            sample_func(i)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")



