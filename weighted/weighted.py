import pandas as pd
import sys


def get_weighted_kappa(data, weights_file):
    """
    Return the weighted cohen's kappa given file data and predefined weights.
    """
    df = pd.read_csv(data)
    df1 = pd.read_csv(weights_file, sep=",\s", header=None, names=["c", "w"], 
        engine="python")
    
    total = len(df) 
    num_weights = len(df1)
    weights = dict(zip(df1.c, df1.w))
    
    # calculate weighted ovserved_agreement
    df['Weight'] = df.apply(lambda x: 1 - abs(weights[x['C1']] - 
                    weights[x['C2']]) / float(num_weights - 1), axis=1)
    observed_agreement = df['Weight'].sum() / float(total)

    # calculate weighted agreement_by_chance
    agreement_by_chance = 0
    coder1 = dict(df['C1'].value_counts()) 
    coder2 = dict(df['C2'].value_counts())
    for i in coder1:
        for j in coder2:
            weight = abs(weights[i] - weights[j])
            weight = 1 - (weight / float(num_weights - 1)) # normalization
            agreement_by_chance += (weight * (coder1[i] * coder2[j]) 
            / float(total * total))
                
    kappa = (observed_agreement - agreement_by_chance) \
            / (1 - agreement_by_chance)
    return [kappa, observed_agreement, agreement_by_chance]


def check_input(data, weights):
    """
    Check if the input files exist in the current working directory.
    """
    try:
        with open(data) as f:
            pass
    except IOError:
        print 'Cannot find data file \'{}\'.'.format(data)
        sys.exit(1)
    try:
        with open(weights) as f:
            pass
    except IOError:
        print 'Cannot find weights file \'{}\'.'.format(weights)
        sys.exit(1)


if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print 'usage: python generalized.py <data-file> <weights-file>'
        sys.exit(1)
    data = sys.argv[1]
    weights = sys.argv[2]
    check_input(data, weights)
    
    results = get_weighted_kappa(data, weights)
    print "Weighted Kappa: {}".format(results[0])
    print "Weighted Observed Agreement: {}".format(results[1])
    print "Weighted Agreement by Changce: {}".format(results[2])
    