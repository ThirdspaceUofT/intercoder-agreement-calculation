import pandas as pd
import sys
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
    df1 = pd.read_csv(weights_file, sep=",\s", header=None, names=["c", "w"], 
        engine="python")
    
    total = len(df) 
    if total == 0:
        return 0  
    num_coders = len(df.columns) - 1
    
    num_weights = len(df1)
    weights = dict(zip(df1.c, df1.w))
    
    pi = 0    
    for i in range(1, num_coders):
        for j in range(i + 1, num_coders + 1):
            # calculate weighted ovserved_agreement
            weighted = df.apply(lambda x: 1 - abs(weights[x[i]] - 
                            weights[x[j]]) / (num_weights - 1), axis=1)
            observed_agreement = weighted.sum() / total
            
            # calculate weighted agreement_by_chance
            agreement_by_chance = 0
            coder1 = dict(df.iloc[:, i].value_counts()) 
            coder2 = dict(df.iloc[:, j].value_counts())
            for k in coder1:
                for t in coder2:
                    weight = 1 - abs(weights[k] - weights[t]) / (num_weights - 1)
                    a, b = 0, 0
                    if k in coder2:
                        a = coder2[k]
                    if t in coder1:
                        b = coder1[t]
                    agreement_by_chance += weight * (coder1[k] + a) * \
                        (coder2[t] + b) / (4 * total * total)
            pi += (observed_agreement - agreement_by_chance) \
                / (1 - agreement_by_chance)
                
    pi = pi / (num_coders * (num_coders - 1) / 2)
    
    print("Scott's Pi:", pi)

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


    