import pandas as pd
import sys

# Assumptions about the input data file: 
# 1. The data file contains headers (e.g., C1, C2)
# 2. There is an index column.
# 3. There is a vector column (i.e., a column with values like 1,1,0,0) 
# for each coder. 
# 4. There are exactly 2 coders and the data recorded for the 2 coders have the 
# same pattern. Each coder records either 1 or 0 for every label.

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
    return 1 - diff / float((len(a) + 1) / 2)

def helper(x):
    """
    Given a line x in the data frame, calculate the corresponding weight.
    """
    a = x[len(x) / 2]
    b = x[len(x) - 1]
    return get_weight(str(a), str(b))

def get_weighted_kappa(data):
    """
    Return the weighted cohen's kappa given data.
    """
    df = pd.read_csv(data)
    total = len(df)
    if total == 0:
        return 0  
    num_cols = len(df.columns)
    df['Weight'] = df.apply(helper, axis=1)
    observed_agreement = df['Weight'].sum() / float(total)
    
    agreement_by_chance = 0
    coder1 = dict(df.iloc[:,num_cols/2].value_counts()) 
    coder2 = dict(df.iloc[:,num_cols-1].value_counts())
    for i in coder1:
        for j in coder2:
            weight = get_weight(str(i), str(j))
            agreement_by_chance += (weight * (coder1[i] * coder2[j]) 
            / float(total * total))
                
    kappa = (observed_agreement - agreement_by_chance) \
            / (1 - agreement_by_chance)
    return [kappa, observed_agreement, agreement_by_chance]


def check_input(data):
    """
    Check if the input files exist in the current working directory.
    """
    try:
        with open(data) as f:
            pass
    except IOError:
        print 'Cannot find data file \'{}\'.'.format(data)
        sys.exit(1)

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print 'usage: python multilabel.py <data-file>'
        sys.exit(1)
    data = sys.argv[1]
    check_input(data)
    
    results = get_weighted_kappa(data)
    print "Weighted Kappa: {}".format(results[0])
    print "Weighted Observed Agreement: {}".format(results[1])
    print "Weighted Agreement by Changce: {}".format(results[2])
    