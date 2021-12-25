import json
import os
import requests
import time

if not os.path.exists('cache/'):
    os.makedirs('cache/')


def save():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34107611450150347083_1580736608778' \
          '&_=%d' % int(time.time() * 1000)
    content = str(requests.get(url=url).content, encoding='utf8')
    content = content[content.index('{'):-1]
    with open('cache/data.json', 'w', encoding='utf-8') as writeFile:
        writeFile.write(content)
    data = json.loads(content)['data']
    data = json.loads(data)
    countries = data['areaTree']
    print(len(countries))
    for country in countries:
        print(country['name'])
    country = countries[0]
    print(country['name'])
    provinces = country['children']
    for province in provinces:
        print(' ', province['name'])
        cities = province['children']
        for city in cities:
            print('   %s  %d %d %d %d' % (city['name'], city['total']['confirm'],
                                          city['total']['suspect'], city['total']['dead'],
                                          city['total']['heal']))


def request():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34107611450150347083_1580736608778' \
          '&_=%d' % int(time.time() * 1000)
    proxies = {"http": None, "https": None}
    content = str(requests.get(url=url, proxies=proxies).content, encoding='utf8')
    content = content[content.index('{'):-1]
    data = json.loads(content)['data']
    with open('cache/data.cache', 'w', encoding='utf-8') as writeFile:
        writeFile.write(data)
    return json.loads(data)


def main():
    data = request()
    print(type(data['chinaTotal']))
    print(type(data['areaTree']))
    print(type(data['areaTree'][0]))
    print(type(data['areaTree'][0]['today']))
    print(type(data['areaTree'][0]['children']))
    print(type(data['areaTree'][0]['children'][0]))
    print(type(data['areaTree'][0]['children'][0]['children']))
    print(type(data['areaTree'][0]['children'][0]['children'][0]))


if __name__ == '__main__': main()
