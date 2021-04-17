import pandas as pd
from gazpacho import get, Soup

url = "https://pypi.org/project/pandas/#history"

html = get(url)

soup = Soup(html)

cards = soup.find('a', {'class': 'card'})


def parse_card(card):
    version_number = card.find('p', {'class': "release__version"}, partial=False).text
    timestamp = card.find('time').attrs['datetime']
    return {'version': version_number, 'timestamp': timestamp}

result = pd.DataFrame([parse_card(c) for c in cards])

print(result)