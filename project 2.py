"""
# Project 2
# Name: Nicodemus Ong
# Student ID: 22607943
"""

def main(csvfile):
    vid_data = read_csv_file(csvfile) # Processes the file into a List for further use in the program
    continent,country = both_dict_creation(vid_data) # Creates 2 empty dictionaries for country and continent
    country = pop_dict(country,vid_data,"country") # Populate the countries dictionary
    continent = pop_dict(continent,vid_data,"continent") # Populate the continent dictionary
    return country,continent

"""
                    **Colates the total lists to be added into the dictionary**
# This function has two parts
# 1. First part focuses on the specific country for processing data
# 2. Second part focuses on the specific continent for processing data
# coalation_of_list(vid_data,month,key,types,country_continent) colates the list for total cases, total deaths, total number of days that is above the average cases/deaths per month 
"""

def colation_of_list(vid_data,month,key,types,country_continent):
    tmplist = []
    # If statement to check if its country or continent data that should be processed
    if country_continent == 'country':
        # Does the relevant check to see which data is required to be processed and returned as a list for all the month
        if types == "total_case":
            for i in range(len(month)):
                tmplist.append(total_cases(vid_data,month[i],key,'country'))
        elif types == "total_death":
            for i in range(len(month)):
                tmplist.append(total_deaths(vid_data,month[i],key,'country'))
        elif types == "total_avg_case":
            for i in range(len(month)):
                tmplist.append(total_days(vid_data,month[i],key,"total_case",'country'))
        elif types == "total_avg_death":
            for i in range(len(month)):
                tmplist.append(total_days(vid_data,month[i],key,"total_death",'country'))
    else:
        # Does the relevant check to see which data is required to be processed and returned as a list for all the month
        if types == "total_case":
            for i in range(len(month)):
                tmplist.append(total_cases(vid_data,month[i],key,'continent'))
        elif types == "total_death":
            for i in range(len(month)):
                tmplist.append(total_deaths(vid_data,month[i],key,'continent'))
        elif types == "total_avg_case":
            for i in range(len(month)):
                tmplist.append(total_days(vid_data,month[i],key,"total_case",'continent'))
        elif types == "total_avg_death":
            for i in range(len(month)):
                tmplist.append(total_days(vid_data,month[i],key,"total_death",'continent'))
    return tmplist

"""
                    **Specific data processing section**
# Every function in this section has two parts
# 1. First part focuses on the specific country for processing data
# 2. Second part focuses on the specific continent for processing data
# total_cases(vid_data,month,key,country_continent) calculates the total number of cases for a specific month for a specific country or continent
# total_deaths(vid_data,month,key,country_continent) calculates the total number of deaths for a specific month for a specific country or continent
# average_of_month(vid_data,month,key,types,country_continent) calculates the average for a specific month for a specific country or continent
# total_days(vid_data,month,key,types,country_continent) calculates the total days that is above the average of cases and deaths for a specific month for a specific country or continent
"""

def total_cases(vid_data,month,key,country_continent):
    total = 0
    # If statement to check if its country or continent data that should be processed
    if country_continent == 'country':
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][1] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific country
                total += int(vid_data[i][3]) # Accumulate all the cases in a variable 
    else:
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][0] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific continent
                total += int(vid_data[i][3]) # Accumulate all the cases in a variable 
    return total

def total_deaths(vid_data,month,key,country_continent):
    total = 0
    # If statement to check if its country or continent data that should be processed
    if country_continent == 'country':
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][1] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific country
                total += int(vid_data[i][4]) # Accumulate all the deaths in a variable 
    else:
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][0] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific continent
                total += int(vid_data[i][4]) # Accumulate all the deaths in a variable 
    return total

def average_of_month(vid_data,month,key,types,country_continent):
    average = 0
    counter = 0
    # If statement to check if the data required is for total cases or total deaths
    if types == "total_case":
        total = total_cases(vid_data,month,key,country_continent)
    else:
        total = total_deaths(vid_data,month,key,country_continent)
    # If statement to check if its country or continent data that should be processed
    if country_continent == 'country':
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][1] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific country
                counter += 1
    else:
        for i in range(len(vid_data)):
            if vid_data[i][2].split("/")[1] == month and vid_data[i][0] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific continent
                counter += 1
    if total == 0: # Special case if the total value is 0, to prevent a divided by 0 error, return 0
        return 0
    else:
        average = total / counter
        return average

def total_days(vid_data,month,key,types,country_continent):
    counter = 0
    average = average_of_month(vid_data,month,key,types,country_continent) # Store the average of specific country/continent
    # If statement to check if its country or continent data that should be processed
    if country_continent == 'country':
        # If statement to check if the data required is for total cases or total deaths for country
        if types == "total_case":
            for i in range(len(vid_data)):
                if vid_data[i][2].split("/")[1] == month and vid_data[i][1] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific country
                    if int(vid_data[i][3]) > average: # If the value of total cases that specific day is above average, increment counter
                       counter += 1
        else:
            for i in range(len(vid_data)):
                if vid_data[i][2].split("/")[1] == month and vid_data[i][1] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific continent
                    if int(vid_data[i][4]) > average: # If the value of total deaths that specific day is above average, increment counter
                       counter += 1
    else:
        # If statement to check if the data required is for total cases or total deaths for continent
        if types == "total_case":
            for i in range(len(vid_data)):
                if vid_data[i][2].split("/")[1] == month and vid_data[i][0] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific country
                    if int(vid_data[i][3]) > average: # If the value of total cases that specific day is above average, increment counter
                       counter += 1
        else:
            for i in range(len(vid_data)):
                if vid_data[i][2].split("/")[1] == month and vid_data[i][0] == key: # Matches the month and the key of the dictionary to get the relevant data for the specific continent
                    if int(vid_data[i][4]) > average: # If the value of total deaths that specific day is above average, increment counter
                       counter += 1
    return counter

"""
                    **dictionary creation and population section**
# pop_dict(dict_data,vid_data,country_continent) populates the specific dictionary with the necessary data
# both_dict_creation(vid_data) creates both dictionaries for country and continent by calling their respective functions
# continent_dict_creation(vid_data) creates the dictionary for continent
# country_dict_creation(vid_data) creates the dictionary for country
"""

def pop_dict(dict_data,vid_data,country_continent):
    month_data = month()
    keys = list(dict_data.keys())
    for key in keys:
        # Populates the first list of the dictionary with A list containing the total number of recorded positive cases of COVID-19 for each month of the year.
        dict_data[key][0] = colation_of_list(vid_data,month_data,key,"total_case",country_continent)
        # Populates the second list of the dictionary with A list containing the total number of recorded deaths due to COVID-19 for each month of the year.
        dict_data[key][1] = colation_of_list(vid_data,month_data,key,"total_death",country_continent)
        # Populates the third list of the dictionary with A list containing the total number of days for each month of year, when the recorded positive cases of COVID-19 for that month
        # of the year were greater than the average recorded positive cases of that month of the year.
        dict_data[key][2] = colation_of_list(vid_data,month_data,key,"total_avg_case",country_continent)
        # Populates the third list of the dictionary with A list containing the total number of days for each month of year, when the recorded deaths due to COVID-19 for that month of the year were
        # greater than the average deaths due to COVID-19 for that month of the year.
        dict_data[key][3] = colation_of_list(vid_data,month_data,key,"total_avg_death",country_continent)
    return dict_data

def both_dict_creation(vid_data):
    continent_dict = continent_dict_creation(vid_data) # calls the continent_dict_creation() function to create an empty continent dictionary
    country_dict = country_dict_creation(vid_data) # calls the country_dict_creation() function to create an empty country dictionary
    return continent_dict,country_dict

def continent_dict_creation(vid_data): 
    continent = dict()
    for i in range(len(vid_data)):
        continent[vid_data[i][0]] = list(([],[],[],[])) # Populate the dictionary with 4 empty list to be replaced later with processed data
    return continent

def country_dict_creation(vid_data):
    country = dict()
    for i in range(len(vid_data)):
        if vid_data[i][0] not in country:
            country[vid_data[i][1]] = list(([],[],[],[])) # Populate the dictionary with 4 empty list to be replaced later with processed data
    return country

"""
                        **File-processing section**
# read_csv_file(csvfile) reads the file and and puts them in a list for processing
# seperate(line,index_list) filters out the data and makes the list more compact for easier data processing
# headers(header) gets the required columns from the file and returns the index of each column
# clean_data(data) replaces all of the non-integer values in the total case and total death columns to 0
# clean_month(data) removes the entire entry if the format of the date provided is wrong
"""

def read_csv_file(csvfile):
    try: # Test to see if the file exist, catch the exception if there is no such file and return with a statement "File not found, now exiting program..."
        csv_file = open(csvfile,"r")
    except FileNotFoundError:
        print("File not found, now exiting program...")
        return
    header = csv_file.readline().split(",") # Store the header as a list for further processing later in the program
    process_file = csv_file.readlines()
    column_index_list = []
    vid_data = []
    try: # Test to see if there are the correct headers in the file, if there are missing columns catch the exception and return with a statement "column missing, now exiting program..."
        column_index_list = headers(header) # The column indexes is extracted from the file
    except:
        print("column missing, now exiting program...")
        return
    for line in process_file: # Here is where the file processing starts
        line = line.lower().split("\n") # each line by "\n" to seperate each line of data
        line = seperate(line,column_index_list) # The function seperate() is called here to further seperate the line into a list
        vid_data.append(line) # append the fully edited list into the master list
    vid_data = clean_data(vid_data) # clean_data() function is called to clean up all the values that do not match the required format
    return vid_data

def seperate(line,index_list):
    lists = []
    lists = line[0].split(",") # Split the specific line by comma, this makes it into a list
    lists = [lists[i] for i in index_list] # here the list will be filtered by the column index list to cut out unwanted data
    return lists

def headers(header):
    continent = header.index('continent') # Gets the index of the first required column
    location = header.index('location') # Gets the index of the second required column
    date = header.index('date') # Gets the index of the third required column
    new_cases = header.index('new_cases') # Gets the index of the fourth required column
    new_deaths = header.index('new_deaths') # Gets the index of the fifth required column
    return continent,location,date,new_cases,new_deaths

def clean_data(vid_data):
    for i in range(len(vid_data)):
        if vid_data[i][3] == '' or vid_data[i][3].isdigit() == False: # Checks to see if the new_case value is incorrect, if true replace with 0
            vid_data[i][3] = '0'
        if vid_data[i][4] == '' or vid_data[i][4].isdigit() == False: # Checks to see if the new_death value is incorrect, if true replace with 0
            vid_data[i][4] = '0'
    vid_data = clean_month(vid_data)
    return vid_data

def clean_month(vid_data):
    tmplist = []
    for i in range(len(vid_data)):
        # Checks to see if the month is in the right format by first checking if it has 3 parts by splitting the string with "/"
        # Next checks to see if the day is in the format of DD followed by the format of the month MM and lastly the format of the year by YYYY
        # If there is an error, store the index of that entire line in a temporary list
        if len(vid_data[i][2].split("/")) < 3 or len(vid_data[i][2].split("/")[0]) > 2 or len(vid_data[i][2].split("/")[1]) > 2 or len(vid_data[i][2].split("/")[2]) > 4 or vid_data[i][2].split("/")[0].isdigit() == False or vid_data[i][2].split("/")[1].isdigit() == False or vid_data[i][2].split("/")[2].isdigit() == False:
            tmplist.append(i)
    # Cycle through the temporary list to remove those lines with an error in the date format
    for i in tmplist:
        vid_data.remove(vid_data[i])
    return vid_data

def month():
    return ['1','2','3','4','5','6','7','8','9','10','11','12'] # Just returns the month data as a list to be used throughout the program