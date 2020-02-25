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

    # for i in links:
    #     result[i] = {
    #         'position': number + 1,
    #         'title': text[number],
    #         'description': description[number]
    #     }
    #     number += 1
    #
    # return result
    return links, text, description


number = 0
result = {}
keyword = 'software development company'
top_count = 10

request = get_response(keyword, top_count)
print(request[0][0], request[1][0], request[2][0])
# for i in request[0]:
    # result[i] = {
    #     'position': number + 1,
    #     'title': request[1][number],
    #     'description': request[2][number]
    # }
    # number += 1



# print('*'*50)
# pprint(request[0])
# pprint(request[1])
# pprint(request[2])
# print('*'*50)