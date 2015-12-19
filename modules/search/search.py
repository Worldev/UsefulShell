import urllib, urllib.parse, urllib.request
import json

def search(search_string):
    """Search a query to Google"""
    query = urllib.parse.urlencode({'q': search_string})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s&rsz=large' % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    data = results['responseData']
    print('Total results: %s' % data['cursor']['estimatedResultCount'])
    hits = data['results']
    print('Top %d hits:' % len(hits))
    for h in hits: print(' ', h['url'])
    print('For more results, see %s' % data['cursor']['moreResultsUrl'])
    return hits