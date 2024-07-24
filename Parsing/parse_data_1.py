#Here we will going to parse data form an txt file

#First - define the file and its path
file_path = "groceries.txt"

with open(file_path, "r") as file:
    data = file.read()

#Show the data
print('data: ' + data)

parseData = data.split(", ") ##Remember, this command creates a list of the elements received
#This is useful when we want to specify by an index an element of the list or the information
print('parsed data: ' , parseData)
#so, if we want one or more specific elements of the parsed list, we can call them with an index
print("Information lovated: ", parseData[2])



