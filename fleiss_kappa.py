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

def helper(x, i, weights, max_diff, metric):
    """
    This helper function applies to each row for the sake of calculating 
    observed agreement.
    
    Parameters:
        x: a row corresponding to a subject
        i: a chosen category
        weights: a dictionary mapping categories to weights
        max_diff: the difference between the maximum weight and the minimum 
                weight
        metric: the level of measurement for the data 
    """
    if x.num_coders < 2:
        return 0
    
    # subject_info contains the categories that were assigned to that subject 
    # and the corresponding number of times they appear
    y = x.drop(labels=['num_coders'])
    subject_info = dict(y.value_counts())

    if i not in subject_info:
        return 0
    
    
    if metric == 'nominal':
        return (subject_info[i] ** 2 - subject_info[i]) / \
            x.num_coders * (x.num_coders - 1)
    
    result = 0
    for j in weights:
        if j in subject_info:
            result += (1 - abs(weights[i] - weights[j]) / max_diff) * \
                        subject_info[j]
    result -= 1
    result *= subject_info[i]
    result /= x.num_coders * (x.num_coders - 1)
    return result

def helper1(x, i):
    """
    This helper function calculates, for each subject, the fraction of 
    the number of raters that assign category i to that subject divided 
    by the total number of raters that assign to that subject.
    
    Parameters:
        x: a row corresponding to a subject
        i: a chosen category
    """
    y = x.drop(labels=['num_coders'])
    subject_info = dict(y.value_counts())
    if i in subject_info:
        return subject_info[i] / x.num_coders  
    else:
        return 0
    

def main():
    
    parser = argparse.ArgumentParser(description='This program calculates '\
        'Fleiss\' Kappa of the given data.')
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

    df = pd.read_csv(data, index_col=0)
    df1 = pd.read_csv(weights_file, sep=",\s", header=None, names=["c", "w"], 
        engine="python")
    
    total = len(df) 
    if total == 0:
        exit(0)
    
    max_diff = df1.w.max() - df1.w.min()
    weights = dict(zip(df1.c, df1.w))
    
    # find the number of subjects that were coded by >= 2 raters
    df['num_coders'] = df.apply(lambda x: sum([1 if i in weights else 0 \
                        for i in list(x)]), axis=1)
    check_valid = df.apply(lambda x: 1 if x.num_coders >= 2 else 0, axis=1)
    valid_total = check_valid.sum()
    
    kappa, agreement_by_chance, observed_agreement = 0, 0, 0
    
    # variable categories is for calculating agreement_by_chance
    categories = {}
    for i in weights:
        observed = df.apply(lambda x: helper(x, i, weights, max_diff, 
                metric) if x.num_coders >= 2 else 0, axis=1)
        observed_agreement += observed.sum()
        
        chance = df.apply(lambda x: helper1(x, i), axis=1)
        categories[i] = chance.sum()
        
        
    for i in weights:
        if metric == 'nominal':
            agreement_by_chance += categories[i] ** 2
        else:
            for j in weights:
                weight = 1 - abs(weights[i] - weights[j]) / max_diff
                agreement_by_chance += weight * categories[i] * categories[j]
            
    agreement_by_chance /= total ** 2
    observed_agreement /= valid_total
    kappa = (observed_agreement - agreement_by_chance) \
                / (1 - agreement_by_chance)
    print('Fleiss\' Kappa for {} metric:'.format(metric), kappa)
    

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


    