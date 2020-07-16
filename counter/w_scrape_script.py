# BS4 web scrraping imports
from bs4 import BeautifulSoup
import requests
import re

# Webscrape script
source = requests.get('https://korona.gov.sk/').text
soup = BeautifulSoup(source, 'lxml')
info_block = soup.find('div', id='block_5e9990d35fffd')
numbers = [x.text for x in info_block.find_all('h2', class_='govuk-heading-l govuk-!-margin-bottom-3')]
confirmed_today = soup.find_all('div', class_='govuk-!-margin-bottom-6 app-pane-gray govuk-!-padding-top-4 govuk-!-padding-bottom-2 govuk-!-padding-right-4 govuk-!-padding-left-4')
confirmed_today = [x.text for x in confirmed_today]
confirmed_today = confirmed_today[1]
confirmed_today = (re.findall('\d+', confirmed_today ))

tested = numbers[0]
confirmed = numbers[1]
confirmed_today = confirmed_today[2]
deaths = numbers[2]
cured = numbers[3]