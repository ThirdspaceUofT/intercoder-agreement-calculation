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
        'Scott\'s Pi of the given data.')
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
    categories = list(df1.c)
    num_weights = len(df1)
    weights = dict(zip(df1.c, df1.w))
    
    kappa, agreement_by_chance, observed_agreement = 0, 0, 0
    for i in categories:
        count = df.apply(lambda x: dict(x.value_counts())[i] \
                if i in list(x) else 0, axis=1)
        squared_count = df.apply(lambda x: (dict(x.value_counts())[i] * 
                    dict(x.value_counts())[i]) if i in list(x) else 0, axis=1)
        agreement_by_chance += count.sum() * count.sum() / (total * num_coders) ** 2
        observed_agreement += squared_count.sum()
        
    observed_agreement -= total * num_coders
    observed_agreement /= total * num_coders * (num_coders - 1)
    kappa = (observed_agreement - agreement_by_chance) \
                / (1 - agreement_by_chance)
    print('Fless Kappa:', kappa)
    

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


    