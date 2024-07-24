#This code writes information specifit within other files

inputFile = open('Files/inputFile.txt', 'r')

passFile = open('Files/passFile.txt', 'w')

failFile = open('Files/failFile.txt', 'w')


for i in inputFile:
    lineSplit = i.split() #This command converts the sequence in a list
    if lineSplit[2] == "P":
        passFile.write(i)
    else:
        failFile.write(i)
        
inputFile.close()
passFile.close()
failFile.close()










