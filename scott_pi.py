import pandas as pd
import sys
import argparse

# Assumptions about the input data file: 
# 1. The data file contains headers (e.g., C1, C2)
# 2. There is an index column.
# 3. There are exactly 2 coders and each coder occupies one column.

# Assumptions about the input weights file:
# 1. There are exactly two columns with the first one being the categories and
# the second one being the weights. 
# 2. There are no headers in this file.

def main():
    
    parser = argparse.ArgumentParser(description='This program calculates '\
        'Scott\'s Pi of the given data.')
    parser.add_argument('level_of_measurement', choices=['nominal', 'ordinal'], 
    nargs=1, help='set level of measurement')
    parser.add_argument('data', nargs=1, help='set the data file')
    parser.add_argument('weights', nargs=1, help='set the weights file')
    args = parser.parse_args()
    data = args.data[0]
    weights_file = args.weights[0]
    metric = args.level_of_measurement[0]
    check_input(data)
    check_input(weights_file)

    df = pd.read_csv(data)
    df1 = pd.read_csv(weights_file, sep=",\s", header=None, names=["c", "w"], 
        engine="python")
    
    total = len(df) 
    if total == 0:
        exit(0)
    num_coders = len(df.columns) - 1
    if num_coders > 2:
        print("The number of raters should be exactly 2.")
        exit(1)
 
    max_diff = df1.w.max() - df1.w.min()
    weights = dict(zip(df1.c, df1.w))
    
    pi = 0

    # calculate weighted ovserved_agreement
    if metric == 'nominal':
        weighted = df.apply(lambda x: 1 if x[1] == x[2] else 0, 
                axis=1)
    else:
        weighted = df.apply(lambda x: 1 - abs(weights[x[1]] - 
                    weights[x[2]]) / max_diff, axis=1)
    observed_agreement = weighted.sum() / total
            
    # calculate weighted agreement_by_chance
    agreement_by_chance = 0
    coder1 = dict(df.iloc[:, 1].value_counts()) 
    coder2 = dict(df.iloc[:, 2].value_counts())
    if metric == 'nominal':    
        for k in weights:
            a, b = 0, 0
            if k in coder1:
                a = coder1[k]
            if k in coder2:
                b = coder2[k]
            agreement_by_chance += (a + b) ** 2
    else:
        for k in coder1:
            for t in coder2:
                weight = 1 - abs(weights[k] - weights[t]) \
                    / max_diff
                a, b = 0, 0
                if k in coder2:
                    a = coder2[k]
                if t in coder1:
                    b = coder1[t]
                agreement_by_chance += weight * (coder1[k] + a) * \
                (coder2[t] + b)
            
    agreement_by_chance /= (2 * total) ** 2
    pi += (observed_agreement - agreement_by_chance) \
        / (1 - agreement_by_chance)

    print("Scott's Pi for {} metric:".format(metric), pi)

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


    