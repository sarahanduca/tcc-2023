import requests
import json

url = 'https://api.openalex.org/works?filter=institutions.id:I123443094,publication_year:2018-2021&per-page=100&cursor='


def get_works(cursor, authors):
    resp = requests.get(url + cursor)
    resp_json = json.loads(resp.text)
    total_pages = resp_json['meta']['count']//resp_json['meta']['per_page']
    next_cursor = resp_json['meta']['next_cursor']
    authors += [work['authorships'] for work in resp_json['results']]
    return [total_pages, next_cursor, authors]
