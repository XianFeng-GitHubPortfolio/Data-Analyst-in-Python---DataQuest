# Create function that extracts the values for any column we want in a separate list. 
# Create a function that generates a frequency table for a list. 

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index): # Define a function called extract that has an index parameter 
    column = [] # Initialize an empty list called column
    for row in apps_data[1:]: # For each row in the apps_data list after the header row 
        value = row[index] # Assign the "input-th" indexed item to the variable value        
        column.append(value) # Append value to the column list  
    return column # Return the column list 

def freq_table(a_list): # Define a function called freq_table that has a list parameter
    freq_dict = {} # Initialize an empty dictionary
    for element in a_list: # For each element in the input list   
        if element in freq_dict: # If the element is in the dictionary freq_dict 
            freq_dict[element] += 1 # Add one to the counter 
        else: 
            freq_dict[element] = 1 # Else, initialize a value of 1 
    return freq_dict # Return freq_dict

genres_ft = freq_table(extract(11)) # Creates a genre freq table based on the 11th indexed item in the apps_data list





# Write a function named freq_table() that generates a frequency table for any column in any data set by taking in two parameters.
# Assume the first row of the data set to be a header row. 

def freq_table(data_set, column): # Define the freq_table function with 2 parameters, a data set and a column number
    freq_dict = {} # Initialize an empty frequency table dictionary 
    
    for row in data_set[1:]: # For each row after the header in the dataset parameter
        element = row[column] # Assign the "column-th" item in each row to a variable called element  
        if element in freq_dict: # If the element is in the frequency table dictionary, freq_dict
            freq_dict[element] += 1 # Add one to its counter
        else:
            freq_dict[element] = 1 # Else, initialize a value of 1
    
    return freq_dict # Return the frequency table dictionary, freq_dict
  
  

  

# Write a function named mean() that computes the mean for any column we want from a data set.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    a_list = extract(data_set, index) 
    sum_list = find_sum(a_list)
    len_list = find_length(a_list) 
    mean_list = sum_list/len_list
    
    return mean_list

avg_price = mean(apps_data,4)
  
  
