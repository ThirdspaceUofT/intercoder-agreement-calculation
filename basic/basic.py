import pandas as pd
import sys

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
        print 'usage: python basic.py <data-file>'
        sys.exit(1)
    data = sys.argv[1]
    check_input(data)
    
    df = pd.read_csv(data)
    total = len(df) # defining the total number of records in a column

    # calculate observed_agreement
    df['Weight'] = df.apply(lambda x: 1 if x['C1'] == x['C2'] else 0 , axis=1)
    observed_agreement = df['Weight'].sum() / float(total)
 
    # calculate agreement_by_chance.
    agreement_by_chance = 0
    coder1 = dict(df['C1'].value_counts()) 
    coder2 = dict(df['C2'].value_counts())
    for category in coder1:
        if category in coder2: 
            agreement_by_chance += (coder1[category] * coder2[category]) / float((total * total))

    kappa = (observed_agreement - agreement_by_chance) / (1 - agreement_by_chance)
    print "Cohen\'s Kappa: {}".format(kappa)
    print "Observed Agreement: {}".format(observed_agreement)
    print "Agreement by Chance: {}".format(agreement_by_chance)
