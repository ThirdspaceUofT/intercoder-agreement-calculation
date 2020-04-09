# Now that you have calculated Cohen's Kappa, the next step is to computed weighted Kappa. This is usually done when the categories are ordered or ranked (for example, a Likert scale with categories such as ‘strongly disagree’, ‘disagree’, ‘neutral’, ‘agree’, and ‘strongly agree’). Here, we give weights to each of the categories to calculate the degree of disagreement.

# One of my previous students had created a spreadsheet for calculating the weighted Kappa, I am sharing this with you: 
# https://docs.google.com/spreadsheets/d/1FqNlDVw53oUTOTPugVQE2ZVczriQOMX7020j-9iphgs/edit?usp=sharing

# Have a look, see if you're able to understand what's happening here. I think this should be straightforward, you have to multiply the corresponding weights with the observed_agreement and agreement_by_chance matrices. The spreadsheet only has the agreement matrix - could you make a data file to use in your program that reflects this

# The spreadsheet has some test data which is different than the data in the matrices. - the categories in the test data are a Likert scale from (0 to 15). Assume the weighting is linear.

#----------------------------

# observed_agreement, agreement_by_chance;
# multiply the corresponding weights with the observed_agreement and agreement_by_chance matrices? 

# step 1: agreement matrix -> data file (write to a file)
