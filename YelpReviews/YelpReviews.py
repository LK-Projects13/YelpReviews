#This project was developed using the YELP API to extract Restaurant Reviews

#Import requests module
import requests

#Define a restaurant id
restaurant_id = "bollywood-grill-milwaukee-6"

#Define API, endpoint and headers
API_KEY = "<enter your API KEY>"
ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(restaurant_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Make request to Yelp API
response = requests.get(url = ENDPOINT, headers = HEADERS)

#Convert from JSON to dictonary 
restaurant_data = response.json()

#Print review details
print (restaurant_data)
