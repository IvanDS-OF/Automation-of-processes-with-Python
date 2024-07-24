#In this project we weill lear how to call and use  an API from upcitemdb

#Import all the libraries needed
import requests

#Define the url
url = 'https://api.upcitemdb.com/prod/trial/lookup'

#Define the parameter that we can type later
parameters = {'upc': '025000044908'}


#Use the API
response = requests.get(url, params=parameters)

print(response.url)

#Simply, this code returns us a web page where the information of the 
#Product is 


#Now we are goin to extract the information and show the specific that we want from the response
#Import the libraries needed
import json

#Now we need to parse the information obtained
info = json.loads(response.text)
#Is recommendable to parse the information using Json and it command .loads
#This could make eaasy the work of extract the information needed correctly

item = info['items'][0]

tittle = item['title']

brand = item['brand']



#No we print the information obtained

print('title: ', tittle)
print('brand: ', brand)













