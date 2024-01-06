import json 
import os

# function to save dictionary as json file
def save_json(dictionary, filename):
    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile)
        
# function to load json file as dictionary
def load_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)
    
# function to create directory if it does not exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


    