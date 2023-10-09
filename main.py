import random
from api import get_works
from gender_api import get_gender


def gender_counter(authors):
    authors_names_br = []
    gender_count = {'female': 0, 'male': 0, None: 0}
    gender_request_limit = 1000
    for work_authors in authors:
        for author in work_authors:
            if (int(gender_request_limit) == 0):
                break
            if len(author['countries']) > 0 and author['countries'][0] == 'BR':
                author_gender, gender_request_limit = get_gender(author)
                # rand = random.randint(0, 9)
                # author_gender = "female" if rand <= 5 else "male"
                gender_count[author_gender] += 1
                authors_names_br.append(
                    [author['raw_author_name'], author_gender])
    return [authors_names_br, gender_count]


if __name__ == "__main__":
    total_pages, next_cursor, authors = get_works('*', [])
    for page in range(2, 4):
        total_pages, next_cursor, authors = get_works(next_cursor, authors)

    authors_names_br, gender_count = gender_counter(authors)

    with open('results2.txt', 'w', encoding="utf-8") as f:
        for author in authors_names_br:
            if author[1] is None:
                author[1] = "None"
            f.write(author[0] + ' - ' + author[1] + '\n')

        f.write('Total: ')
        f.write("female - " + str(gender_count["female"]))
        f.write('\n')
        f.write("male - " + str(gender_count["male"]))
