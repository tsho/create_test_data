import pandas as pd
import argparse


def create_test_data_single_thread(N, df_output):
    for i in range(N):
        df_dummy = df.sample()

        test_id = "test_{}".format(i)
        df_dummy['ID'] = test_id

        df_output = df_output.append(df_dummy.to_dict('records'))
        if (i % 10000) == 0:
            print(i)

    df_output.to_csv('test.csv', index=None)

if __name__ == '__main__':
    df = pd.read_csv('./iris.csv')
    df_output = pd.DataFrame(columns = df.columns)

    parser = argparse.ArgumentParser(description='XXX')
    parser.add_argument('N', help='Number of rows to create test data')
    args = parser.parse_args()
    N = int(args.N)
    create_test_data_single_thread(N, df_output)



