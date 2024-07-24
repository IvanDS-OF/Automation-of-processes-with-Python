#Here we will discover automation of input validation
#Understand its role as a shield

#Import the library needed
import pyinputplus as pyip

print('EXAMPLE 1')


result = pyip.inputInt('Enter the number of shopping bag you will need for your items: ', min=0)

print('You will use: ', result, 'store bags')

#Ww can use this type of validation in different types: Using a list
result = pyip.inputMenu(['red', 'blue', 'greeb'], lettered=True, numbered=False)
print('you have chosen: ',  result)

#An even with an email
result = pyip.inputEmail('Enter a valid email addres :D')
print('Your email is: ', result)






