#In this project we will read a file and other simple operations with the files

import numpy as np

#Initially open the file
inputFile = open("Files/inputFile.txt", 'r')
#No, print the info read
#print(inputFile.read())

print()

#Lets to apply a simple filter, iteratin through the rows
for i in inputFile:
    lineSplit = i.split() #This command converts the sequence in a list
    if lineSplit[2] == "P":
        print(i)
    

inputFile.close()




