import pandas as pd

if __name__ == '__main__':
    
    df = pd.read_csv ('./data25032020.csv')

    # Obtain the count for each category (e.g., Generic) in the two columns.
    coder1 = dict(df['C2'].value_counts()) 
    coder2 = dict(df['C2'].value_counts())

    total = len(df['C1']) # defining the total number of records in a column

    # Obtain a list of booleans, where 'True' indicates the agreement between 
    # two coders over one row
    test_equal = df.apply(lambda x: True if x['C1'] == x['C2'] else False , axis=1)
    agreement_count = dict(test_equal.value_counts())[True]
    observed_agreement = agreement_count / float(total)
 
    # Calculate agreement_by_chance.
    agreement_by_chance = 0
    for category in coder1:
        if category in coder2: 
            agreement_by_chance += (coder1[category] * coder2[category]) / float((total * total))

    kappa = (observed_agreement - agreement_by_chance) / (1 - agreement_by_chance)
    print "The Cohen\'s Kappa coefficient between coders C1 and C2 is {}.".format(kappa)
