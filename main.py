##########################################################################################
################################### Imports ##############################################

import os    # Module to create file paths across operating systems
import csv   # Module to read CSV files
import time  # Track time for program to execute

start_time = time.process_time()  # Track Time (start)

##########################################################################################
######################### Data Extract / Create Dict #####################################

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row:  Voter ID,County,Candidate
    header_row = next(csvreader)
    dict_final={}

    # 
    for row in csvreader:
        k = row[2]   #index 2 - Candidate
        n = 1
        if k in dict_final.keys():
            dict_final[k] = dict_final[k] + n
        else:
            dict_final[k] = n  #dict_add could be replaced with 1

        
    ###################################################################
    ################### Printout Dict to .txt #########################
    f = open('output.txt',"w+")
    print(f'', file=f)
    print(f'Election Results', file=f)
    print(f'------------------------------------------', file=f)
    total_votes = sum(dict_final.values())
    print(f'Total Votes: {total_votes}', file=f)
    print(f'------------------------------------------', file=f)

    # print all key-value pairs via a loop
    for k, v in dict_final.items():
        print(f'{k}:  {round(v/total_votes*100,1)}%  ({v})', file=f)
    print(f'------------------------------------------', file=f)
    
    # find and print the key of the max vote count
    max_value = max(dict_final.values())
    max_keys = [k for k, v in dict_final.items() if v == max_value] 
    if len(max_keys)>1:
        print(f'There was a tie with:  {max_keys}', file=f)
    else:
        print(f'Winner: {max_keys[0]}', file=f)
    print(f'------------------------------------------', file=f)

    f.close()

    print(f"--- {(time.process_time() - start_time)} seconds ---")  # Final program run time

    ###################################################################
    ################ Printout Dict to terminal ########################

    # print(f'\nElection Results')
    # print(f'------------------------------------------')
    # total_votes = sum(dict_final.values())
    # print(f'Total Votes: {total_votes}')
    # print(f'------------------------------------------')

    # # print all key-value pairs via a loop
    # for k, v in dict_final.items():
    #     print(f'{k}:  {round(v/total_votes*100,1)}%  ({v})')
    # print(f'------------------------------------------')
    
    # # find and print the key of the max vote count
    # max_value = max(dict_final.values())
    # max_keys = [k for k, v in dict_final.items() if v == max_value] 
    # if len(max_keys)>1:
    #     print(f'There was a tie with:  {max_keys}')
    # else:
    #     print(f'Winner: {max_keys[0]}')
    # print(f'------------------------------------------')

# I could use the code above or I could just open the file that I created
# Below is the output file printed to the terminal.
with open('output.txt', 'r') as fin:
    print(fin.read())

###################################################################
######################## Data Check ###############################

# Module to do math calculations and check above calculation
# import pandas as pd 
# import numpy as np

# file_one = "Resources/election_data.csv"
# file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

# output=file_one_df["Candidate"].value_counts()

# print(f'')
# print(f'Election Results')
# print(f'------------------------------------------')
# print(f'Total Votes:')
# print(f'------------------------------------------')
# print(output)
# print(f'------------------------------------------')
