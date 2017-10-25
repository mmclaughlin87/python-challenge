"""This script will open files of existing employee information and reformat them"""

import os
import csv

emp_ids = []
name = ""
full_name = []
first_names = []
last_names = []
date = ""
date_split = []
date_formatted = []
SSN = ""
SSN_split = []
SSN_formatted = []
state = ""
abbreviated_states = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# open csv file
filename = input("Please enter the filename for the data you would like to update: ")

filepath = os.path.join("raw_data",filename)
with open(filepath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # reformat data and build lists for each output
    for row in csvreader:
        emp_ids.append(row[0])
        
        name = row[1]
        full_name = name.split(" ")
        first_names.append(full_name[0])
        last_names.append(full_name[1])
        
        date = row[2]
        date_split = date.split("-")
        date_formatted.append(f"{date_split[1]}/{date_split[2]}/{date_split[0]}")

        SSN = row[3]
        SSN_split = SSN.split("-")
        SSN_formatted.append(f"***-**-{SSN_split[2]}")

        state = row[4]
        abbreviated_states.append(us_state_abbrev[state])
        
employees = zip(emp_ids,first_names,last_names,date_formatted,SSN_formatted,abbreviated_states)

# save as csv
save_filepath = filename.strip(".csv") + "_reformatted.csv"
employee_list = list(employees)

with open(save_filepath,"w", newline="") as csvfile:
    csvwriter =csv.writer(csvfile, delimiter = ",")

    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN", "State"])
    for row in employee_list:
        csvwriter.writerow(row)