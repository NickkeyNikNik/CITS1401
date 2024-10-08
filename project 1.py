"""
# Project 1
# Name: Nicodemus Ong
# Student ID: 22607943
"""

def main(csvfile,country,type):
    """
    The reason for doing .lower().replace(' ', '') is to ensure
    1. All data will be presented in lower case to avoid capitalization error
    2. Remove unwanted spaces from the data provided
    """
    month = month_data() # Getting data for the month
    if type.lower().replace(' ','') == "statistics":
        vid_data = read_csv_file(str(csvfile),str(country).lower().replace(' ', '')) # Extracting the data from the file for the specific country
        mn,mx,av,sd = stats(vid_data,month) # Calling the functions to return the desired outputs
        return mn,mx,av,sd
    else:
        vid_data1 = read_csv_file(str(csvfile),str(country[0]).lower().replace(' ', '')) # Extracting the data from the file for the first country 
        vid_data2 = read_csv_file(str(csvfile),str(country[1]).lower().replace(' ', '')) # Extracting the data from the file for the second country
        mnc,mxc,avc,sdc = corre(vid_data1,vid_data2,month) # Getting the correlation data between both countries
        return mnc,mxc,avc,sdc

"""
# This function returns the required data for minimum, maximum, average and standard deviation by calling
  the respective functions
# This is for statistic type
"""
def stats(vid_data,month):
    mini = total_list_for_avg_sd_min_max(vid_data,month,'min')
    maxi = total_list_for_avg_sd_min_max(vid_data,month,'max')
    aver = total_list_for_avg_sd_min_max(vid_data,month,'av')
    sd = total_list_for_avg_sd_min_max(vid_data,month,'sd')
    return mini,maxi,aver,sd

"""
# This function gets the minimum, maximum, average and standard deviation of both countries and than calculates and return the correlation
# This function is for Correlation type
"""

def corre(vid_data1,vid_data2,month):
    mn1,mx1,av1,sd1 = stats(vid_data1,month)
    mn2,mx2,av2,sd2 = stats(vid_data2,month)
    mn3,mx3,av3,sd3 = cor_of_x_y(mn1,mn2),cor_of_x_y(mx1, mx2),cor_of_x_y(av1,av2),cor_of_x_y(sd1,sd2)
    return mn3,mx3,av3,sd3

"""
# read_csv_file(csvfile,country) function reads the file and extracts out the data for the specific country and stores it in a list
# seperate_read_file(vid_data,country) function helps to further process the list into a list of lists where for easier data extraction
  throughout the program
"""
def read_csv_file(csvfile,country):
    vid_data = []
    dict_data = []
    in_file = open(csvfile,"r")
    next(in_file)
    for lines in in_file:
        if country in lines.lower().replace(' ', ''): # .lower().replace(' ', '') ensures the data has no spaces and capitilization error
            lines = lines.replace(' ','')
            vid_data = vid_data + lines.lower().split() # The data is being split and stored into a list
    in_file.close()
    dict_data = seperate_read_file(vid_data,country) # the call to this function further breaks down the list into a list of list
    return dict_data
def seperate_read_file(vid_data,country):
    dict_data = []
    for x in range(len(vid_data)):
        if (country == vid_data[x].split(",")[2:5][0]): 
            dict_data.append(vid_data[x].split(",")[2:5]) # Cuts away unwanted information and only stores country,date and case
    return dict_data
"""
# total_list_for_avg_sd(vid_data,month,avg_sd) function compiles the data for every month for either:
# Minimum
# Maximum
# Average
# Standard Deviation
# and returns the data as a list
"""

def total_list_for_avg_sd_min_max(vid_data,month,min_max_av_sd):
    total_list = []
    if min_max_av_sd == 'min':
        for a in range(len(month)):
            total_list.append(extract_month_case_min_max(vid_data,month[a],min_max_av_sd))
    elif min_max_av_sd == 'max':
        for a in range(len(month)):
            total_list.append(extract_month_case_min_max(vid_data,month[a],min_max_av_sd))
    elif min_max_av_sd == 'av':
        for a in range(len(month)):
            total_list.append(average_of_month(vid_data,month[a]))
    else:
        for a in range(len(month)):
            total_list.append(standard_deviation_of_month(vid_data,month[a]))
    return total_list

"""
# Extract_month_case_min_max(vid_data,month,min_or_max) function extracts the data out of the master list of data
# For months that have no cases it returns 0
# Removes 0 from the extracted data, this ensures that the minimum will not be returned as 0, only when there is no cases in the month will it return 0
# Note that this function only returns for a specific month and returns 1 value depending if its min or max
"""

def extract_month_case_min_max(vid_data,month,min_or_max):
        min_or_max_case = []
        for x in range(len(vid_data)):
            if vid_data[x][1].split("/")[1] == month and int(vid_data[x][2]) > 0: # Checks the data to match both the month and ensure the data is not 0
                min_or_max_case.append(int(vid_data[x][2])) # Puts the data into a list to be sorted later in the function
        if min_or_max_case == []: # Special case for when there are no cases in that specified month, it returns a 0
            return 0
        else:
            if min_or_max == 'min': # Returns min or max case based on the desired result
                return min(min_or_max_case)
            else:
                return max(min_or_max_case)

"""
# average_of_month(vid_data,month) function calculates the average for a specific month and returns the value
# standard_deviation_of_month(vid_data,month) function calculates the standard deviation for a specific month and returns the value
# Average formula is total population / count of days
"""

def average_of_month(vid_data,month):
    total_case = 0
    count = 0
    for x in range(len(vid_data)):
        if vid_data[x][1].split("/")[1] == month:
            total_case += int(vid_data[x][2]) # Accumulation of data
            count += 1
    if count == 0: # special case if there are no cases in the month
        return 0
    else:
        total_case /= count # Average formula is applied here
        return round(total_case,4)

"""
# Standard deviation formula is slightly more complicated so it has been broken down into steps
# Step 1: calculate the summation of (xi - u)**2 where xi represents each value from the population and u represents the population mean
# Step 2: calculate N where N represents the count of days
# Step 3: take the results from step 1 and devide them with the results of step 2
# Step 4: Finally squareroot the result from step 3 and you will get the standard deviation
"""

def standard_deviation_of_month(vid_data,month):
    sum_of_sd = 0
    standard_deviation = 0
    count = 0
    average = average_of_month(vid_data,month)
    for x in range(len(vid_data)):
        if vid_data[x][1].split("/")[1] == month:
            sum_of_sd += (int(vid_data[x][2]) - average)**2 # Step 1
            count += 1 # Step 2
    if count == 0: # Special case if there are no cases for that month return 0
        return 0
    else:
        standard_deviation = sum_of_sd / count # Step 3
        standard_deviation = standard_deviation**0.5 # Step 4
        return round(standard_deviation,4)

"""
# For Correlation, it has been broken down into different functions to calculate different parts of the equation
# cor_of_x_y(value_of_x, value_of_y) will call all the different functions and apply the full equation
# Step 1: super_sum_x_y(value_of_x_y) function will get the summation of (X-Mx)**2 or (Y-My)**2 depending on which data is provided
# Step 2: combined_x_y(value_of_x, value_of_y) function than combines both summation of X and Y as represented by summation(X-Mx)(Y-My)
# Step 3: average_x_y(value_for_average) function returns the average for either X or Y depending on what data was provided
# return the correlation data
"""
def cor_of_x_y(value_of_x, value_of_y):
    total_for_x = super_sum_x_y(value_of_x) # Step 1: getting sum of X
    total_for_y = super_sum_x_y(value_of_y) # Step 2: getting sum of Y
    if total_for_x == 0 or total_for_y == 0: # special case if one of the countries has 0 cases return 0 for corelation
        return 0
    combine_x_y = combined_x_y(value_of_x,value_of_y) # Step 3: combining X and Y
    corr = combine_x_y / (total_for_x * total_for_y)**0.5 # applying the full equation of correlation
    return round(corr,4)

def super_sum_x_y(value_of_x_y):
    average = average_x_y(value_of_x_y)
    total_for_x_y = 0
    for a in range(len(value_of_x_y)):
        total_for_x_y += (value_of_x_y[a] - average)**2
    return total_for_x_y

def combined_x_y(value_of_x, value_of_y):
    average_of_x = average_x_y(value_of_x)
    average_of_y = average_x_y(value_of_y)
    combine_x_y = 0
    for a in range(12):
        combine_x_y += (value_of_x[a] - average_of_x)*(value_of_y[a] - average_of_y)
    return combine_x_y

def average_x_y(value_for_average):
    average = sum(value_for_average)/len(value_for_average)
    return average

"""
# Month_data() just returns the month in a list to be used throughout the program
"""

def month_data():
    return ["01","02","03","04","05","06","07","08","09","10","11","12"]


    
