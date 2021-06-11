# Compute the average rating of the apps that have a price greater than $9.
# Find out how many apps have a price greater than $9 and assign the result to a variable named n_apps_more_9.
# Find out how many apps have a price less than or equal to $9 and assign the result to a variable named n_apps_less_9.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

above_9_ratings = [] # Initialize an empty list called above_9_ratings
for row in apps_data[1:]: # For each row after the header row 
	if float(row[4]) > 9: # If the price (4th indexed item) of the app is greater than $9
		above_9_ratings.append(float(row[7])) # Append the corresponding rating to the above_9_ratings list   

avg_rating = sum(above_9_ratings)/len(above_9_ratings) # Calculate average rating of apps that have a price of greater than $9 

n_apps_more_9 = 0 # Initialize counter for apps that cost more than $9 
for row in apps_data[1:]: 
    if float(row[4]) > 9:
        n_apps_more_9 = n_apps_more_9 + 1

n_apps_less_9 = 0 # Initialize counter for apps that cost less than $9 
for row in apps_data[1:]:
    if float(row[4]) < 9:
        n_apps_less_9 = n_apps_less_9 + 1




# Label each app as "free," "affordable," "expensive," or "very expensive" in a newly created column called price_label. 

pened_file = open('AppleStore.csv') # Open file
from csv import reader # Import reader
read_file = reader(opened_file) # Read file
apps_data = list(read_file) # Convert file to a list

for app in apps_data[1:]: # For each row after the header in the apps_data list
    price = float(app[4]) # Set price to equal the 4th indexed item in each row as a float
    if price == 0: # If price is 0, label the app as free by appending the string 'free' at the end of the current row
        app.append('free')
    elif 0 < price < 20:
        app.append('affordable')
    elif 20 <= price < 50: 
        app.append('expensive')
    else:
        app.append('very expensive')
        
apps_data[0].append('price_label') # Append the strong 'price_label' to the first (header) row of the apps_data list
print(apps_data[:6]) # Print the header row and first 5 data rows
