import requests
import json
import os
import sys
import time

# Enable import of our secret key
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from src.video_store.settings import TMDB_API_KEY

movie_list = os.path.join(project_root, 'MOVLIST.JSON')
result_list = os.path.join(project_root, 'linked.txt')

api_root = 'http://api.themoviedb.org/3/'
search_url = api_root + "search/movie"
api_kwargs = {
    'headers': {'Accept': 'application/json'},
    'params': {'api_key': TMDB_API_KEY}
}

with open(movie_list, 'r') as f:
    data = json.loads(f.read())

try:
    start_at = int(sys.argv[1])
except IndexError:
    raise Exception("Please provide an index to start at.")

for index, movie in enumerate(data):
    if index < start_at:
        continue

    print "[%d] Searching for %s..." % (index, movie['Movie Title'])

    api_kwargs['params']['query'] = movie['Movie Title']
    response = requests.get(search_url, **api_kwargs)
    results = response.json()['results']

    for result in results:
        print "\t", result['title'], "(id %s)" % result['id']

    # If we have one
    if len(results) == 1:
        movie['title'] = results[0]['title']
        movie['id'] = results[0]['id']
        with open(result_list, 'a') as f:
            f.write(json.dumps(movie) + "\n")

    # Let's not get throttled
    time.sleep(1)

print "Successfully matched %d out of %d." % (
    len(successful_matches),
    len(data)
)
