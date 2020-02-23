from pprint import pprint
from requests_html import HTMLSession


def get_response(keyword, top_count):
    result = {}
    number = 0

    session = HTMLSession()

    google_url = f'https://www.google.com/search?q={keyword}&num={top_count}&hl=en'
    resp = session.get(google_url)
    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
    text = resp.html.xpath('//div[@class="r"]/a/h3/text()')
    description = [element.text for element in resp.html.find('.st')]

    for i in links:
        result[i] = {
            'position': number + 1,
            'title': text[number],
            'description': description[number]
        }
        number += 1

    return result

keyword = 'software development company'
top_count = 10



print('*'*50)
pprint(get_response(keyword, top_count))
print('*'*50)