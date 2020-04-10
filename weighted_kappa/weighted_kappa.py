import pandas as pd
import random

# defining global variables
# weight_i contains all pairs of records that correspond to weight i (i=1,2,3)
weight_1 = [{"strongly disagree", "disagree"},
            {"disagree", "neutral"},
            {"neutral", "agree"},
            {"agree", "strongly agree"}]
weight_2 = [{"strongly disagree", "neutral"},
            {"disagree", "agree"},
            {"neutral", "strongly agree"}]
weight_3 = [{"strongly disagree", "agree"},
            {"disagree", "strongly agree"}]

def create_data_file():
    """Create a data file according to some given agreement matrix."""
    
    random_index = random.sample(range(0, 400), 400)
    C1 = []
    C2 = []
    agreement_matrix = [14, 9, 12, 14, 12, 
                        12, 55, 11, 11, 14, 
                        1, 41, 12, 14, 1, 
                        5, 11, 18, 14, 11,
                        8, 15, 12, 12, 61]
    categories = ["strongly disagree", "disagree", "neutral", 
                  "agree", "strongly agree"]
    values = []
    for i in categories:
        for j in categories:
            values.append([i, j])
            
    for i in range(25):
        for j in range(agreement_matrix[i]):
            index = random_index.pop(0)
            C1.insert(index, values[i][0])
            C2.insert(index, values[i][1])
    data = {'C1': C1, 'C2': C2}  
    df = pd.DataFrame(data) 
    df.to_csv('data.csv') 

def categorize_row(x):
    """
    Categorize each row in the data set according to its corresponding weight.
    """
    records = {x['C1'], x['C2']}
    if len(records) == 1:   # x['C1'] == x['C2']
        return 0 
    if records in weight_1:
        return 1
    if records in weight_2:
        return 2
    if records in weight_3:
        return 3
    return 4

def get_weighted_kappa(filename):
    """Return the weighted cohen's kappa given file filename."""
    df = pd.read_csv(filename)

    total = len(df['C1']) # defining the total number of records in a column

    # calculate weighted ovserved_agreement
    result = df.apply(categorize_row , axis=1)
    result = dict(result.value_counts())
    disagree_0 = disagree_1 = disagree_2 = disagree_3 = 0
    if 0 in result:
        disagree_0 = result[0]
    if 1 in result:
        disagree_1 = result[1]
    if 2 in result:
        disagree_2 = result[2]
    if 3 in result:
        disagree_3 = result[3]
    observed_agreement = (disagree_0 / float(total) 
                          + 0.75 * (disagree_1 / float(total)) 
                          + 0.5 * (disagree_2 / float(total)) 
                          + 0.25 * (disagree_3 / float(total)))

    # calculate weighted agreement_by_chance
    agreement_by_chance = 0
    coder1 = dict(df['C1'].value_counts()) 
    coder2 = dict(df['C2'].value_counts())
    for i in coder1:
        for j in coder2:
            records = {i, j}
            if len(records) == 1:   # i == j
                agreement_by_chance += ((coder1[i] * coder2[j]) 
                / float(total * total))
            if records in weight_1:
                agreement_by_chance += (0.75 * ((coder1[i] * coder2[j])
                / float(total * total)))
            if records in weight_2:
                agreement_by_chance += (0.5 * ((coder1[i] * coder2[j]) 
                / float(total * total)))
            if records in weight_3:
                agreement_by_chance += (0.25 * ((coder1[i] * coder2[j]) 
                / float(total * total)))
    kappa = (observed_agreement - agreement_by_chance) / (1 - agreement_by_chance)
    return [kappa, observed_agreement, agreement_by_chance]

if __name__ == '__main__':
    # hardcode a data file if it does not exists
    try:
        with open('./data.csv') as f:
            pass
    except IOError:
        create_data_file()  

    results = get_weighted_kappa('./data.csv')
    print ("The weighted Kappa between" + 
        " coders C1 and C2 is {}.".format(results[0]))
    print ("The weighted observed-agreement is {}.".format(results[1]))
    print ("The weighted agreement-by-changce is {}.".format(results[2]))
    