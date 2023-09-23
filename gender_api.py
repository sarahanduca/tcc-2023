import requests
import json

url = 'https://api.genderize.io'
headers = {'X-Rate-Limit-Remaining': 'true'}


def get_gender(author):
    gender_api = url + "/?name=" + \
        (author['raw_author_name'].split(
            " ")[0]) + "&country_id=BR"
    gender_resp = requests.get(gender_api,  headers=headers)
    author_gender = json.loads(gender_resp.text)
    print(gender_resp.headers['X-Rate-Limit-Remaining'])
    return author_gender['gender'], gender_resp.headers['X-Rate-Limit-Remaining']
