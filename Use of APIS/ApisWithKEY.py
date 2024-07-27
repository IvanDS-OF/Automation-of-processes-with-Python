#There are some apis that required some Key to be used, or just for security. 
#In this project we will review how to implement the keys when we want use an API


#Once obtained the key and the setting steps, lets to code
#Iport all the libraries
import requests

url = 'https://openweathermap.org/forecast5#name5'
#url = 'https://api.openweathermap.org/data/2.5/forecast'



#Use of the commands to use the API besithe its key
parameters = {'q': 'Paris,FR',
              'appid': '*'}

response = requests.get(url, params=parameters)



#print(response.text)



