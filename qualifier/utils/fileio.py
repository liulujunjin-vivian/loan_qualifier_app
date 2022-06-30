# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#this is a function that receive a nested list
#and save the data in a csv file 
#the purpose is to provide the user a spreadsheet
def save_csv(qualification_list):
    print("Providing a spreadsheet requires file path\n"
        + "please enter a path (./your_file_name.csv)")
    
    csvpath = questionary.text("Enter a file path to a rate-sheet").ask()
    header = ["lender", "Max Loan Amount", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    with open(csvpath, 'w') as my_file:
        csvwriter = csv.writer(my_file)
        csvwriter.writerow(header)
        for line in qualification_list:
            csvwriter.writerow(line)
