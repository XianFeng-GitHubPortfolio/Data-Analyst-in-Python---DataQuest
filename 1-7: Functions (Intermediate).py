# Build a function that opens CSV files and set the iOS apps data set ('AppleStore.csv') as the default argument. 

def open_dataset(file_name= 'AppleStore.csv'): # Define the open_dataset function and set 'AppleStore.csv' as the default argument
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data
  

  

# Build a function that takes two numbers as the input and returns either the sum of the two numbers of the difference between the two numbers. 

def sum_or_diff(a, b, do_sum=True): # The do_sum variable has a default argument of True
    if do_sum: # If do_sum has a value of True, then we return a+b
        return a+b
    else: # Else (if do_sum is False), we return a-b
        return a-b

 


# Build a function that opens CSV files and converts it into a list.
# The function takes two input parameters, a file name and boolean of whether it contains a header row or not. 
# If the data set has a header, the function returns separately both the header and the rest of the data set.
# Else (if there's no header), the function returns the entire data set.

def open_dataset(file_name, header):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header == True:
        return data[0], data[1:]
    else:
        return data
      
# Open the AppleStore.csv file, which has a header row. Assign the result to a variable named all_data. 
# From the all_data tuple, assign the header to a vairable named header and assign the rest of the data set to a variable named apps_data. 

all_data = open_dataset('AppleStore.csv', True)
header  = all_data[0]
apps_data = all_data[1] # You can also use 'apps_data, header = all_data ' to assignt he variable names
