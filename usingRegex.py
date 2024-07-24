#In this file we will know how to extract information using Regular Expersions

#Import the regex library
import re

#Initialy we write the Regex expresion knowin what specifically we want
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#This is the logic, 3 numbers, then a hyphen, then 3 digits more, then a hyphen and finnaly 4 digits

example = 'My number is 123-123-1234'

#Now, apply the Regex to our example using the method SEARCH

result = phoneNumberRegex.search(example)

print(result)
#This retuns me the follwoing: <re.Match object; span=(13, 25), match='123-123-1234'>
#So we need to modify our out
print('using group only: ', result.group())                         #Return me 123-123-1234
print('Using group and the coordinates: ', result.group()[0:3])     #Return me 123







