import requests
import json
import math

url = 'https://api.openalex.org/works?filter=institutions.id:I123443094&per-page=100&cursor='


def get_works(cursor, authors):
    resp = requests.get(url + cursor)
    resp_json = json.loads(resp.text)
    total_pages = math.ceil(
        resp_json['meta']['count']/resp_json['meta']['per_page'])
    next_cursor = resp_json['meta']['next_cursor']
    authors += [work['authorships'] for work in resp_json['results']]
    return [total_pages, next_cursor, authors]
