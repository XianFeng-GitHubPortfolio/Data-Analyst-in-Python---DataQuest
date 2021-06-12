from csv import reader
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)[1:] 

for row in moma:
    nationality = row[2] 
    gender = row[5] 

# Remove parantheses from nationality column 
# Replace blank nationalities "", with "Nationality Unknown" and capitalize nationalities
# Assign the modified variable back to the list index of 2 for each row

    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    
    if nationality == "":
        nationality = "Nationality Unknown"
    else:
        nationality = nationality.title()
    
    row[2] = nationality

# Remove parantheses from gender column 
# Replace blank nationalities "", with "Gender Unknown/Other" and capitalize genders
# Assign the modified variable back to the list index of 5 for each row    
    
    gender = gender.replace("(","")
    gender = gender.replace(")","")
    
    if gender == "":
        gender = "Gender Unknown/Other"
    else:
        gender = gender.title() 
    
    row[5] = gender
    
    
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
    
    
# Create a function that cleans date columns by removing parentheses and also converts the string values in date columns to integers.
# The modified variables replaces the previously uncleaned variables.

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma: # Uses the moma lists of list defined in the cell block above
    BeginDate = row[3]
    EndDate = row[4] 
    
    row[3] = clean_and_convert(BeginDate)
    row[4] = clean_and_convert(EndDate) 
 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create  a function called strip_characters that strips strings of pre-defined bad characters. 
# Apply that function to a test dataset.
# Create a new list void of bad characters called stripped_test_data.  

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = str.replace(char,"")
    return string

stripped_test_data = []
for entry in test_data:
    clean_entry = remove_bad_chars(entry)
    stripped_test_data.append(clean_entry)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Define a function called process_date that returns the integer value of each input.
# If the input is a date range, return the average of the range, rounded to the nearest integer.
# Pass each entry in the date column through the strip_characters and process_date functions. 
# Replace the old value with the modified value.

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

  
def process_date(date):
    if '-' in date:
        date = round((int(date[:4])+int(date[-4:]))/2)
    else:
        date = int(date)     
    return date
    
    
for row in moma:
    date = strip_characters(row[6])
    date = process_date(date)
    row[6] = date





