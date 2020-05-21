import pandas as pd
import sys

# Assumptions about the input data file: 
# 1. The data file contains headers (e.g., C1, C2)
# 2. There is an index column.
# 3. There are at least 2 coders and the data recorded for every coder has the 
# same pattern. 
# 4. Each coder records either 1 or 0 for every label and there is a vector 
# column (with values like 1,0,0,1) for every coder.

def get_weight(a, b):
    """
    Given two vectors, calculate the corresponding weight.
    
    Assumtion: 
    Strings a and b have the same length and are delimited by commas.
    """
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return 1 - diff / ((len(a) + 1) / 2)


def get_weighted_kappa(data):
    """
    Return the weighted cohen's kappa given data.
    """
    df = pd.read_csv(data)
    total = len(df)
    if total == 0:
        exit(0)
    
    size = 1 # define the number of columns occupied by each coder
    while size < len(df.columns):
        if len(str(df.iloc[:, size][0])) > 1:
            break
        size += 1
    num_coders = int((len(df.columns) - 1) / size)
    
    sum_kappa = 0    
    for i in range(1, num_coders):
        for j in range(i + 1, num_coders + 1):
            # calculate weighted ovserved_agreement
            df['Weight'] = df.apply(lambda x: get_weight(str(x[i*size]), 
                            str(x[j*size])), axis=1)
            observed_agreement = df['Weight'].sum() / total
            
            # calculate weighted agreement_by_chance
            agreement_by_chance = 0
            coder1 = dict(df.iloc[:, i*size].value_counts()) 
            coder2 = dict(df.iloc[:, j*size].value_counts())
            for k in coder1:
                for t in coder2:
                    weight = get_weight(str(k), str(t))
                    agreement_by_chance += weight * (coder1[k] * coder2[t])\
                        / (total * total)
            sum_kappa += (observed_agreement - agreement_by_chance) \
                / (1 - agreement_by_chance)
                
    kappa = sum_kappa / (num_coders * (num_coders - 1) / 2)
    return kappa


def check_input(data):
    """
    Check if the input files exist in the current working directory.
    """
    try:
        with open(data) as f:
            pass
    except IOError:
        print("Cannot find data file \'", data, "\'")
        sys.exit(1)

if __name__ == '__main__':
    if '-h' in sys.argv:
        print("usage: python3 multilabel_kappa.py <data-file>")
        exit(0)
        
    if len(sys.argv) != 2:
        print("usage: python3 multilabel_kappa.py <data-file>")
        sys.exit(1)
    data = sys.argv[1]
    check_input(data)
    
    result = get_weighted_kappa(data)
    print("Weighted Kappa:", result)
    