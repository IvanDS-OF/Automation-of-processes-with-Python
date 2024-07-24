#Here we will parse data from an Json file

#Import all the libraries
import json

#Define the path 
file_path = "groceries.json"

with open(file_path, 'r') as file:
    data = file.read()

#The Json library allows us to parse the information from a json file
parsed_data= json.loads(data)
#And the way to index the infromatioi is using the KEY
print("Specific information: ", parsed_data["apples"])








