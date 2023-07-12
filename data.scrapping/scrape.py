import urllib.request


from bs4 import BeautifulSoup

import pprint

url = ('https://news.ycombinator.com/')
url2 = ('https://news.ycombinator.com/?p=2')

res = urllib.request.urlopen(url)

res2 = urllib.request.urlopen(url2)

soup = BeautifulSoup(res.read(), 'html.parser')
soup2 = BeautifulSoup(res2.read(), 'html.parser')


links = soup.select('.titleline')
votes = soup.select('.score')

links2 = soup2.select('.titleline')
votes2 = soup2.select('.score')

mega_links = links + links2
mega_votes = votes + votes2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()

        href = links[idx].find('a')
        href.get('href', None)
        points = int(votes[0].getText().replace('points', ''))
    
        if points >= 99:
            hn.append({'title': title, 'links': href,'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_votes))