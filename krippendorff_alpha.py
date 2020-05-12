import pandas as pd
import krippendorff
import numpy as np
import argparse
import sys

# Assumptions about the input data file: 
# 1. The data file contains headers (e.g., C1, C2)
# 2. There is an index column.
# 3. There are at least 2 coders and each coder occupies one column.

# Assumptions about the input weights file:
# 1. There are exactly two columns with the first one being the categories and
# the second one being the weights. 
# 2. There are no headers in this file.

def main():
    
    parser = argparse.ArgumentParser(description='This program calculates '\
        'Krippendorff\'s Alpha given nominal data or ordinal data.')
    parser.add_argument('level_of_measurement', choices=['nominal', 'ordinal'], 
    nargs=1, help='set level of measurement')
    parser.add_argument('data', nargs=1, help='set the data file')
    parser.add_argument('-w', '--weights', nargs=1, help='set the weights file,'
    ' required for ordinal data only')
    
    args = parser.parse_args()
    metric = args.level_of_measurement[0]
    data = args.data[0]
    if (metric == 'ordinal') & (args.weights == None):
        parser.error('Must provide a separate file for weights.')
    check_input(data)
    
    df = pd.read_csv(data)
    reliability_data = []
    if metric == 'ordinal':
        check_input(args.weights[0])
        df1 = pd.read_csv(args.weights[0], sep=",\s", header=None, 
            names=["c", "w"], engine="python")
        weights = dict(zip(df1.c, df1.w))
        for i in range(1, len(df.columns)):
            temp = df.apply(lambda x: np.nan if str(x[i]).strip() == '' \
            else weights[x[i]], axis=1)
            reliability_data.append(temp.to_list())
    else:
        for i in range(1, len(df.columns)):
            temp = df.apply(lambda x: np.nan if str(x[i]).strip() == '' \
            else x[i], axis=1)
            reliability_data.append(temp.to_list())

    print("Krippendorff's alpha for {} metric:".format(metric), 
    krippendorff.alpha(reliability_data=reliability_data, 
                       level_of_measurement=metric))

def check_input(data):
    """
    Check if the input files exist in the current working directory.
    """
    try:
        with open(data) as f:
            pass
    except IOError:
        print("Cannot find file \'", data, "\'")
        sys.exit(1)

if __name__ == '__main__':
    main()
    
    
    