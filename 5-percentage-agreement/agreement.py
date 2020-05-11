import pandas as pd
import krippendorff
import numpy as np
import argparse

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
        'percentage agreement of the given data.')
    parser.add_argument('data', nargs=1, help='set the data file')
    parser.add_argument('weights', nargs=1, help='set the weights file')
    args = parser.parse_args()
    data = args.data[0]
    weights_file = args.weights[0]
    check_input(data)
    check_input(weights_file)
    
    df = pd.read_csv(data)
    total = len(df) 
    if total == 0:
        return 0  
    num_coders = len(df.columns) - 1
            
    df1 = pd.read_csv(weights_file, sep=",\s", header=None, names=["c", "w"], 
        engine="python")
    num_weights = len(df1)
    weights = dict(zip(df1.c, df1.w))
    agreement = 0    
    for i in range(1, num_coders):
        for j in range(i + 1, num_coders + 1):
            # calculate weighted ovserved_agreement
            weighted = df.apply(lambda x: 1 - abs(weights[x[i]] - 
                            weights[x[j]]) / float(num_weights - 1), axis=1)
            agreement += weighted.sum() / float(total)
            
    result = agreement / (num_coders * (num_coders - 1) / 2)
    print("Percentage Agreement: ", result)

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
    
    
    