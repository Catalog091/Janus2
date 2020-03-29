# pip install beautifulsoup4
# pip install requests
#
#
# make sure this is run with python3
# python3 whatever-you-name-this-file.py
#
#
# it will create a directory along side the file called "results"
#
#
# each result will be stored as an html page inside of "results"
# it will also have a corresponding .txt file with the post_body

import os
import io
import shutil

from bs4 import BeautifulSoup
import requests

# delete old results if they exist
if os.path.exists('results'):
    shutil.rmtree('results')
    os.makedirs('results')
else:
# make results directory if it does not exist
    os.makedirs('results')


base_url = 'http://new-york-city.skipthegames.com'
# url = base_url + '/massage?area[]=BRX&area[]=BRK&area[]=MNH&area[]=NYC&area[]=QUE&area[]=STN&keywords=+incall'
# url = base_url + '/massage?area[]=BRX&area[]=BRK&area[]=MNH&area[]=NYC&area[]=QUE&area[]=STN'
url = base_url + '/massage?area[]=All&area[]=ALB&area[]=DSV-BATH&area[]=BGM&area[]=BRX&area[]=BRK&area[]=BUF&area[]=CSN&area[]=CQN&area[]=KTX&area[]=ELX&area[]=FFD&area[]=FLK&area[]=GFN&area[]=POU&area[]=ITH&area[]=ISP&area[]=MNH&area[]=NYC&area[]=OTH&area[]=OTN&area[]=PGH&area[]=MDN&area[]=QUE&area[]=ROC&area[]=STN&area[]=SYR&area[]=TTN&area[]=UNY&area[]=RMM&area[]=WTO&area[]=WCH'

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.text)
results = soup.select('td#quick_view a')

for num, result in enumerate(results):
    link_title = result.get_text()
    link_url = result['href']

    individual_page_response = requests.get((base_url + link_url), headers=headers)

    with io.open(("results/" + str(num) + ".html"), 'w', encoding='utf-8') as f:
        f.write(individual_page_response.text)

    with io.open(("results/" + str(num) + ".txt"), 'w', encoding='utf-8') as f:
        individual_soup = BeautifulSoup(individual_page_response.text)
        post_body = individual_soup.select('#post-body')[0].text
        f.write(post_body)

    print(result.get_text())
    print(result.attrs['href'])