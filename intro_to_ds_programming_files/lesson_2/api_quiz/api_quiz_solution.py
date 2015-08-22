import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    # data = requests.get(url).text

    # Modified to work with provided JSON file
    with open("lastfm.json") as json_file:
    	data = json.load(json_file) 
    
    # my solution
    # top_artists = data['topartists']
    # top_artist = top_artists['artist'][0]
    # return top_artist['name'] # return the top artist in Spain

    # udacity solution
    	return data['topartists']['artist'][0]['name']


if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain


	url = 1
	print api_get_request(url) 

