# Map content ratings to their corresponding number of ratings in the iOS app store inside a dictionary.
# Retrieve the value at index 12+ from the content_ratings dictionary. Assign it to a variable named over_12_n_apps.

content_ratings = {}
content_ratings['4+'] = 4433;
content_ratings['9+'] = 987;
content_ratings['12+'] = 1155;
content_ratings['17+'] = 622;

over_12_n_apps = content_ratings['12+']

  
  

# What percentage of apps has a content rating of '17+'?
# What percentage of apps can a 15-year-old download?

opened_file = open('AppleStore.csv') # Opens desired file
from csv import reader # Import reader
read_file = reader(opened_file) # Reads file
apps_data = list(read_file) # Converts file to list

content_ratings = {} # Initialize content dictionary

for row in apps_data[1:]: # For each row in list excluding the header in apps_data[0] 
    c_rating = row[10] # Content rating is the 11th for each row 
    if c_rating in content_ratings: # If c_rating is in content_ratings dictionary, add 1 to counter  
        content_ratings[c_rating] += 1
    else: # Else, if it not yet in content_ratings dictionary, initialize counter at 1
    	content_ratings[c_rating] = 1
        
total_number_of_apps = 0 
        
for c_rating in content_ratings:
	total_number_of_apps = content_ratings[c_rating] + total_number_of_apps # Total number of apps


for dict_key in content_ratings: 
    content_ratings[dict_key] /= total_number_of_apps # Overwrite original dictionary values to proportions 
    content_ratings[dict_key] *= 100 # Convert updated proportional dictionary values to percentages
    
print(content_ratings)

percentage_17_plus = content_ratings['17+'] # Percentage of apps that has a content rating of 17+
percentage_15_allowed = 100-percentage_17_plus # Percentage of apps that 15 year olds can download





# Create three separate dictionaries: one storing frequencies, another storing proportions, and another storing percentages.

opened_file = open('AppleStore.csv') # Opens desired file
from csv import reader # Import reader
read_file = reader(opened_file) # Reads file
apps_data = list(read_file) # Converts file to list

content_ratings = {} # Initialize content dictionary

for row in apps_data[1:]: # For each row in list excluding the header in apps_data[0] 
    c_rating = row[10] # Content rating is the 11th for each row 
    if c_rating in content_ratings: # If c_rating is in content_ratings dictionary, add 1 to counter  
        content_ratings[c_rating] += 1
    else: # Else, if it not yet in content_ratings dictionary, initialize counter at 1
    	content_ratings[c_rating] = 1
        
total_number_of_apps = 0 
        
for c_rating in content_ratings:
	total_number_of_apps = content_ratings[c_rating] + total_number_of_apps # Total number of apps
    
c_ratings_proportions = {} # Initilize proportion and percentage dictionaries 
c_ratings_percentages = {}

for key in content_ratings:
    proportion = content_ratings[key]/total_number_of_apps # Calculate proportion for each dictionary value 
    c_ratings_proportions[key] = proportion # Assign proportional dictionary value to corresponding key in c_ratings_proportions
    
    percentage = proportion*100 
    c_ratings_percentages[key] = percentage # Assign percentage dictionary value to corresponding key in c_ratings_percentages



    
    
# Based on the max and min value, choose 5 intervals to base your frequency table off of. 
# Store the frequency table in a dictionary.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

total_ratings_list = [] # Create an empty total ratings list

for row in apps_data[1:]:
    total_ratings = int(row[5]) # Assign the total user ratings of each app from apps_data to the total_ratings variable as an int
    total_ratings_list.append(total_ratings) # Append the total_ratings variable to total_ratings_list

min_total_ratings = min(total_ratings_list)
max_total_ratings = max(total_ratings_list)

# Create total ratings dictionary 
total_ratings_dict = {'0 - 10000': 0, '10000 - 100000': 0, '100000 - 500000': 0, '500000 - 1000000': 0, '1000000+': 0} 

# Populate the dictionary values of the total ratings dictionary 
for row in apps_data[1:]:
    user_ratings = int(row[5])
    
    if user_ratings <= 10000:
        total_ratings_dict['0 - 10000'] += 1
        
    elif 10000 < user_ratings <= 100000:
        total_ratings_dict['10000 - 100000'] += 1
        
    elif 100000 < user_ratings <= 500000:
        total_ratings_dict['100000 - 500000'] += 1
        
    elif 500000 < user_ratings <= 1000000:
        total_ratings_dict['500000 - 1000000'] += 1
        
    elif user_ratings > 1000000:
        total_ratings_dict['1000000+'] += 1
